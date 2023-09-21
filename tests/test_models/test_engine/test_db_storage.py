#!/usr/bin/python3
"""test for file storage"""
import unittest
import pep8
import json
import os
from os import getenv
import MySQLdb
from models.base_model import BaseModel, Base
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models.engine.db_storage import DBStorage


@unittest.skipIf(getenv("HBNB_TYPE_STORAGE") != 'db', 'DATABASE')
class TestDBStorage(unittest.TestCase):
    '''this will teste DBStorage'''

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        """set up for test"""
        self.User = getenv("HBNB_MYSQL_USER")
        self.Passwd = getenv("HBNB_MYSQL_PWD")
        self.Db = getenv("HBNB_MYSQL_DB")
        self.Host = getenv("HBNB_MYSQL_HOST")
        self.db = MySQLdb.connect(host=self.Host, user=self.User,
                                  passwd=self.Passwd, db=self.Db,
                                  charset="utf8")
        self.query = self.db.cursor()
        self.storage = DBStorage()
        self.storage.reload()

    @classmethod
    def tearDown(self):
        """at the end of the test this wiear it down"""
        self.query.close()
        self.db.close()

    @unittest.skipIf(getenv("HBNB_TYPE_STORAGE") != 'db', 'DATABASE')
    def test_pepDBStorage(self):
        """Test Pep8"""
        style = pep8.StyleGuide(quiet=True)
        p = style.check_files(['models/engine/db_storage.py'])
        self.assertEqual(p.total_errors, 0, "fix pep8")

    @unittest.skipIf(getenv("HBNB_TYPE_STORAGE") != 'db', 'DATABASE')
    def test_r_tables(self):
        """existing tables"""
        self.query.execute("SHOW TABLES")
        salsa = self.query.fetchall()
        self.assertEqual(len(salsa), 7)

    @unittest.skipIf(getenv("HBNB_TYPE_STORAGE") != 'db', 'DATABASE')
    def test_noement_user(self):
        """no elem in users"""
        self.query.execute("SELECT * FROM users")
        salsa = self.query.fetchall()
        self.assertEqual(len(salsa), 0)

    @unittest.skipIf(getenv("HBNB_TYPE_STORAGE") != 'db', 'DATABASE')
    def test_no_elnt_cities(self):
        """no elem in cities"""
        self.query.execute("SELECT * FROM cities")
        salsa = self.query.fetchall()
        self.assertEqual(len(salsa), 0)

    @unittest.skipIf(getenv("HBNB_TYPE_STORAGE") != 'db', 'DATABASE')
    def test_ad(self):
        """Test same size between storage() and existing db"""
        self.query.execute("SELECT * FROM states")
        salsa = self.query.fetchall()
        self.assertEqual(len(salsa), 0)
        state = State(name="LUISILLO")
        state.save()
        self.db.autocommit(True)
        self.query.execute("SELECT * FROM states")
        salsa = self.query.fetchall()
        self.assertEqual(len(salsa), 1)


if __name__ == "__main__":
    unittest.main()
