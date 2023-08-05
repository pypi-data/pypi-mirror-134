# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

modules = \
['enigma']
install_requires = \
['requests>=2,<3', 'six']

setup_kwargs = {
    'name': 'fakenigma',
    'version': '0.1.0',
    'description': '',
    'long_description': None,
    'author': 'Andreas Oberritter',
    'author_email': 'obi@saftware.de',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/mtdcr/fakenigma',
    'package_dir': package_dir,
    'py_modules': modules,
    'install_requires': install_requires,
    'python_requires': '>=2.7, !=3.0.*, !=3.1.*, !=3.2.*, !=3.3.*, !=3.4.*, !=3.5.*',
}


setup(**setup_kwargs)
