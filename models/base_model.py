#!/usr/bin/python3
"""Defines all common attributes/methods for other classes"""
from pydoc import classname
from uuid import uuid4
from datetime import datetime


class BaseModel:
    """Base class"""

    def __init__(self):
        """Initializing Base class
        Args:
            *args:
            **kwargs (dict):
        """
        self.id = str(uuid4())
        self.created_at = datetime.now()
        self.update_at = datetime.now()

    def save(self):
        """updates the attribute updated_at with the current datetime"""
        self.update_at = datetime.now()

    def to_dict(self):
        """Returns a dictionary containing all keys/values
        of __dict__ of the instance
        a key __class__ must be added to this dictionary with the class name
        of the object
        """
        dictionnary = self.__dict__
        dictionnary['__class__'] = self.__class__.__name__
        dictionnary['created_at'] = self.created_at.isoformat()
        dictionnary['update_at'] = self.update_at.isoformat()
        return dictionnary

    def __str__(self):
        """Return the print/str representation of the BaseModel instance."""
        className = self.__class__.__name__
        return "[{}] ({}) {}".format(className, self.id, self.__dict__)
