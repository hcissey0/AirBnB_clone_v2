#!/usr/bin/python3
""" """
from tests.test_models.test_base_model import test_basemodel
from models.amenity import Amenity
from models.base_model import BaseModel
import pep8
import unittest
from os import getenv


class test_Amenity(test_basemodel):
    """ """

    def __init__(self, *args, **kwargs):
        """ """
        super().__init__(*args, **kwargs)
        self.name = "Amenity"
        self.value = Amenity
        self.amen = Amenity()
        self.amen.name = "kofi"

    def test_pep8_amenity(self):
        """ """
        s = pep8.StyleGuide(quiet=True)
        p = s.check_files(['models/amenity.py'])
        self.assertEqual(p.total_errors, 0, "pep8 error")

    def test_attributes_Amenity(self):
        """chekcing if amenity have attibutes"""
        self.assertTrue(hasattr(self.amen, "id"))
        self.assertTrue(hasattr(self.amen, "created_at"))
        self.assertTrue(hasattr(self.amen, "updated_at"))
        self.assertTrue(hasattr(self.amen, 'name'))

    def test_subclass(self):
        """ """
        self.assertTrue(issubclass(self.value, BaseModel))
