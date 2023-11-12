#!/usr/bin/python3
"""Inherent Class for BaseModel"""
from models.base_model import BaseModel


class Review(BaseModel):
    """Definition of class Review"""

    place_id = ""
    user_id = ""
    text = ""

    def __init__(self, *args, **kwargs):
        """Function initialization for class Review"""
        super().__init__(*args, **kwargs)
