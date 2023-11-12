#!/usr/bin/python3
"""Unit tests for the AirBnB console"""

import unittest
import console
from console import HBNBCommand


class test_console(unittest.TestCase):
    """Definition of the test console class"""

    def create(self):
        """Instantiation of Create method"""
        return HBNBCommand()

    def test_quit(self):
        """ Instantiation of tje test_quit method"""
        con = self.create()
        self.assertTrue(con.onecmd("quit"))

    def test_EOF(self):
        """Instantiation of the test_EOF method"""
        con = self.create()
        self.assertTrue(con.onecmd("EOF"))
