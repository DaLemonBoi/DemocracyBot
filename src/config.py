import os

BOT_TOKEN = os.environ.get("BOT_TOKEN")

DB_USER = os.environ.get("DB_USER")
DB_PASSWORD = os.environ.get("DB_PASSWORD")
DB_DEFAULT_DATABASE = os.environ.get("DB_DEFAULT_DATABASE")
DB_HOST = os.environ.get("DB_HOST")
DB_PORT = int(os.environ.get("DB_PORT"))

OWNERS = list(map(int, os.environ['OWNERS'].split(';')))
