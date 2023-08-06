"""
This module provides an abstract base class (abc) for implementing gravity field models.

This abc provides a design guide for building ceres compatible gravity fields.  All user defined gravity field models
should likely subclass this class to ensure that they implement all of the required properties and methods that ceres expects
a gravity field to have.

Theory
______

*Coming Soon*

Use
___

"""

from abc import ABCMeta, abstractmethod

class GravityField(metaclass=ABCMeta):
    """
    """
    def __init__(self,mu):
        """
        """
        return

    @abstractmethod
    def get_acceleration(self, object_position):
        """
        """
        return 