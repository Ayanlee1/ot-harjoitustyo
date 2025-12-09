import os
import sqlite3
import sys


def get_database_connection():
    """Palauttaa tietokantayhteyden."""
    dirname = os.path.dirname(__file__)

    if os.getenv("TESTING") == "true" or "pytest" in sys.modules:
        database_name = "test.db"
    else:
        database_name = "weather.db"

    database_path = os.path.join(dirname, "..", "data", database_name)

    os.makedirs(os.path.dirname(database_path), exist_ok=True)

    connection = sqlite3.connect(database_path)
    connection.row_factory = sqlite3.Row

    return connection
