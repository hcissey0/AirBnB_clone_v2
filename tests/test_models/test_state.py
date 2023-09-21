#!/usr/bin/python3
""" """
from tests.test_models.test_base_model import test_basemodel
from models.base_model import BaseModel
from models.state import State
from os import getenv
import unittest


class test_state(test_basemodel):
    """ """

    def __init__(self, *args, **kwargs):
        """ """
        super().__init__(*args, **kwargs)
        self.name = "State"
        self.value = State
        self.state = State()

    def test_subclass(self):
        """_summary_
        """
        self.assertTrue(issubclass(State, BaseModel))

    @unittest.skipIf(getenv("HBNB_TYPE_STORAGE") == "db", "Database")
    def test_name3(self):
        """ """
        new = self.value()
        self.assertTrue(hasattr(self.state, "name"))
