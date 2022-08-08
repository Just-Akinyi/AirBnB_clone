#!/usr/bin/python3
"""Defines all common attributes/methods for other classes"""
import models
from uuid import uuid4
from datetime import datetime


class BaseModel:
    """Base class
        Arttributes:
            id(str): assign with an uuid when an instance is created
            created_at: assigns current datetime
            updated_at: updates current datetime
    """

    def __init__(self, *args, **kwargs):
        """Initializing Base class
        Args:
            *args: a Tuple that contains all arguments
            **kwargs: a dictionary that contains all arguments by key/value
        """
        DATE_FORMAT = "%Y-%m-%dT%H:%M:%S.%f"
        self.id = str(uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
        if kwargs:
            for key, val in kwargs.items():
                if key in ("created_at", "updated_at"):
                    self.__dict__[key] = datetime.strptime(val, DATE_FORMAT)
                else:
                    self.__dict__[key] = val
        else:
            models.storage.new(self)

    def save(self):
        """updates the attribute updated_at with the current datetime"""
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """Returns a dictionary containing all keys/values
        of __dict__ of the instance
        a key __class__ must be added to this dictionary with the class name
        of the object
        """
        dictionnary = self.__dict__.copy()
        dictionnary['created_at'] = self.created_at.isoformat()
        dictionnary['updated_at'] = self.updated_at.isoformat()
        dictionnary['__class__'] = self.__class__.__name__
        return dictionnary

    def __str__(self):
        """Return the print/str representation of the BaseModel instance."""
        className = self.__class__.__name__
        return "[{}] ({}) {}".format(className, self.id, self.__dict__)
