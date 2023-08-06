# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['struct_model']

package_data = \
{'': ['*']}

install_requires = \
['ujson>=5.1.0,<6.0.0']

setup_kwargs = {
    'name': 'struct-model-python',
    'version': '0.1.1',
    'description': 'Struct to model (dataclass) for python',
    'long_description': '# Welcome\n\n## Struct-Model\n\nStruct-Model is an annotations based wrapper for python\'s built-in `Struct` module.\n\n```python example.py\nfrom struct_model import StructModel, String, uInt4\n\nclass Form(StructModel):\n    username: String(16)\n    balance: uInt4\n    \nprint(Form("Adam Bright", 12).pack())\n# b\'Adam Bright\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x0c\'\nprint(Form.unpack(b\'Adam Bright\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x0c\').json())\n# {"username": "Adam Bright", "balance": 12}\n```\n\n## Installation\n\n### Poetry\n\n```shell\npoetry add struct-model-python\n```\n\n### PIP\n\n```shell\npip install struct-model-python\n```\n\n## Requirements\n\n+ [`ujson >= 4.1.0`](https://github.com/ultrajson/ultrajson)',
    'author': 'Bogdan Parfenov',
    'author_email': 'adam.brian.bright@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://adambrianbright.github.io/struct-model-python/',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.10.0rc1,<4.0',
}


setup(**setup_kwargs)
