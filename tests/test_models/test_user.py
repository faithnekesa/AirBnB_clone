#!/usr/bin/python3
"""Test module for test User class"""
import unittest
import datetime
import pep8
import json


from models.user import User
from models.base_model import BaseModel


class TestUser(unittest.TestCase):
    """Check implementation for User class"""
    def test_doc_module(self):
        """Function for documentation module"""
        doc = User.__doc__
        self.assertGreater(len(doc), 1)

    def test_pep8_conformance_base_model(self):
        """Function thats tests user.py aligns with PEP8"""
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['models/user.py'])
        self.assertEqual(result.total_errors, 0,
                         "Code style errors and (or warnings) found")

    def test_pep8_conformance_test_base_model(self):
        """Function that checks if test_user.py aligns to PEP8"""
        pep8style = pep8.StyleGuide(quiet=True)
        res = pep8style.check_files(['tests/test_models/test_user.py'])
        self.assertEqual(res.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_doc_constructor(self):
        """Fucntion that checks constructor for documentation"""
        doc = User.__init__.__doc__
        self.assertGreater(len(doc), 1)

    def test_class(self):
        """Functon that checks teh class attributes of a class"""
        with self.subTest(msg='Inheritance'):
            self.assertTrue(issubclass(User, BaseModel))

        with self.subTest(msg='Attributes'):
            self.assertIsInstance(User.email, str)
            self.assertIsInstance(User.password, str)
            self.assertIsInstance(User.first_name, str)
            self.assertIsInstance(User.last_name, str)


if __name__ == '__main__':
    unittest.main()
