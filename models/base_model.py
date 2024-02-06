#!/usr/bin/python3
from uuid import uuid4 as uu
from datetime import datetime as dt

class BaseModel:
    def __init__(self, *args, **kwarge):
        self.id = str(uu())
        if kwargs:
            for key, value in kwargs.items():
                if key != 'class':
                    if key in ['created_at', 'updated_at']:
                        value = datetime.strptime(value, '%Y-%m-%dT%H:%M:%S.%f')
                    setattr(self, key, value)
        self.created_at = dt.now()
        self.updated_at = dt.now()
    
    def __repr__(self):
        return f'[{self.__class__.__name__}] ({self.id}) {self.__dict__}'
    
    def save(self):
        self.updated_at = dt.now()
        
    def to_dict(self):
        dict_copy = self.__dict__.copy()
        dict_copy["__class__"] = self.__class__.__name__
        dict_copy["created_at"] = self.created_at.isoformat()
        dict_copy["updated_at"] = self.updated_at.isoformat()
        return dict_copy
