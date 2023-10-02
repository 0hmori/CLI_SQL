import os

import datetime
import logging
from playhouse.db_url import connect
from dotenv import load_dotenv

from peewee import Model, IntegerField, CharField, TextField, TimestampField


load_dotenv()  # .envの読み込み

# データベースへの接続設定
# db = SqliteDatabase("peewee_db.sqlite")  # SQLite固定の場合
db = connect(os.environ.get("DATABASE"))  # 環境変数に合わせて変更する場合
# db = connect(os.environ.get("DATABASE") or "sqlite:///peewee_db.sqlite")  # 環境変数が無い場合にデフォルト値として値を設定することも可能

# 接続NGの場合はメッセージを表示
if not db.connect():
    print("接続NG")
    exit()


class User(Model):
    """User Model"""

    id = IntegerField(primary_key=True)  # idは自動で追加されるが明示
    name = CharField()
    age = IntegerField()

    class Meta:
        database = db
        table_name = "user"


db.create_tables([User])
