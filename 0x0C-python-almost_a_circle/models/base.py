#!/usr/bin/python3
"""
containes a class called Base
"""


class Base:
    """
    a class called Base

    Attributes
    ----------
    __nb_objects: initialized to 0; a counter
    """
    __nb_objects = 0
    def __init__(self, id=None):
        """
        Parameters
        ---------
        id: int
            identification which is unique
        """
        if id is not None:
            self.id = id
        else:
           Base.__nb_objects += 1
           self.id = Base.__nb_objects
    @staticmethod
    def to_json_string(list_dictionaries):
        """converts to json"""
        import json
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        else:
            return json.dumps(list_dictionaries)
    @classmethod
    def save_to_file(cls, list_objs):
        import json
        filename = cls.__name__ + ".json"
        arr = []
        if list_objs is not None:
            for i in list_objs:
                arr.append(cls.to_dictionary(i))    
        with open(filename, mode="w", encoding="utf-8") as f:               
            f.write(cls.to_json_string(arr))
