#!/usr/bin/python3
"""Defines the Amenity class that inherits from BaseModel."""
from models.base_model import BaseModel


class Amenity(BaseModel):
    """Amenity class"""
    
    def __init__(self, *args, **kwargs):
        """Initialize Amenity instance"""
        super().__init__(*args, **kwargs)
        self.name = kwargs.get('name', "")
