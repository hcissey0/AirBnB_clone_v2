#!/usr/bin/python3
"""Test cases for the console"""

from io import StringIO
from models.base_model import BaseModel
from models.state import State
from models.user import User
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.engine.file_storage import FileStorage
import unittest
from unittest.mock import patch
import os
import sys
import json
import console
import pep8

@unittest.skipIf(os.getenv("HBNB_TYPE_STORAGE") == 'db', "DATABASE")
class test_console(unittest.TestCase):
    """This is the test case for the console app"""

    def __init__(self, *args, **kwargs):
        """This is the constructor
        """
        super().__init__(*args, **kwargs)
        self.cons = console.HBNBCommand()

    @classmethod
    def setUpClass(cls):
        """set up class"""
        try:
            os.remove(FileStorage._FileStorage__file_path)
        except Exception:
            pass

    @classmethod
    def tearDown(self) -> None:
        try:
            os.remove(FileStorage._FileStorage__file_path)
        except Exception:
            pass

    def test_pep8(self):
        """test for pepe
        """
        s = pep8.StyleGuide(quiet=True)
        p = s.check_files(["console.py"])
        self.assertEqual(p.total_errors, 0, 'Pep8 has error')

    def test_emptyline(self):
        """_summary_
        """
        with patch('sys.stdout', new=StringIO()) as t:
            self.cons.onecmd("\n")
            self.assertEqual("", t.getvalue())

    # Testing create
    def test_create_no_class_name(self):
        """_summary_
        """
        with patch('sys.stdout', new=StringIO()) as t:
            self.cons.onecmd('create')
            self.assertEqual('** class name missing **\n', t.getvalue())

    def test_create_wrong_class_name(self):
        """_summary_
        """
        with patch('sys.stdout', new=StringIO()) as t:
            self.cons.onecmd('create hello')
            self.assertEqual(t.getvalue(), "** class doesn't exist **\n")

    def test_create_params(self):
        """_summary_
        """
        with patch('sys.stdout', new=StringIO()) as t:
            self.cons.onecmd('create User name="Naame"')
            self.assertIsNotNone(t.getvalue)

    def test_all_user(self):
        """_summary_
        """
        with patch('sys.stdout', new=StringIO()) as t:
            self.cons.onecmd('create User')
            t.truncate()
            self.cons.onecmd('all')
            self.assertNotEqual("[]\n", t.getvalue())

    def test_quit(self):
        """Used to test quit
        """
        with patch('sys.stdout', new=StringIO()) as t:
            self.cons.onecmd("quit")
            self.assertEqual("", t.getvalue())

    # Testing show
    def test_show_no_class(self):
        """no class test
        """
        with patch('sys.stdout', new=StringIO()) as t:
            self.cons.onecmd('show')
            self.assertEqual(
                '** class name missing **\n', t.getvalue()
            )

    def test_show_wrong_class(self):
        """wrong class test
        """
        with patch('sys.stdout', new=StringIO()) as t:
            self.cons.onecmd("show how")
            self.assertEqual(
                "** class doesn't exist **\n", t.getvalue())

    def test_show_no_id(self):
        """no instance id"""
        with patch('sys.stdout', new=StringIO()) as t:
            self.cons.onecmd("show User")
            self.assertEqual(
                "** instance id missing **\n", t.getvalue())

    def test_show_wrong_id(self):
        """test with wrong id"""
        with patch('sys.stdout', new=StringIO()) as t:
            self.cons.onecmd("show User sdf")
            self.assertEqual(
                "** no instance found **\n", t.getvalue())

    # Testing destroy
    def tes_destroy_no_class(self):
        """no class name"""
        with patch('sys.stdout', new=StringIO()) as t:
            self.cons.onecmd("destroy")
            self.assertEqual(
                "** class name missing **\n", t.getvalue())

    def test_destroy_wrong_class(self):
        """wrong class name test"""
        with patch('sys.stdout', new=StringIO()) as t:
            self.cons.onecmd("destroy nod")
            self.assertEqual(
                "** class doesn't exist **\n", t.getvalue())

    def test_destroy_no_id(self):
        """no instance id"""
        with patch('sys.stdout', new=StringIO()) as t:
            self.cons.onecmd("destroy User")
            self.assertEqual(
                "** instance id missing **\n", t.getvalue())

    def test_destroy_wrong_id(self):
        """wrong instance id"""
        with patch('sys.stdout', new=StringIO()) as t:
            self.cons.onecmd("destroy User ndfn")
            self.assertEqual(
                "** no instance found **\n", t.getvalue())

    # Testing all
    def test_all_no_class(self):
        """no class"""
        with patch('sys.stdout', new=StringIO()) as t:
            self.cons.onecmd("all")
            self.assertEqual("[]\n", t.getvalue())

    def test_all_with_class(self):
        """with class"""
        with patch('sys.stdout', new=StringIO()) as t:
            self.cons.onecmd("all User")
            self.assertIsNotNone(t.getvalue())

    def test_all_wrong_class(self):
        """test wrong class"""
        with patch("sys.stdout", new=StringIO()) as t:
            self.cons.onecmd("all dfl")
            self.assertEqual(
                "** class doesn't exist **\n", t.getvalue())

    def test_doc_string(self):
        """testing docstring"""
        self.assertIsNotNone(console.__doc__)
        self.assertIsNotNone(console.HBNBCommand.emptyline.__doc__)
        self.assertIsNotNone(console.HBNBCommand.do_quit.__doc__)
        self.assertIsNotNone(console.HBNBCommand.do_EOF.__doc__)
        self.assertIsNotNone(console.HBNBCommand.do_all.__doc__)
        self.assertIsNotNone(console.HBNBCommand.do_create.__doc__)
        self.assertIsNotNone(console.HBNBCommand.do_show.__doc__)
        self.assertIsNotNone(console.HBNBCommand.do_destroy.__doc__)
        self.assertIsNotNone(console.HBNBCommand.do_update.__doc__)
        self.assertIsNotNone(console.HBNBCommand.do_count.__doc__)

    # Testing update
    def test_update_no_class_name(self):
        """tesing the update
        """
        with patch('sys.stdout', new=StringIO()) as t:
            self.cons.onecmd("update")
            self.assertEqual(
                "** class name missing **\n", t.getvalue()
            )

    def test_update_wrong_class(self):
        """wrong class update"""
        with patch('sys.stdout', new=StringIO()) as t:
            self.cons.onecmd("update lksjdf")
            self.assertEqual(
                "** class doesn't exist **\n", t.getvalue()
            )

    def test_update_no_id(self):
        """no instance id"""
        with patch('sys.stdout', new=StringIO()) as t:
            self.cons.onecmd("update User")
            self.assertEqual(
                "** instance id missing **\n", t.getvalue()
            )

    def test_update_wrong_id(self):
        """wrong id"""
        with patch('sys.stdout', new=StringIO()) as t:
            self.cons.onecmd("update User skldf")
            self.assertEqual(
                "** no instance found **\n", t.getvalue())

    def test_no_attribute(self):
        """no attribute"""
        uid = ""
        with patch('sys.stdout', new=StringIO()) as t:
            self.cons.onecmd("create User")
            uid = t.getvalue()
        with patch('sys.stdout', new=StringIO()) as t:
            self.cons.onecmd("update User " + uid)
            self.assertEqual(
                "** attribute name missing **\n", t.getvalue())

    def test_no_value(self):
        """value missing"""
        uid = ""
        with patch('sys.stdout', new=StringIO()) as t:
            self.cons.onecmd("create User")
            uid = t.getvalue()
        with patch('sys.stdout', new=StringIO()) as t:
            self.cons.onecmd("update User " + uid[:-1] + " name")
            self.assertEqual(
                "** value missing **\n", t.getvalue()
            )

    # Testing <class>.<command>()
    # Testing <class>.all()
    def test_wrong_class_all(self):
        """test class.all()"""
        with patch('sys.stdout', new=StringIO()) as t:
            self.cons.onecmd(self.cons.precmd("sldj.all()"))
            self.assertEqual(
                "** class doesn't exist **\n", t.getvalue()
            )

    def test_correct_class_all(self):
        """testing with correct class"""
        with patch('sys.stdout', new=StringIO()) as t:
            self.cons.onecmd(self.cons.precmd("User.all()"))
            self.assertRegex(t.getvalue(), r'\[.*\]\n')

    # Testing <class>.count()
    def test_wrong_class_count(self):
        """testing with wrong class"""
        with patch('sys.stdout', new=StringIO()) as t:
            self.cons.onecmd(self.cons.precmd("sldfj.count()"))
            self.assertEqual(
                "** class doesn't exist **\n", t.getvalue()
            )

    def test_correct_class_count(self):
        """testing with a correct class"""
        with patch('sys.stdout', new=StringIO()) as t:
            self.cons.onecmd(self.cons.precmd("User.count()"))
            self.assertRegex(t.getvalue(), r'\d+\n')

    # Testing <class>.destroy()
    def test_wrong_class_destroy(self):
        """testing with wrong class"""
        with patch('sys.stdout', new=StringIO()) as t:
            self.cons.onecmd(self.cons.precmd("lsdf.destroy()"))
            self.assertEqual(
                "** class doesn't exist **\n", t.getvalue()
            )

    def test_no_id_destroy(self):
        """test with no id"""
        with patch('sys.stdout', new=StringIO()) as t:
            self.cons.onecmd(self.cons.precmd("User.destroy()"))
            self.assertEqual(
                "** instance id missing **\n", t.getvalue()
            )

    def test_wrong_id_destroy(self):
        """test with wrong id"""
        with patch('sys.stdout', new=StringIO()) as t:
            self.cons.onecmd(self.cons.precmd("User.destroy(helo)"))
            self.assertEqual(
                "** no instance found **\n", t.getvalue()
            )

    # Testing <class>.update()
    def test_wrong_class_update(self):
        """testing with a wrong class"""
        with patch('sys.stdout', new=StringIO()) as t:
            self.cons.onecmd(self.cons.precmd("lsdfj.update()"))
            self.assertEqual(
                "** class doesn't exist **\n", t.getvalue()
            )

    def test_no_id_update(self):
        """testing with a wrong id"""
        with patch('sys.stdout', new=StringIO()) as t:
            self.cons.onecmd(self.cons.precmd("User.update()"))
            self.assertEqual(
                "** instance id missing **\n", t.getvalue()
            )

    def test_wrong_id_update(self):
        """Testing with a wrong id"""
        with patch('sys.stdout', new=StringIO()) as t:
            self.cons.onecmd(self.cons.precmd("User.update(sldf)"))
            self.assertEqual(
                "** no instance found **\n", t.getvalue()
            )

    def test_no_attribute_update(self):
        """tesing with no attribute name"""
        uid = ""
        with patch('sys.stdout', new=StringIO()) as f:
            self.cons.onecmd("create User")
            uid = f.getvalue()[:-1]
        with patch('sys.stdout', new=StringIO()) as t:
            self.cons.onecmd(self.cons.precmd(
                "User.update(" + uid + ")"))
            self.assertEqual(
                "** attribute name missing **\n", t.getvalue()
            )

    def test_no_value_update(self):
        """testing without attribute value"""
        uid = ""
        with patch('sys.stdout', new=StringIO()) as t:
            self.cons.onecmd('create User')
            uid = t.getvalue()[:-1]
        with patch('sys.stdout', new=StringIO()) as t:
            self.cons.onecmd(self.cons.precmd(
                "User.update(" + uid + " name)"))
            self.assertEqual(
                "** value missing **\n", t.getvalue()
            )

    # Testing <class>.show()
    def test_wrong_class_show(self):
        """testing with a wrong class"""
        with patch("sys.stdout", new=StringIO()) as t:
            self.cons.onecmd(self.cons.precmd("sjdlf.show()"))
            self.assertEqual(
                "** class doesn't exist **\n", t.getvalue()
            )

    def test_no_id_show(self):
        """testing with a correct class"""
        with patch('sys.stdout', new=StringIO()) as t:
            self.cons.onecmd(self.cons.precmd("User.show()"))
            self.assertEqual(
                "** instance id missing **\n", t.getvalue()
            )

    def test_wrong_id_show(self):
        """Testing with a wrong id"""
        with patch('sys.stdout', new=StringIO()) as t:
            self.cons.onecmd(self.cons.precmd("User.show(sldf)"))
            self.assertEqual(
                "** no instance found **\n", t.getvalue()
            )

    def test_correct_id_show(self):
        """tesing with no attribute name"""
        uid = ""
        with patch('sys.stdout', new=StringIO()) as f:
            self.cons.onecmd("create User")
            uid = f.getvalue()[:-1]
        with patch('sys.stdout', new=StringIO()) as t:
            self.cons.onecmd(self.cons.precmd(
                "User.show(" + uid + ")"))
            self.assertRegex(
                t.getvalue(), r'\[.*\] \(.*\) \{.*\}'
            )


if __name__ == '__main__':
    unittest.main()
