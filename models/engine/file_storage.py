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
    return FileStorage.__objects

def new(self, obj):
    """sets in __object the obj with key <obj class name>.id"""
    obj_class_name = obj.__class__.__name__
    obj_id = obj.id
    key_name = obj_class_name + "." + obj_id
    
    FileStorage.__objects[key_name] = obj
    return obj

def save(self):
    """seralizes __objects to JSON file"""
    obj_dict = {}
    for k, v in FileStorage.__objects.items():
        obj_dict[k] = v.to_dict()
    with open(FileStorage.__file_path, "w") as FILE:
        json.dump(obj_dict, FILE)

def reload(self):
    """
     deserializes the JSON file to __objects
     does nothing if file is not found
    """
    try:
        with open(FileStorage.__file_path, "r") as read_file:
            dummy_dict = json.load(read_file)
            for k, v in dummy_dict.items():
                FileStorage.__objects[k] = eval(v['__class__'])(**v)
    except FileNotFoundError:
            pass
