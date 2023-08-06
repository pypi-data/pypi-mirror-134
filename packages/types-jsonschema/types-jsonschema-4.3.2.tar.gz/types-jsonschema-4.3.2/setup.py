from setuptools import setup

name = "types-jsonschema"
description = "Typing stubs for jsonschema"
long_description = '''
## Typing stubs for jsonschema

This is a PEP 561 type stub package for the `jsonschema` package.
It can be used by type-checking tools like mypy, PyCharm, pytype etc. to check code
that uses `jsonschema`. The source for this package can be found at
https://github.com/python/typeshed/tree/master/stubs/jsonschema. All fixes for
types and metadata should be contributed there.

See https://github.com/python/typeshed/blob/master/README.md for more details.
This package was generated from typeshed commit `85318d1b215a32825fd4ecb7fa6466fe75f7c428`.
'''.lstrip()

setup(name=name,
      version="4.3.2",
      description=description,
      long_description=long_description,
      long_description_content_type="text/markdown",
      url="https://github.com/python/typeshed",
      install_requires=[],
      packages=['jsonschema-stubs'],
      package_data={'jsonschema-stubs': ['__init__.pyi', '_format.pyi', '_legacy_validators.pyi', '_reflect.pyi', '_types.pyi', '_utils.pyi', '_validators.pyi', 'cli.pyi', 'exceptions.pyi', 'protocols.pyi', 'validators.pyi', 'METADATA.toml']},
      license="Apache-2.0 license",
      classifiers=[
          "License :: OSI Approved :: Apache Software License",
          "Typing :: Stubs Only",
      ]
)
