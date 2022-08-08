#!/usr/bin/python3
"""Serializes instances to a JSON file
and deserializes JSON file to instances"""

import json
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review


class FileStorage:
    """FileStorage class
    Attributes:
        __file_path: str - path to the JSON file
        __objects: dict - empty but will store all objects by <class name>.id
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """returns the dictionary __objects"""
        return self.__objects

    def new(self, obj):
        """sets in __objects the obj with key <obj class name>.id"""
        if obj is not None:
            key = obj.__class__.__name__+"."+obj.id
            self.__objects[key] = obj

    def save(self):
        """serializes __objects to the JSON file (path: __file_path)"""
        dic_obj = {}
        for key in self.__objects:
            dic_obj[key] = self.__objects[key].to_dict()
        # Convert the dictionary into json and save in __filepath.
        with open(self.__file_path, 'w') as jsonFile:
            json.dump(dic_obj, jsonFile)

    def reload(self):
        """deserializes the JSON file to __objects
        (only if the JSON file (__file_path) exists ; otherwise, do nothing.
        If the file doesn’t exist, no exception should be raised)
        """
        try:
            with open(self.__file_path, 'r', encoding="utf8") as f:
                obj_dict = json.load(f)
            for obj_item in obj_dict.values():
                class_name = obj_item["__class__"]
                del obj_item["__class__"]
                self.new(eval(class_name)(**obj_item))
        except Exception:
            pass

    def update_obejts(self, ob):
        self.__objects = ob
        self.save()
