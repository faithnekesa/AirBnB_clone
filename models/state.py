#!/usr/bin/python3
"""Inherent Class for BaseModel"""
from models.base_model import BaseModel


class State(BaseModel):
    """Definition for Class State"""

    name = ""

    def __init__(self, *args, **kwargs):
        """Function for initializion of class State"""
        super().__init__(*args, **kwargs)
