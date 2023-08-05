from setuptools import setup

name = "types-playsound"
description = "Typing stubs for playsound"
long_description = '''
## Typing stubs for playsound

This is a PEP 561 type stub package for the `playsound` package.
It can be used by type-checking tools like mypy, PyCharm, pytype etc. to check code
that uses `playsound`. The source for this package can be found at
https://github.com/python/typeshed/tree/master/stubs/playsound. All fixes for
types and metadata should be contributed there.

See https://github.com/python/typeshed/blob/master/README.md for more details.
This package was generated from typeshed commit `7191d12e243d66fc349f3f5a42e9dee4256aca21`.
'''.lstrip()

setup(name=name,
      version="1.3.0",
      description=description,
      long_description=long_description,
      long_description_content_type="text/markdown",
      url="https://github.com/python/typeshed",
      install_requires=[],
      packages=['playsound-stubs'],
      package_data={'playsound-stubs': ['__init__.pyi', 'METADATA.toml']},
      license="Apache-2.0 license",
      classifiers=[
          "License :: OSI Approved :: Apache Software License",
          "Typing :: Stubs Only",
      ]
)
