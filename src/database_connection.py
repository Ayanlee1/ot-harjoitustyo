import os
import sqlite3
from dotenv import load_dotenv

dirname = os.path.dirname(__file__)

try:
    load_dotenv(dotenv_path=os.path.join(dirname, "..", ".env"))
except FileNotFoundError:
    pass

database_url = os.getenv("DATABASE_URL") or "weather.db"
database_path = os.path.join(dirname, "..", "data", database_url)


os.makedirs(os.path.dirname(database_path), exist_ok=True)

connection = sqlite3.connect(database_path)
connection.row_factory = sqlite3.Row


def get_database_connection():
    return connection
