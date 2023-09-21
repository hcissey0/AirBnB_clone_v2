#!/usr/bin/python3
""" """
from tests.test_models.test_base_model import test_basemodel
from models.base_model import BaseModel
from models.user import User
from os import getenv
import pep8


class test_User(test_basemodel):
    """ """

    def __init__(self, *args, **kwargs):
        """ """
        super().__init__(*args, **kwargs)
        self.name = "User"
        self.value = User
        self.use = User()

    def test_pep8_User(self):
        """Tests pep8 style"""
        style = pep8.StyleGuide(quiet=True)
        p = style.check_files(['models/user.py'])
        self.assertEqual(p.total_errors, 0, "fix wergpep8")

    

    def test_attributeer(self):
        """chekcing if User have attributes"""
        self.assertTrue(hasattr(self.use, 'email'))
        self.assertTrue('id' in self.use.__dict__)
        self.assertTrue('created_at' in self.use.__dict__)
        self.assertTrue('updated_at' in self.use.__dict__)
        self.assertTrue(hasattr(self.use, "password"))
        self.assertTrue(hasattr(self.use, "first_name"))
        self.assertTrue(hasattr(self.use, "last_name"))

    def test_subclass(self):
        """ """
        self.assertTrue(issubclass(User, BaseModel))

    def test_checking_docstring_User(self):
        """checking for docstrings"""
        self.assertIsNotNone(User.__doc__)
