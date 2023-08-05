# (非公式)TUAT掲示板ライブラリ

[![test](https://github.com/pineapplehunter/tuat-feed/actions/workflows/test.yml/badge.svg)](https://github.com/pineapplehunter/tuat-feed/actions/workflows/test.yml) [![doc](https://api.netlify.com/api/v1/badges/77818cbd-dd98-4969-ab2d-2d4c6800434f/deploy-status)](https://app.netlify.com/sites/tuat-feed-doc/deploys) [![PyPI version](https://badge.fury.io/py/tuat-feed.svg)](https://badge.fury.io/py/tuat-feed)

## ドキュメント
https://tuat-feed-doc.netlify.app/tuat_feed.html

## インストール
* `python` >= 3.7

```sh
$ pip install tuat-feed
```

## 使い方

```python
>>> import tuat_feed
>>> feed = tuat_feed.fetch_technology() # 工学部掲示板情報の取得
# >>> feed = tuat_feed.fetch_agriculture() # 農学部掲示板情報の取得
>>> len(feed)
40
>>> feed[0]
Post(...)
```
