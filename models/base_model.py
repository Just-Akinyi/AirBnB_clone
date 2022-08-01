#!/usr/bin/python3
"""Defines all common attributes/methods for other classes"""
from uuid import uuid4
from datetime import datetime


class Basemodel:
    """Base class"""

    def __init__(self, *args, **kwargs):
        """Initializing Base class
        Args:
            *args:
            **kwargs (dict):
        """
        self.id = str(uuid4())
        self.created_at = datetime.today()
        self.update_at = datetime.today()

    def save(self):
        """updates the attribute updated_at with the current datetime"""
