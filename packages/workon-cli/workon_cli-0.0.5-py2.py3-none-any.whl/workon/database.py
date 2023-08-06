"""Database hanlder for the workon project."""
import sqlite3
from pathlib import Path
from typing import Dict, NamedTuple, List

from workon import DB_READ_ERROR
from workon import DB_WRITE_ERROR
from workon import DB_DELETE_ERROR

class DBresponse(NamedTuple):
    """This class is to handle the response from the database"""
    error: int
    data: List[Dict[str, str]]

class Database:

    def __init__(self, dbfile: Path) -> None:

        self._dbfile = dbfile
        self.connection = sqlite3.connect(self._dbfile)
        self.cursor = self.connection.cursor()

        self.create_db()
    
    def create_db(self) -> None:
        """
        This function is to create the database file
        """

        self.cursor.execute("""CREATE TABLE IF NOT EXISTS projects (
            name text unique,
            path text unique,
            env text unique,
            python_version text
        )""")

        self.connection.commit()

    def get_projects(self) -> DBresponse:
        """This function is to get the projects from the database"""

        try:
            
            self.cursor.execute("SELECT name FROM projects")
            data = self.cursor.fetchall()

            return DBresponse(0, data)

        except sqlite3.Error as e:
            
            return DBresponse(DB_READ_ERROR, [])
    
    def call_project(self, name: str) -> DBresponse:
        """This function is to call a project to the database"""

        try:
            
            self.cursor.execute("SELECT name, path, env FROM projects WHERE name = ?", (name,))
            data = self.cursor.fetchone()
            return DBresponse(0, data)

        except sqlite3.Error as e:
            
            return DBresponse(DB_READ_ERROR, [])
    
    def add_project(self, path:str, env: str, python: str) -> DBresponse:
        """This function is to add a project to the database"""

        try:
            
            self.cursor.execute("INSERT INTO projects VALUES (?, ?, ?, ?)", (env, path, env, python))
            self.connection.commit()

            return DBresponse(0, [])

        except sqlite3.Error as e:
            
            return DBresponse(DB_WRITE_ERROR, [])
    
    def remove_project(self, name: str) -> DBresponse:
        """This function is to remove a project to the database"""

        try:
            
            self.cursor.execute("DELETE FROM projects WHERE name = ?", (name,))
            self.connection.commit()
            return DBresponse(0, [])

        except sqlite3.Error as e:
            
            return DBresponse(DB_DELETE_ERROR, [])