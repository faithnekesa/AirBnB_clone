#!/usr/bin/python3
'''A class user that inherent from BaseModel'''
from models.base_model import BaseModel


class User(BaseModel):
    '''represent a class User'''

    first_name = ""
    last_name = ""
    email = ""
    password = ""
