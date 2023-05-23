#!usr/bin/python3
""" module defining the BaseModel class """

import uuid
from datetime import datetime
from models import storage

class BaseModel:
    """ class BaseModel that defines all common
    attributes/methods for other classes
    """
    def __init__(self, *args, **kwargs):
        """ initializes the base instance """
        if kwargs is not None and kwargs != {}:
            for k, v in kwargs:
                if k == "created_at":
                    self.__dict__["created_at"] = datetime.strptime(kwargs["created_at"], "%Y-%m-%dT%H:%M:%S.%f")
                elif k == "updated_at":
                    self.__dict__["updated_at"] = datetime.strptime(kwargs["updated_at"], "%Y-%m-%dT%H:%M:%S.%f")
                else:
                    self.__dict__[k] = kwargs[k]
        else:
            self.id = str(uuid.uuid4()())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)

    def __str__(self):
        """ prints: [<class name>] (<self.id>) <self.__dict__> """
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        """updates the public instance attribute updated_at
        with the current datetime"""
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """ returns a dictionary containing all
        keys/values of __dict__ of the instance """
        my_dict = self.__dict__.copy()
        my_dict["__class__"] = self.__class__.__name__
        my_dict["created_at"] = my_dict["created_at"].isoformat()
        my_dict["updated_at"] = my_dict["updated_at"].isoformat()
        return my_dict