#!/usr/bin/python3
"""Defines a base model class.
This class defines all common attributes/methods for other classes.
"""
# Imports
from datetime import datetime
from uuid import uuid4
import models


class BaseModel:
    """Represents the "base" for all other classes."""

    # kwargs is a dictionary
    def __init__(self, *args, **kwargs):
        """Initialize a new BaseModel/ Instance
        Args:
            id (int): Unique id for each BaseModel
            created_at: Date of object creation
            updated_at: Date of object change
        """
        # tform = "%Y-%m-%dT%H:%M:%S.%f"

        if kwargs:
            # Create from dictionary, Loop dictionary key and values
            for key, value in kwargs.items():
                # Set object attributes dynamically using setattr function
                if(key == "__class__"):
                    continue

                # Convert isoformat string date to datetime object
                if key in ("created_at", "updated_at"):
                    value = datetime.fromisoformat(value)

                setattr(self, key, value)
        else:
            self.id = str(uuid4())
            self.created_at = datetime.today()
            self.updated_at = datetime.today()
            models.storage.new(self)

    def save(self):
        """Updates the public instance attribute updated_at with
            the current datetime.
        """
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """Return a dictionary containing all keys/values of __dict__ of
            the instance
        """
        dictionary = self.__dict__.copy()
        dictionary["created_at"] = self.created_at.isoformat()
        dictionary["updated_at"] = self.updated_at.isoformat()
        dictionary["__class__"] = self.__class__.__name__
        return dictionary

    def __str__(self):
        """Return the printable representation of model"""
        return "[{}] ({}) {}" \
            .format(self.__class__.__name__, self.id, self.__dict__)
