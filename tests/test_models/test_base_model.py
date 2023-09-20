#!/usr/bin/python3
""" """
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
import unittest
import datetime
import json
import os
import time
import uuid


class test_basemodel(unittest.TestCase):
    """ """

    def __init__(self, *args, **kwargs):
        """ """
        super().__init__(*args, **kwargs)
        self.name = 'BaseModel'
        self.value = BaseModel

    def setUp(self):
        """ """
        pass

    def tearDown(self):
        try:
            os.remove('file.json')
        except Exception:
            pass

    def test_default(self):
        """ """
        i = self.value()
        self.assertEqual(type(i), self.value)

    def test_kwargs(self):
        """ """
        i = self.value()
        copy = i.to_dict()
        new = BaseModel(**copy)
        self.assertFalse(new is i)

    def test_kwargs_int(self):
        """ """
        i = self.value()
        copy = i.to_dict()
        copy.update({1: 2})
        with self.assertRaises(TypeError):
            new = BaseModel(**copy)

    def test_save(self):
        """ Testing save """
        i = self.value()
        i.save()
        key = self.name + "." + i.id
        with open('file.json', 'r') as f:
            j = json.load(f)
            self.assertEqual(j[key], i.to_dict())

    def test_str(self):
        """ """
        i = self.value()
        self.assertEqual(str(i), '[{}] ({}) {}'.format(self.name, i.id,
                         i.__dict__))

    def test_todict(self):
        """ """
        i = self.value()
        n = i.to_dict()
        self.assertEqual(i.to_dict(), n)

    def test_kwargs_none(self):
        """ """
        n = {None: None}
        with self.assertRaises(TypeError):
            new = self.value(**n)

    def test_kwargs_one(self):
        """ """
        n = {'Name': 'test'}
        new = self.value(**n)

    def test_id(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.id), str)
        old = self.value()
        self.assertNotEqual(new.id, old.id)
        lis = [self.value().id for i in range(2000)]
        self.assertEqual(len(lis), len(set(lis)))

    def test_created_at(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.created_at), datetime.datetime)
        newer = self.value()
        self.assertTrue(new.created_at < newer.created_at)

    def test_updated_at(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.updated_at), datetime.datetime)
        n = new.to_dict()
        new = BaseModel(**n)
        self.assertFalse(new.created_at == new.updated_at)
        pt = new.updated_at
        new.save()
        nt = new.updated_at
        self.assertTrue(pt < nt)


class test_BaseModel_save(unittest.TestCase):
    """The save method test case

    Args:
        unittest (_type_): _description_
    """

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.name = 'BaseModel'
        self.value = BaseModel

    def clear_storage(self):
        """_summary_
        """
        FileStorage._FileStorage__objects = {}
        if os.path.isfile(FileStorage._FileStorage__file_path):
            os.remove(FileStorage._FileStorage__file_path)

    def tearDown(self) -> None:
        self.clear_storage()

    def test_no_args(self):
        """_summary_
        """
        with self.assertRaises(TypeError):
            self.value.save()

    def test_available(self):
        """_summary_
        """
        self.clear_storage()
        self.assertFalse(os.path.isfile(FileStorage._FileStorage__file_path))
        new = self.value()
        new.save()
        self.assertTrue(os.path.isfile(FileStorage._FileStorage__file_path))

    def test_update_time(self):
        """
        """
        new = self.value()
        ctime = new.created_at
        time.sleep(0.1)
        new.save()
        uptime = new.updated_at
        self.assertTrue(ctime < uptime)

    def test_stored(self):
        """_summary_
        """
        new = self.value()
        new.save()
        dic = {f"{self.name}.{new.id}": new.to_dict()}
        self.assertTrue(os.path.isfile(FileStorage._FileStorage__file_path))
        with open(FileStorage._FileStorage__file_path) as file:
            self.assertEqual(json.JSONEncoder().encode(dic), file.read())
            file.seek(0)
            self.assertEqual(json.JSONDecoder().decode(file.read()), dic)


class test_to_dict(unittest.TestCase):
    """_summary_

    Args:
        unittest (_type_): _description_
    """
    def test_type(self):
        """_summary_
        """
        new = BaseModel()
        self.assertIsInstance(new.to_dict(), dict)

    def test_two(self):
        """_summary_
        """
        d1 = BaseModel().to_dict()
        d2 = BaseModel().to_dict()
        self.assertNotEqual(d1, d2)

    def test_withargs(self):
        """_summary_
        """
        with self.assertRaises(TypeError):
            BaseModel().to_dict(23)

    def test_presence(self):
        """_summary_
        """
        new = BaseModel()
        name = "Hollow"
        new.firstname = name
        dic = new.to_dict()
        self.assertEqual(dic['firstname'], name)

    def test_no_args(self):
        """_summary_
        """
        with self.assertRaises(TypeError):
            BaseModel.to_dict()

    def test_create(self):
        """_summary_
        """
        dic = {
            "id": str(uuid.uuid4()),
            "__class__": "BaseModel",
            "updated_at": datetime.datetime.now().isoformat(),
            "created_at": datetime.datetime.now().isoformat(),
            "name": "Hollow",
            "age": 34
        }
        new = BaseModel(**dic)
        self.assertDictEqual(dic, new.to_dict())
