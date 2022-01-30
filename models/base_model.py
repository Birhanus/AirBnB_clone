#!/usr/bin/python3
"""
    module for 'BaseModel class'
    that defines all common attributes/methods for other classes
"""
import models
from uuid import uuid4
from datetime import datetime


class BaseModel:
    """Defines common attributes/methods for other classes"""
    def __init__(self, *args, **kwargs):
        """Initializes a new instance of BaseModel class
        Args:
        *args (any type): A variable number of arguments
        **kwargs (dict): Key/value pairs of attributes
        """
        if kwargs:
            for k in kwargs:
                if k in ['created_at', 'updated_at']:
                    setattr(self, k, datetime.fromisoformat(kwargs[k]))
                elif k != '__class__':
                    setattr(self, k, kwargs[k])
        else:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)

    def __str__(self):
        """Returns the string representation of an instance of BaseModel"""
        clsname = self.__class__.__name__
        val = "[" + clsName + "] " + "(" + self.id + ") " + str(self.__dict__)
        return (val)

    def save(self):
        """Updates the public instance attribute updated_at"""
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """Returns a dictionary containing all keys/values
        of `__dict__` of the instance.
        """
        dct = self.__dict__.copy()
        dct["__class__"] = self.__class__.__name__
        dct["created_at"] = self.created_at.isoformat()
        dct["updated_at"] = self.updated_at.isoformat()
        return (dct)
