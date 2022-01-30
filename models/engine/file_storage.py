#!/usr/bin/python3
"""
serializes instances to a JSON file and deserializes JSON file to instances
"""

import json
from os import path
from os.path import isfile
from models.amenity import Amenity
from models.base_model import BaseModel
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User
import sys


class FileStorage:
    """Filestorage Representation"""
    __file_path = "file.json"
    __objects = dict()

    def __init__(self):
        """Initialization"""
        pass

    def all(self):
        """ returns the dictionary __objects"""
        return (self.__objects)

    def new(self, obj):
        """sets in __objects the obj with key <obj class name>.id"""
        key = '{}.{}'.format(obj.__class__.__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        """serializes __objects to the JSON file (path: __file_path)"""
        dic_obj = {k: v.to_dict() for k, v in FileStorage.__objects.items()}
        with open(self.__file_path, "w") as f:
            json.dump(dic_obj, f)

    def reload(self):
        """deserializes the JSON file to __objects
        (only if the JSON file (__file_path) exists
        """
        fil = self.__file_path
        if path.isfile(fil):
            with open(FileStorage.__file_path, "r") as f:
                json_f = json.load(f)
                for value in json_f.values():
                    clsName = value["__class__"]
                    del value["__class__"]
                    self.new(eval(clsName)(**value))
