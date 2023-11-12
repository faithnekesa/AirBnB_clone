#!/usr/bin/python3
"""inherent class for BaseModel"""
from models.base_model import BaseModel


class Amenity(BaseModel):
    """Definition for Class amenity"""

    name = ""

    def __init__(self, *args, **kwargs):
        """Initialization of the Amenity class"""
        super().__init__(*args, **kwargs)
