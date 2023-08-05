# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['deep_sorted']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'deep-sorted',
    'version': '0.0.2',
    'description': 'Sorting of nested dicts and lists',
    'long_description': '# deep-sorted\n\n![Testing and linting](https://github.com/danhje/deep-sorted/workflows/Test%20And%20Lint/badge.svg)\n[![codecov](https://codecov.io/gh/danhje/deep-sorted/branch/master/graph/badge.svg)](https://codecov.io/gh/danhje/deep-sorted)\n![GitHub release (latest by date including pre-releases)](https://img.shields.io/github/v/release/danhje/deep-sorted?include_prereleases)\n![PyPI](https://img.shields.io/pypi/v/deep-sorted)\n\n## Motivation\n\nWhen validating parsed JSON objects, schemas and other nested data structures in unit tests, order\nis typically not important. And yet I often find myself manually sorting the target structures\nwhen the internals of the tested function is modified such that order is changed. With this package,\nboth the target and the actual structure can be recursively sorted before comparison.\n\n## Installation\n\nUsing poetry:\n\n```shell\npoetry add deep-sorted\n```\n\nUsing pipenv:\n\n```shell\npipenv install deep-sorted\n```\n\nUsing pip:\n\n```shell\npip install deep-sorted\n```\n\n## Usage\n\n```python\nfrom deep_sorted import deep_sorted\nfrom datetime import datetime\n\none = {\n    "id": 9,\n    "name": "Ted Chiang",\n    "books": [\n        {\n            "id": 124,\n            "published": datetime(1991, 8, 1, 0, 0),\n            "title": "Understand",\n            "ratings": (6, 6, 3, 5, 6, 6, 0, 6, 0),\n        },\n        {\n            "id": 125,\n            "published": datetime(2019, 5, 7, 0, 0),\n            "title": "Exhalation",\n        },\n    ],\n}\n\ntwo = {\n    "books": [\n        {\n            "published": datetime(2019, 5, 7, 0, 0),\n            "title": "Exhalation",\n            "id": 125,\n        },\n        {\n            "ratings": (3, 0, 0, 6, 6, 6, 6, 5, 6),\n            "id": 124,\n            "published": datetime(1991, 8, 1, 0, 0),\n            "title": "Understand",\n        },\n    ],\n    "id": 9,\n    "name": "Ted Chiang",\n}\n\nassert deep_sorted(one) == deep_sorted(two)\n```\n',
    'author': 'Daniel Hjertholm',
    'author_email': 'daniel.hjertholm@icloud.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/danhje/deep-sorted',
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.7,<=3.10',
}


setup(**setup_kwargs)
