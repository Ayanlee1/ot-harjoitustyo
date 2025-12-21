import os
import sqlite3
import sys


def get_database_connection():
    """Palauttaa tietokantayhteyden. Testitilassa käytetään test.db-tiedostoa, muuten weather.db.

    Returns:
        sqlite3.Connection: Tietokantayhteys SQLite-tietokantaan."""
    dirname = os.path.dirname(__file__)

    if "pytest" in sys.modules:
        database_name = "test.db"
    else:
        database_name = "weather.db"

    database_path = os.path.join(dirname, "..", "data", database_name)

    os.makedirs(os.path.dirname(database_path), exist_ok=True)

    connection = sqlite3.connect(database_path)
    connection.row_factory = sqlite3.Row

    return connection
