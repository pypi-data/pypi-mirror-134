# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['tuat_feed']

package_data = \
{'': ['*']}

install_requires = \
['requests>=2.26.0,<3.0.0']

setup_kwargs = {
    'name': 'tuat-feed',
    'version': '0.2.3',
    'description': 'Unofficial library for fetching the feed for TUAT',
    'long_description': '# (非公式)TUAT掲示板ライブラリ\n\n[![test](https://github.com/pineapplehunter/tuat-feed/actions/workflows/test.yml/badge.svg)](https://github.com/pineapplehunter/tuat-feed/actions/workflows/test.yml) [![doc](https://api.netlify.com/api/v1/badges/77818cbd-dd98-4969-ab2d-2d4c6800434f/deploy-status)](https://app.netlify.com/sites/tuat-feed-doc/deploys) [![PyPI version](https://badge.fury.io/py/tuat-feed.svg)](https://badge.fury.io/py/tuat-feed)\n\n## ドキュメント\nhttps://tuat-feed-doc.netlify.app/tuat_feed.html\n\n## インストール\n* `python` >= 3.7\n\n```sh\n$ pip install tuat-feed\n```\n\n## 使い方\n\n```python\n>>> import tuat_feed\n>>> feed = tuat_feed.fetch_technology() # 工学部掲示板情報の取得\n# >>> feed = tuat_feed.fetch_agriculture() # 農学部掲示板情報の取得\n>>> len(feed)\n40\n>>> feed[0]\nPost(...)\n```\n',
    'author': 'Shogo Takata',
    'author_email': 's196643z@st.go.tuat.ac.jp',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/pineapplehunter/tuat-feed',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
