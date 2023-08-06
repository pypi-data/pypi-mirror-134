from setuptools import setup

name = "types-tzlocal"
description = "Typing stubs for tzlocal"
long_description = '''
## Typing stubs for tzlocal

This is a PEP 561 type stub package for the `tzlocal` package.
It can be used by type-checking tools like mypy, PyCharm, pytype etc. to check code
that uses `tzlocal`. The source for this package can be found at
https://github.com/python/typeshed/tree/master/stubs/tzlocal. All fixes for
types and metadata should be contributed there.

See https://github.com/python/typeshed/blob/master/README.md for more details.
This package was generated from typeshed commit `7920f502e2e9fd072b450d343a5d11018f674ec9`.
'''.lstrip()

setup(name=name,
      version="4.1.0",
      description=description,
      long_description=long_description,
      long_description_content_type="text/markdown",
      url="https://github.com/python/typeshed",
      install_requires=['types-pytz'],
      packages=['tzlocal-stubs'],
      package_data={'tzlocal-stubs': ['__init__.pyi', 'METADATA.toml']},
      license="Apache-2.0 license",
      classifiers=[
          "License :: OSI Approved :: Apache Software License",
          "Typing :: Stubs Only",
      ]
)
