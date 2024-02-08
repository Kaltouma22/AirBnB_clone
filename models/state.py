#!/usr/bin/python3
"""all those classes that inherit from BaseModel """
from models.base_model import BaseModel


class State(BaseModel):
    """State class"""

    def __init__(self, *args, **kwargs):
        """Initialize State instance"""
        super().__init__(*args, **kwargs)
        self.name = kwargs.get('name', '')
