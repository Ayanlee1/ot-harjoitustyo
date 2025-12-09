import sqlite3
from database_connection import get_database_connection


class LocationRepository:
    def __init__(self, connection=None):
        self._connection = connection or get_database_connection()

    def find_all(self):
        cursor = self._connection.cursor()
        cursor.execute("SELECT name FROM locations")
        rows = cursor.fetchall()
        return [row["name"] for row in rows]

    def create(self, location):
        cursor = self._connection.cursor()

        cursor.execute(
            "SELECT name FROM locations WHERE LOWER(name) = LOWER(?)", (location,))
        existing = cursor.fetchone()

        if existing:
            return False

        try:
            cursor.execute(
                "INSERT INTO locations (name) VALUES (?)", (location,))
            self._connection.commit()
            return True
        except sqlite3.IntegrityError:
            return False

    def delete(self, location):
        cursor = self._connection.cursor()
        cursor.execute(
            "DELETE FROM locations WHERE LOWER(name) = LOWER(?)", (location,))
        self._connection.commit()
        return cursor.rowcount > 0

    def delete_all(self):
        cursor = self._connection.cursor()
        cursor.execute("DELETE FROM locations")
        self._connection.commit()
