# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

modules = \
['c3voc', 'epgdb']
install_requires = \
['requests>=2,<3']

entry_points = \
{'console_scripts': ['c3vocupdate = c3voc:update_streams_v2']}

setup_kwargs = {
    'name': 'e2voc',
    'version': '0.1.1',
    'description': '',
    'long_description': None,
    'author': 'Andreas Oberritter',
    'author_email': 'obi@saftware.de',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/mtdcr/e2voc',
    'package_dir': package_dir,
    'py_modules': modules,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=2.7, !=3.0.*, !=3.1.*, !=3.2.*, !=3.3.*, !=3.4.*, !=3.5.*',
}


setup(**setup_kwargs)
