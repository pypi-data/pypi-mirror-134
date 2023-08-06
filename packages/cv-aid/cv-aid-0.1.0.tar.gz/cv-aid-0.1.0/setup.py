# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['cv_aid', 'tests']

package_data = \
{'': ['*']}

modules = \
['scripts']
install_requires = \
['deepstack-sdk>=0.2.1,<0.3.0', 'filetype>=1.0.9,<2.0.0']

entry_points = \
{'console_scripts': ['test = scripts:test']}

setup_kwargs = {
    'name': 'cv-aid',
    'version': '0.1.0',
    'description': 'CV Aid is a set of helpers of computer vision tasks.',
    'long_description': None,
    'author': 'Khalid Mohamed Elborai',
    'author_email': 'accnew820@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'py_modules': modules,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
