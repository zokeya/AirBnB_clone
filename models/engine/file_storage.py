#!/usr/bin/python3
"""
module that defines a FileStorage class
"""
import json
import os
import datetime

class FileStorage:
    """ class that  that serializes instances to a
    JSON file and deserializes JSON file to instances"""
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """ returns the dictionary __objects """
        return self.__objects

    def new(self, obj):
        """ sets in __objects the obj
        with key <obj class name>.id """
        key = f"{obj.__class__.__name__}.{obj.id}"
        self.__objects[key] = obj

    def save(self):
        """serializes __objects to the JSON file (path: __file_path)"""
        with open(self.__file_path, "w", encoding="utf-8") as f:
            tmp = {k: v.to_dict() for k, v in self.__objects.items()}
            json.dump(tmp, f)

    def reload(self):
        """deserializes the JSON file to __objects
        only if the JSON file (__file_path) exists
        otherwise, do nothing
        If the file doesn’t exist, no exception should be raised"""
        if not os.path.isfile(self.__file_path):
            return

        with open(self.__file_path, "w", encoding="utf-8") as f:
            obj_dict = json.load(f)
            for k, v in obj_dict.items():
                cls = v["__class_"]
                self.__objects[k] = self.__classes[cls](**v)