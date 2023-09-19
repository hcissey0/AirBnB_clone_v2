#!/usr/bin/python3
""" """
from tests.test_models.test_base_model import test_basemodel
from models.base_model import BaseModel
from models.state import State


class test_state(test_basemodel):
    """ """

    def __init__(self, *args, **kwargs):
        """ """
        super().__init__(*args, **kwargs)
        self.name = "State"
        self.value = State

    def test_subclass(self):
        """_summary_
        """
        self.assertTrue(issubclass(State, BaseModel))

    def test_name3(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.name), str)
