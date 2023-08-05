## django-orm-filter

django drf query filter

## Install
```sh
pip install django-orm-filter
```

## Use
```python
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