# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['qlient', 'qlient.schema']

package_data = \
{'': ['*']}

install_requires = \
['requests>=2.27.1,<3.0.0']

setup_kwargs = {
    'name': 'qlient',
    'version': '0.0.1a1',
    'description': 'A fast and modern graphql client designed with simplicity in mind.',
    'long_description': '# Qlient: Python GraphQL Client\n\n[![qlient-org](https://circleci.com/gh/qlient-org/python-qlient.svg?style=svg)](https://circleci.com/gh/qlient-org/python-qlient)\n[![pypi](https://img.shields.io/pypi/v/python-qlient.svg)](https://pypi.python.org/pypi/python-qlient)\n[![versions](https://img.shields.io/pypi/pyversions/python-qlient.svg)](https://github.com/qlient-org/python-qlient)\n[![license](https://img.shields.io/github/license/qlient-org/python-qlient.svg)](https://github.com/qlient-org/python-qlient/blob/master/LICENSE)\n\nA fast and modern graphql client designed with simplicity in mind.\n\n## Help\n\nSee [documentation](https://qlient-org.github.io/python-qlient/) for more details\n\n## Installation\n\n```shell script\npip install qlient\n```\n\n## Quick Start\n\n````python\nfrom qlient import Client\n\nclient = Client("https://api.spacex.land/graphql/")\n\nres = client.query.launchesPast(\n    # spacex graphql input fields\n    find={"mission_name": "Starlink"},\n    limit=5,\n    sort="mission_name",\n\n    # qlient specific\n    _fields=["mission_name", "launch_success", "launch_year"]\n)\n````\n\nwhich sends the following query\n\n```gql\nquery launchesPast($find: LaunchFind, $limit: Int, $sort: String) {\n  launchesPast(find: $find, limit: $limit, sort: $sort) {\n    mission_name\n    launch_success\n    launch_year\n  }\n}\n```\n\nto the server and return this body:\n\n````json\n{\n  "data": {\n    "launchesPast": [\n      {\n        "mission_name": "Paz / Starlink Demo",\n        "launch_success": true,\n        "launch_year": "2018"\n      },\n      {\n        "mission_name": "Starlink 1",\n        "launch_success": true,\n        "launch_year": "2019"\n      },\n      {\n        "mission_name": "Starlink 2",\n        "launch_success": true,\n        "launch_year": "2020"\n      },\n      {\n        "mission_name": "Starlink 3",\n        "launch_success": true,\n        "launch_year": "2020"\n      },\n      {\n        "mission_name": "Starlink 4",\n        "launch_success": true,\n        "launch_year": "2020"\n      }\n    ]\n  }\n}\n````',
    'author': 'Daniel Seifert',
    'author_email': 'info@danielseifert.ch',
    'maintainer': 'Daniel Seifert',
    'maintainer_email': 'info@danielseifert.ch',
    'url': 'https://qlient-org.github.io/python-qlient/',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.6,<4.0',
}


setup(**setup_kwargs)
