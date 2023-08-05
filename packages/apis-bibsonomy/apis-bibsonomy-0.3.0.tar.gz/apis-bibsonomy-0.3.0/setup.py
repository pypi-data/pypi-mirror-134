# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['apis_bibsonomy', 'apis_bibsonomy.migrations', 'apis_bibsonomy.templatetags']

package_data = \
{'': ['*'],
 'apis_bibsonomy': ['static/apis_bibsonomy/css/*',
                    'static/apis_bibsonomy/js/*',
                    'templates/apis_bibsonomy/*']}

install_requires = \
['apis-core>=0.16.0']

setup_kwargs = {
    'name': 'apis-bibsonomy',
    'version': '0.3.0',
    'description': 'Bibsonomy/Zotero plugin for managing refernces in APIS framework',
    'long_description': None,
    'author': 'Matthias Schlögl',
    'author_email': 'm.schloegl@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.6,<3.9',
}


setup(**setup_kwargs)
