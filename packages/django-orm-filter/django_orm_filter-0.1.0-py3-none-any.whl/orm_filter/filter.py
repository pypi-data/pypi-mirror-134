import re
import types

from django.db.models import Q
from rest_framework import exceptions
from rest_framework.request import Request, QueryDict


class FQ:
    def __init__(
        self,
        pattern_str: str,
        fv: types.FunctionType = None,
        error_text: str = None,
        repl: str = None,
        many: bool = False,
        cond: str = "AND",
        is_not: bool = False,
    ) -> None:
        """查询参数匹配

        Args:
            pattern_str (str): [匹配查询参数的正则字符串，匹配成功的才会进行过滤查询]
            fv (types.FunctionType, optional): [格式化查询参数的值]. Defaults to None.
            error_text (str, optional): [格式化失败返回的错误字符串]. Defaults to None.
            repl (str, optional): [转换查询参数的正则字符串]. Defaults to None.
            many (bool, optional): [查询参数是否为数组]. Defaults to False.
            cond (str, optional): [AND或则OR查询]. Defaults to "AND".
            is_not (bool, optional): [非逻辑查询]. Defaults to False.
        """
        (
            self.pattern_str,
            self.fv,
            self.error_text,
            self.repl,
            self.many,
            self.cond,
            self.is_not,
        ) = (pattern_str, fv, error_text, repl, many, cond, is_not)

        self._filter_key = None
        self._filter_value = None

    def match(self, query_key: str) -> bool:
        """查询参数匹配"""
        return not not re.search(self.pattern_str, query_key)

    def format(self, query_value: str):
        """查询值格式化
        返回None会跳过查询
        """
        return self.fv(query_value) if self.fv else query_value

    def replace(self, k: str) -> str:
        """转换查询参数"""
        if self.repl is None:
            return k
        return re.sub(self.pattern_str, self.repl, k)

    @property
    def is_and(self) -> bool:
        """是否为AND或则OR查询"""
        return self.cond.upper() == "AND"

    def get_Q(self):
        assert(self._filter_key is not None and self._filter_value is not None)
        q = Q((self._filter_key, self._filter_value))
        return ~q if self.is_not else q


class OrmFilter:
    """
    ## 在视图中添加ORM过滤器后端

    查询参数匹配，查询数据转换，错误消息，别名配置

    使用正则表达式匹配查询参数

    ```py
    from orm_filter.filter import OrmFilter, FQ

    class UserViewSet(viewsets.ModelViewSet):
      filter_backends = [OrmFilter,]

      # 设置需要匹配的查询参数
      orm_fields = [
          # 基本的 and 查询   
          # date_joined__lt=2021-12-09&date_joined__gt=2021-12-1
          FQ(r'date_joined__(lt|gt)$'),

          # 获取查询参数数组
          # date_joined__range=2021-12-10&date_joined__range=2021-12-12'
          FQ(r'date_joined__range$', many=True),

          # 对查询的key和value进行转换
          # ids=[1,2,10]
          FQ(r'ids$', fv=json.loads, error_text='ids 必须是json数组', repl='id__in'),

          # 正则表达式查询
          # email__regex=gmail.com$
          FQ(r'email__regex$'),

          # or 查询
          # is_staff=false&email__iendswith=qq.com
          # filter( Q(is_staff=False) | Q(email__iendswith=qq.com) )
          FQ(r'email__iendswith$', cond='or'),
          FQ(r'is_staff$', json.loads, cond='or'),

          # not 查询
          # email__not=ajanuw@qq.com
          # ~Q(email='ajanuw@qq.com')
          FQ(r"email__not$", is_not=True, repl='email')
      ]
    ```
    """

    def filter_queryset(self, request: Request, queryset, view):
        """作为过滤器后端必须实现的钩子"""
        orm_fields: list[FQ] = getattr(view, "orm_fields", None)

        if orm_fields is None or not isinstance(orm_fields, (list, tuple)):
            return queryset

        filter_queryset = self.get_filter_queryset(
            request.query_params, orm_fields)

        if not filter_queryset:
            return queryset

        return queryset.filter(filter_queryset)

    def get_filter_queryset(self, query_params: QueryDict, orm_fields: list[FQ]):
        """从查询参数中获取过滤参数"""
        filter_queryset = None

        # 遍历请求中的查询参数
        for query_key in query_params:
            field = self.get_orm_field(query_params, query_key, orm_fields)

            if field is None:
                continue

            q = field.get_Q()

            filter_queryset = q if not filter_queryset else (
                filter_queryset & q if field.is_and else filter_queryset | q
            )

        return filter_queryset

    def get_orm_field(self, query_params: QueryDict, query_key: str, orm_fields: list[FQ]) -> FQ | None:
        """在orm_fields中匹配查询参数"""
        for field in orm_fields:
            if field.match(query_key):
                query_value = query_params.getlist(
                    query_key) if field.many else query_params.get(query_key)
                try:
                    query_value = field.format(query_value)

                    # 跳过值为None的查询，如果要查询null字段，使用 __isnull 过滤器
                    if query_value is None:
                        return None

                except Exception as e:
                    raise exceptions.ParseError(field.error_text or str(e))
                else:
                    field._filter_key = field.replace(query_key)
                    field._filter_value = query_value
                    return field

        return None
