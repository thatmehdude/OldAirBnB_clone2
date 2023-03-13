#!/usr/bin/python3
"""Defines a file storage class"""

import json
from models.base_model import BaseModel

class FileStorage:
    """file storage class"""
    __file_path = "file.json"
    __objects = {}
    
def all(self):
    """returns the dictionary __objects"""
    return Filestorage.__objects

def new(self, obj):
    """sets in __object the obj with key <obj class name>.id"""
    obj_class_name = obj.__class__.__name__
    obj_id = obj.id
    key = obj_class_name + "." + obj_id
    return Filestorage.__objects[key] = obj


