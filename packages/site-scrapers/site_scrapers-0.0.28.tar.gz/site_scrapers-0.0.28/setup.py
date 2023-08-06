# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['site_scrapers',
 'site_scrapers.models',
 'site_scrapers.scrapers',
 'site_scrapers.scrapers.details',
 'site_scrapers.scrapers.list',
 'site_scrapers.tests',
 'site_scrapers.tests.scrapers',
 'site_scrapers.tests.scrapers.details',
 'site_scrapers.utils']

package_data = \
{'': ['*'],
 'site_scrapers.tests.scrapers.details': ['brc_data/*',
                                          'inchcape/*',
                                          'moller_data/*']}

install_requires = \
['gazpacho>=1.1,<2.0',
 'httpx>=0.21.3,<0.22.0',
 'requests>=2.27.1,<3.0.0',
 'returns>=0.18.0,<0.19.0']

setup_kwargs = {
    'name': 'site-scrapers',
    'version': '0.0.28',
    'description': '',
    'long_description': None,
    'author': 'Dmitrijs Balcers,',
    'author_email': 'dmitrijs.balcers@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
