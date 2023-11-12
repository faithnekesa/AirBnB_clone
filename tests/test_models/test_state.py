#!/usr/bin/python3
"""Module for test State class"""
import json
import unittest
import datetime
import pep8

from models.state import State
from models.base_model import BaseModel


class TestState(unittest.TestCase):
    """Class definition for TestState class implementation"""
    def test_doc_module(self):
        """Function that checks module documentation"""
        doc = State.__doc__
        self.assertGreater(len(doc), 1)

    def test_pep8_conformance_state(self):
        """Function that checks if state.py aligns to PEP8"""
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['models/state.py'])
        self.assertEqual(result.total_errors, 0,
                         "Code style errors (and warnings) found")

    def test_pep8_conformance_test_state(self):
        """Function that checks if test_state.py aligns to PEP8"""
        pep8style = pep8.StyleGuide(quiet=True)
        res = pep8style.check_files(['tests/test_models/test_state.py'])
        self.assertEqual(res.total_errors, 0,
                         "Code style errors (and warnings) found")

    def test_doc_constructor(self):
        """Function that checks constructor documentation"""
        doc = State.__init__.__doc__
        self.assertGreater(len(doc), 1)

    def test_class(self):
        """Function that checks class attributes type"""
        with self.subTest(msg='Inheritance'):
            self.assertTrue(issubclass(State, BaseModel))

        with self.subTest(msg='Attributes'):
            self.assertIsInstance(State.name, str)


if __name__ == '__main__':
    unittest.main()
