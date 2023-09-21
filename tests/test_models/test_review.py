#!/usr/bin/python3
""" """
from tests.test_models.test_base_model import test_basemodel
from models.base_model import BaseModel
from models.review import Review


class test_review(test_basemodel):
    """ """

    def __init__(self, *args, **kwargs):
        """ """
        super().__init__(*args, **kwargs)
        self.name = "Review"
        self.value = Review

    def test_subclass(self):
        """
        """
        self.assertTrue(issubclass(Review, BaseModel))

    def test_attrs(self):
        new = self.value()
        self.assertTrue(hasattr(new, "place_id"))
        self.assertTrue(hasattr(new, "text"))
        self.assertTrue(hasattr(new, "user_id"))
