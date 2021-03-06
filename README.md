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
┗━━━ manage.py

```

- 各生成ファイルの役割
  - __init__.py：knowledg_form フォルダがPython のパッケージであることを表す。中身は空。
  - settings.py：Djangoプロジェクトのさまざまな設定を記述する。
  - manage.py：django-admin コマンドを使用する際のショートカットスクリプト。Djangoではこのスクリプトを用いて、開発サーバの立ち上げやテストを実行する。
  - urls.py：ルーティングに関する設定を記述する。
  - asgi.py,wsgi.py：非同期処理の実装などで使うファイル。

- 開発用サーバの立ち上げ
  - python3 manage.py runserver
  - localhost:8000 にアクセス
  - この画面に遷移したら立ち上げ成功！


'''

Watching for file changes with StatReloader
Performing system checks...

System check identified no issues (0 silenced).

You have 18 unapplied migration(s). Your project may not work properly until you apply the migrations for app(s): admin, auth, contenttypes, sessions.
Run 'python manage.py migrate' to apply them.
March 18, 2022 - 01:23:25
Django version 4.0.2, using settings 'knowledge_form.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CONTROL-C.

'''

- 言語設定、タイムゾーンの変更
  - setteings.py
'''
LANGUAGE_CODE = 'ja'    # デフォルト：'en-us'
TIME_ZONE = 'Asia/Tokyo' # デフォルト：'UTC
''''

- データベースをセットアップ
  - settings.py のデータベースに関する記述を確認
  - django ではデフォルトで sqlite3が設定されている

'''
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
'''

  - テーブルの作成・修正
    - マイグレーションという機能を活用
    - テーブルの作成
      - ```% python3 manage.py migrate ```

- Django アプリケーションを作成
  - python3 manage.py startapp knowledge_base
  - 作成されたディレクトリは以下のようになる

```
% python3 manage.py startapp knowledge_base
.
┣  knowledge_form
┃   ┠─ (略)
┣━━━ manage.py
┗━━━ knowledge_base
        ┠─ __init__.py
        ┠─ admin.py
        ┠─ apps.py
        ┠─ migrations/
        ┠─ models.py
        ┠─ tests.py
        ┗─ views.py

```
    - admin.py：管理画面の設定を記述
    - apps.py：アプリケーションの様々な状態にフックする処理を記述
    - migrations/：マイグレーションファイルが生成
    - models.py：データベーススキーマの定義
    - tests.py：テストを記述
    - views.py ：ビューを記述

- path():
  - 第一引数：HTTPリクエストのパスを指定
  - 第二引数：ビュー関数を指定
  - nameキーワード引数：URLの逆引き