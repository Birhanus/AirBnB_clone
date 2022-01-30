#!/usr/bin/python3
"""create unique FileStorage instances"""

from engine.file_storage import Filestorage

storage = Filestorage()
# storage._FileStorage__file_path = 'data.json'
# storage._FileStorage__objects = {}
models = {}


def import_models():
    """import modules after intiating a storage instance to fix imports"""
    global models
    from amenity import Amenity
    from base_model import BaseModel
    from city import City
    from place import Place
    from review import Review
    from state import State
    from user import User

    models = {c.__name__: c
              for c in [BaseModel, Amenity, City, Place, Review, State, User]}


import_models()
storage.reload()
