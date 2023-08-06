# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['sword_to_json']

package_data = \
{'': ['*']}

install_requires = \
['pysword>=0.2.7,<0.3.0']

setup_kwargs = {
    'name': 'sword-to-json',
    'version': '1.4.2',
    'description': 'Generate JSON Files of Bible Translations from SWORD Modules',
    'long_description': '![CI Workflow](https://github.com/evnskc/sword-to-json/actions/workflows/ci.yml/badge.svg)\n\n![STAGING Workflow](https://github.com/evnskc/sword-to-json/actions/workflows/staging.yml/badge.svg)\n\n![PRODUCTION Workflow](https://github.com/evnskc/sword-to-json/actions/workflows/production.yml/badge.svg)\n\n## Generate JSON Files of Bible Translations from SWORD Modules\n\nThe [SWORD project provides modules](http://crosswire.org/sword/modules/ModDisp.jsp?modType=Bibles) freely for common\nBible translations in different languages.\n\nSample JSON format.\n\n```\n{\n  "name": "King James Version",\n  "abbreviation": "KJV",\n  "books": [\n    {\n      "number": 1,\n      "name": "Genesis",\n      "abbreviation": "Gen",\n      "chapters": [\n        {\n          "number": 1,\n          "verses": [\n            {\n              "number": 1,\n              "text": "In the beginning God created the heavens and the earth. "\n            },\n            \n            ...\n          ]\n        },\n        \n        ...\n      ]\n    }\n  ]\n}\n\n```',
    'author': 'evnskc',
    'author_email': 'evans@fundi.dev',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/evnskc/sword-to-json',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
