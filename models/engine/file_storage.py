#!/usr/bin/python3
"""This module defines a class to manage file storage for hbnb clone"""
import json


class FileStorage:
    """This class manages storage of hbnb models in JSON format"""
    __file_path = 'file.json'
    __objects = {}

    def all(self, cls=None):
        """
        Returns the list of objects of one type of class.
        If cls is None, returns all objects.
        """
        if cls is None:
            return list(self.__objects.values())
        return [obj for obj in self.__objects.values()
                if isinstance(obj, cls)]

    def new(self, obj):
        """Adds new object to storage dictionary"""
        key = obj.__class__.__name__ + '.' + obj.id
        self.__objects[key] = obj

    def save(self):
        """Saves storage dictionary to file"""
        with open(self.__file_path, 'w') as f:
            serialized_objects = {key: obj.to_dict()
                                  for key, obj in self.__objects.items()}
            json.dump(serialized_objects, f)

    def reload(self):
        """Loads storage dictionary from file"""
        from models.base_model import BaseModel
        from models.user import User
        from models.place import Place
        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        from models.review import Review

        classes = {
            'BaseModel': BaseModel, 'User': User, 'Place': Place,
            'State': State, 'City': City, 'Amenity': Amenity,
            'Review': Review
        }
        try:
            with open(self.__file_path, 'r') as f:
                serialized_objects = json.load(f)
                for key, value in serialized_objects.items():
                    class_name, obj_id = key.split('.')
                    obj_class = classes[value['__class__']]
                    self.__objects[key] = obj_class(**value)
        except FileNotFoundError:
            pass

    def delete(self, obj=None):
        """Deletes obj from __objects if it exists"""
        if obj is not None:
            key = obj.__class__.__name__ + '.' + obj.id
            self.__objects.pop(key, None)
