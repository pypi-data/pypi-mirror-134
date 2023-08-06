# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['studenttask', 'studenttask.studenttask', 'studenttask.tests']

package_data = \
{'': ['*']}

install_requires = \
['pendulum>=2.1.2,<3.0.0']

setup_kwargs = {
    'name': 'studenttask',
    'version': '0.1.0',
    'description': 'Data Challenge',
    'long_description': None,
    'author': 'Takehiro Tsurumi',
    'author_email': 'cranelook87@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
