#!/usr/bin/python3
from models import storage
from uuid import uuid4 as uu
from datetime import datetime as dt

class BaseModel:
    def __init__(self, *args, **kwargs):
        self.id = str(uu())
        if kwargs:
            for key, value in kwargs.items():
                if key != '__class__':
                    if key == "created_at" or key == "updated_at":
                        value = dt.now()
                        setattr(self, key, value)
        else:
            self.created_at = dt.now()
            self.updated_at = dt.now()
            storage.new(self)
    
    def __repr__(self):
        return f'[{self.__class__.__name__}] ({self.id}) {self.__dict__}'
    
    def save(self):
        self.updated_at = dt.now()
        storage.save()
        
    def to_dict(self):
        dict_copy = self.__dict__.copy()
        dict_copy["__class__"] = self.__class__.__name__
        dict_copy["created_at"] = self.created_at.isoformat()
        dict_copy["updated_at"] = self.updated_at.isoformat()
        return dict_copy
