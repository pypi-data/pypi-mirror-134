# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['impler']

package_data = \
{'': ['*']}

install_requires = \
['asyncio>=3.4,<4.0']

setup_kwargs = {
    'name': 'impler',
    'version': '0.1.0',
    'description': '',
    'long_description': '## Implementation pattern*\n\n/* *inspired by Rust*\n\nUseful when it is needed to extend a class (usually 3d party) with some methods\nor interfaces\n\n### Install\n\n```shell\npip install impler\n```\n\nor\n\n```shell\npoetry add impler\n```\n\n### Usage\n\n#### Methods implementation\n\nUsing implementation pattern you can extend any class (even 3rd party) with\nregular, class or static methods.\n\n```python\nfrom impler import impl\nfrom pydantic import BaseModel\n\n\n@impl(BaseModel)\ndef fields_count(self: BaseModel):\n    return len(self.__fields__)\n\n\nclass Point(BaseModel):\n    x: int = 0\n    y: int = 1\n\n\npoint = Point()\nprint(point.fields_count())\n```\n\nClass methods\n\n```python\n@impl_classmethod(BaseModel)\ndef fields_count(cls):\n    return len(cls.__fields__)\n\n\n# or\n\n@impl(BaseModel)\n@classmethod\ndef fields_count(cls):\n    return len(cls.__fields__)\n```\n\nStatic methods\n\n```python\n@impl_staticmethod(BaseModel)\ndef zero(cls):\n    return 0\n\n\n# or\n\n@impl(BaseModel)\n@staticmethod\ndef zero(cls):\n    return 0\n```\n\nAsync methods\n\n```python\n@impl(BaseModel)\nasync def zero(cls):\n    await asyncio.sleep(1)\n    return 0\n```\n\n#### Interfaces implementation\n\nThe same way you can extend any class with the whole interface\n\nHere is example of the base interface, which\n\n```python\nfrom pathlib import Path\n\n\nclass BaseFileInterfase:\n    def dump(self, path: Path):\n        ...\n\n    @classmethod\n    def parse(cls, path: Path):\n        ...\n```\n\nThis is how you can implement this interface for Pydantic `BaseModel` class:\n\n```python\nfrom impler import impl\nfrom pydantic import BaseModel\nfrom pathlib import Path\n\n\n@impl(BaseModel, as_parent=True)\nclass ModelFileInterface(BaseFileInterface):\n    def dump(self, path: Path):\n        path.write_text(self.json())\n        \n    @classmethod\n    def parse(cls, path: Path):\n        return cls.parse_file(path)\n\n```\n\nIf `as_parent` parameter is `True` the implementation will be injected to the list of the target class parents.\n\nThen you can check if the class or object implements the interface:\n\n```python\nprint(issubclass(BaseModel, BaseFileInterfase))\n# True\n\nprint(issubclass(Point, BaseFileInterfase))\n# True\n\nprint(isinstance(point, BaseFileInterface))\n# True\n```\n\nThe whole api documentation could be found by the [link](https://github.com/roman-right/impler/docs/api.md)',
    'author': 'Roman',
    'author_email': 'roman-right@protonmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/roman-right/impler',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
