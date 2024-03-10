#!/usr/bin/python3
"""
Define the BaseModel class.
"""
from uuid import uuid4
from datetime import datetime
from models import storage


class BaseModel:
     def __init__(self, *args, **kwargs):
        timeFormat = "%Y-%m-%dT%H:%M:%S.%f"
        if kwargs:
            for key, val in kwargs.items():
                if key =="__class__":
                    continue
                elif key == "created_at" or key == "updated_at":
                     setattr(self, key, datetime.strptime(val, timeFormat))
                else:
                     setattr(self, key, val)
        else:
            self.id = str(uuid4())

            self.created_at = datetime.utcnow()
            self.updated_at = datetime.utcnow()

            storage.new(self)
   

     def save(self):
         """Update the current date and time."""

         self.updated_at = datetime.utcnow()
         storage.save()
         return self.updated_at

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


if __name__ == '__main__':
   my_model = BaseModel()
   my_model.name = "My First Model"
   my_model.my_number = 89
   print(my_model)
   my_model.save()
   print(my_model)
   my_model_json = my_model.to_dict()
   print(my_model_json)
   print("JSON of my_model:")
   for key in my_model_json.keys():
      print("\t{}: ({}) - {}".format(key, type(my_model_json[key]), my_model_json[key]))