#!/usr/bin/python3

"""Defines a base model class."""

import uuid
from datetime import datetime
import models

class BaseModel:
    """the base model of the console"""

    def __init__(self, *args, **kwargs):
        """initialiser"""
        
        if kwargs:
            for k, v in kwargs.items():
                if k == "created_at" or k == "updated_at":
                    v = datetime.fromisoformat(kwargs[k])
                if k == "__class__":
                    pass
                else:
                    setattr(self, k, v)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
    
    def __str__(self):
        """return a string representation"""
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        """update and save time of update"""
        self.updated_at = datetime.now()

    def to_dict(self):
        """returns a dictioary with all keys and values of the instance"""
        new_dict = {}

        for key, value in self.__dict__.items():
            if key == "created_at":
                new_dict[key] = datetime.isoformat(value)
            elif key == "updated_at":
                new_dict[key] = datetime.isoformat(value)
            else:
                new_dict[key] = value
        new_dict['__class__'] = type(self).__name__
        return new_dict
    