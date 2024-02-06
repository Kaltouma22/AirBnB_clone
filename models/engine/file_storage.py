#!/usr/bin/python3
import json
import datetime as dt

class FileStorage:
    def __init__(self):
        self.__file_path = "file.json"
        self.__objects = {}
        
    def all(self):
        return FileStorage.self.__objects
    
    def new(self, obj):
        if obj:
            key = "{}.{}".format(obj.__class__.__name__, obj.id)
            FileStorage.__objects[key] = obj


    def save(self):
        data = {}
        
        for key in FileStorage.__objects:
            data[key] = FileStorage.__objects[key].to_dict()
        
        with open(FileStorage.__file_path, "w") as f:
            json.dumps(data, f)
        
    def reload(self):
        try:
            with open(FileStorage.__file_path, 'r') as file:
                returned_data = json.load(file)
            for key, value in returned_data.items():
                class_name, obj_id = key.split(".")
                cls = eval(class_name)
                obj = cls(**value)
                FileStorage.__objects[key] = obj      
        except FileNotFoundError:
            pass
   
        