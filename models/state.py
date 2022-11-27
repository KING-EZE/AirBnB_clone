#!/bin/usr/python3
'''this module creates a user class'''
from models.base_model import BaseModel


class State(BaseModel):
    '''class for managing state objects'''
    name = ""

    def __init__(self, *args, **kwargs):
        '''Initializes attributes for the State class'''
        super().__init__(*args, **kwargs)
