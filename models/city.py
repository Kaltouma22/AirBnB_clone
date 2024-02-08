#!/usr/bin/python3
""" All those classes that inherit from BaseModel """
from models.base_model import BaseModel


class City(BaseModel):
    """City class"""

    state_id: str = ""
    name: str = ""

    def __init__(self, *args, **kwargs):
        """Initialize City instance"""
        super().__init__(*args, **kwargs)
        self.state_id = kwargs.get('state_id', "")
        self.name = kwargs.get('name', "")
