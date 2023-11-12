#!/usr/bin/python3
"""Test module for Review class"""
import unittest
import datetime
import json
import pep8

from models.review import Review
from models.base_model import BaseModel


class TestReview(unittest.TestCase):
    """Class definition for Test Review class"""
    def test_doc_module(self):
        """Function for module documentation"""
        doc = Review.__doc__
        self.assertGreater(len(doc), 1)

    def test_pep8_conformance_review(self):
        """Function that checks if review.py aligns to PEP8"""
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['models/review.py'])
        self.assertEqual(result.total_errors, 0,
                         "Code style errors (and warnings) found")

    def test_pep8_conformance_test_review(self):
        """Function that checks if test_review.py aligns to PEP8"""
        pep8style = pep8.StyleGuide(quiet=True)
        res = pep8style.check_files(['tests/test_models/test_review.py'])
        self.assertEqual(res.total_errors, 0,
                         "Code style errors (and warnings) found")

    def test_doc_constructor(self):
        """Function that checks for constructor documentation"""
        doc = Review.__init__.__doc__
        self.assertGreater(len(doc), 1)

    def test_class(self):
        """Function that checks the class attributes type"""
        with self.subTest(msg='Inheritance'):
            self.assertTrue(issubclass(Review, BaseModel))

        with self.subTest(msg='Attributes'):
            self.assertIsInstance(Review.place_id, str)
            self.assertIsInstance(Review.user_id, str)
            self.assertIsInstance(Review.text, str)


if __name__ == '__main__':
    unittest.main()
