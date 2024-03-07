#!/usr/bin/python3
"""
Define the BaseModel class.
"""
from uuid import uuid4
from datetime import datetime


class BaseModel:
     def __init__(self):
        self.id = str(uuid4())

        self.created_at = datetime.utcnow()
        self.updated_at = datetime.utcnow()

     def save(self):
         """Update the current date and time."""

         self.updated_at = datetime.utcnow()

     def to_dict(self):
        """
        Dictionary of the BaseModel.

        Include the key and value pair of the __class__ name.
        """
        con_to_dict = self.__dict__.copy()
        con_to_dict["__class__"] = self.__class__.__name__
        con_to_dict["created_at"] = self.created_at.isoformat()
        con_to_dict["updated_at"] = self.updated_at.isoformat()
        return con_to_dict

     def __str__(self):
         """
        Return the string representation of the BaseModel.
        """
         class_name = self.__class__.__name__
         return "[{}] ({}) {}".format(class_name, self.id, self.__dict__)

