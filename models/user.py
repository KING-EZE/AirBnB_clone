#!/usr/bin/python3
'''this module creates a user class'''
from models.base_model import BaseModel


class User(BaseModel):
    '''Class for managing user objects'''
    email = ""
    password = ""
    first_name = ""
    last_name = ""

    def __init__(self, *args, **kwargs):
        '''Initializes attributes for the User class'''
        super().__init__(*args, **kwargs)
