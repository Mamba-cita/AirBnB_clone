#!/usr/bin/python3
"""
Define the FileStorage class.
"""
import json
from models.base_model import BaseModel
import models.city
import models.amenity
import models.place
import models.review
import models.state
import models.user


class FileStorage:
    """
    Attributes:
        __file_path (str): The name of the file to save objects to.
        __objects (dict): empty dictionary for storage.
    """
    __file_path = "file.json"
    __objects = {}

    def new(self, obj):
        """Set  __objects obj with key <obj_class_name>.id"""
        objclsname = obj.__class__.__name__
        FileStorage.__objects["{}.{}".format(objclsname, obj.id)] = obj

    def all(self):
        """Retrieve the dictionary __objects."""
        return FileStorage.__objects

    def save(self):
        """Serialize __objects to the JSON file __file_path."""
        all_objs_in_dic = FileStorage.__objects
        obj_dict = {obj: all_objs_in_dic[obj].to_dict() for obj in all_objs_in_dic.keys()}
        with open(FileStorage.__file_path, "w") as f:
            json.dump(obj_dict, f)

    def reload(self):
        """Deserialize existing JSON file __file_path to python __objects."""
        try:
            with open(FileStorage.__file_path) as f:
                obj_dict = json.load(f)
                for o in obj_dict.values():
                    cls_name = o["__class__"]
                    del o["__class__"]
                    self.new(eval(cls_name)(**o))
        except Exception:
            pass