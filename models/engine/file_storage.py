#!/usr/bin/python3
"""Serializes instances to a JSON file
and deserializes JSON file to instances"""

import json
import models


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
        # open file with write permission
        with open(self.__file_path, 'w', encoding="utf-8") as jsonFile:
            # if __objects is not empty
            if self.__objects is not None:
                for key, val in self.__objects.items():
                    dic_obj[key] = val.to_dict()
                    json.dump(dic_obj, jsonFile)

    def reload(self):
        """deserializes the JSON file to __objects
        (only if the JSON file (__file_path) exists ; otherwise, do nothing.
        If the file doesn’t exist, no exception should be raised)
        """
        try:
            with open(self.__file_path, 'r', encoding="utf-8") as jf:
                data = json.load(jf)
                for item in data.values():
                    class_name = item["__class__"]
                    del item["__class__"]
                    print("test {}".format(item))
                    self.new(eval(class_name)(**item))
        except Exception:
            pass
