# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['coltrane',
 'coltrane.config',
 'coltrane.management',
 'coltrane.management.commands']

package_data = \
{'': ['*'], 'coltrane': ['templates/coltrane/*']}

install_requires = \
['Django>3.0',
 'click>=8.0.0,<9.0.0',
 'markdown2>=2.4.2,<3.0.0',
 'python-dotenv>0.17']

extras_require = \
{'docs': ['Sphinx>=4.3.2,<5.0.0',
          'linkify-it-py>=1.0.3,<2.0.0',
          'myst-parser>=0.16.1,<0.17.0',
          'furo>=2021.11.23,<2022.0.0',
          'sphinx-copybutton>=0.4.0,<0.5.0',
          'sphinx-autobuild>=2021.3.14,<2022.0.0'],
 'gunicorn': ['gunicorn>=20.1.0,<21.0.0']}

entry_points = \
{'console_scripts': ['coltrane = coltrane.console:cli']}

setup_kwargs = {
    'name': 'coltrane-web',
    'version': '0.7.0',
    'description': 'A simple content site framework that harnesses the power of Django without the hassle.',
    'long_description': '# coltrane\n\nA simple content site framework that harnesses the power of Django without the hassle.\n\n## Features\n\n- Can either generate a static HTML, be used as a standalone Django site, or integrated into an existing Django site\n- Can use data from JSON files in templates and content\n- All the power of Django templates, template tags, and filters\n- Renders markdown files automatically (for a dynamic site)\n- Can include other Django apps\n\n## Documentation\n\nhttps://coltrane.readthedocs.io\n',
    'author': 'adamghill',
    'author_email': 'adam@adamghill.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/adamghill/coltrane/',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'extras_require': extras_require,
    'entry_points': entry_points,
    'python_requires': '>3.6.2,<4.0',
}


setup(**setup_kwargs)
