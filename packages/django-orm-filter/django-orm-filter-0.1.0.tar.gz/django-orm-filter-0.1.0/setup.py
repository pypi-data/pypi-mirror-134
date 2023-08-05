import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="django-orm-filter",
    version="0.1.0",
    author="Ajanuw",
    author_email="ajanuw1995@gmail.com",
    description="django drf query filter",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/januwA/django-orm-filter",
    project_urls={
        "Bug Tracker": "https://github.com/januwA/django-orm-filter/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    # packages=setuptools.find_packages(where="src"),
    packages=setuptools.find_packages(exclude=['tests*']),
    install_requires=["django", "djangorestframework"],
    python_requires=">=3.6",
)
