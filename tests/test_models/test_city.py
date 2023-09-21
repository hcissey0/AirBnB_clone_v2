#!/usr/bin/python3
""" """
from tests.test_models.test_base_model import test_basemodel
from models.base_model import BaseModel
from models.city import City
from os import getenv
import unittest


class test_City(test_basemodel):
    """ """

    def __init__(self, *args, **kwargs):
        """ """
        super().__init__(*args, **kwargs)
        self.name = "City"
        self.value = City

    def test_attrs(self):
        new = self.value()
        self.assertTrue(hasattr(new, "name"))
        self.assertTrue(hasattr(new, "state_id"))

    def test_subclass(self):
        """_summary_
        """
        self.assertTrue(issubclass(City, BaseModel))
