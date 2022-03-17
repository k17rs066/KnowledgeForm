# django_knowledge_form

- プロジェクト作成時のディレクトリ構成図
```
% django-admin startproject knowledge_form

.
┣  knowledge_form
┃   ┠─ __init__.py
┃   ┠─ asgi.py
┃   ┠─ settings.py
┃   ┠─ urls.py
┃   ┗─ wsgi.py
┗━━━manage.py

```

- 各生成ファイルの役割
  - __init__.py：knowledg_form フォルダがPython のパッケージであることを表す。中身は空。
  - settings.py：Djangoプロジェクトのさまざまな設定を記述する。
  - manage.py：django-admin コマンドを使用する際のショートカットスクリプト。Djangoではこのスクリプトを用いて、開発サーバの立ち上げやテストを実行する。
  - urls.py：ルーティングに関する設定を記述する。
  - asgi.py,wsgi.py：非同期処理の実装などで使うファイル。

