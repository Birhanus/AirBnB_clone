#!/usr/bin/python3
"""Define the State class."""
from models.base_model import BaseModel


class State(BaseModel):
    """ Represent a state.
    Attrinutes:
         name (str): The name of the state
    """
    name = ""
