"""
The module provides a subclass of :class:`.GravityField` that implements a point mass gravity model.

Theory
______

*Coming Soon*

Use
___

This is a concrete implementation of a :class:`.GravityField`, therefore to use this class you simply need to initialize
it with the a valid standard gravitational parameter (mu, sometimes referred to as the "GM").  For instance, say we want
to model the gravity of the Earth as a point mass gravity field.  We could create a model for this scenario as

    >>> from ceres.constants import muEarth
    >>> from ceres.models.gravity import PointMass
    >>> earth_gravity = PointMass(muEarth)

We can now use this model to calculate the surface acceleration on Earth

    >>> from ceres.constants import rEarth
    >>> accel = earth_gravity.get_acceleration(rEarth*np.array([1,0,0]))
    >>> np.linalg.norm(accel)
    0.009820224591618645
"""

import numpy as np
from ceres.models.gravity import GravityField

class PointMass(GravityField):
    """This class provides an implementation of a point mass gravity field for calculating accelerations.

    The :class:`PointMass`
    """
    def __init__(self, mu, position=np.array([0,0,0])):
        """
        The __init__ method may be 
        """
        self._mu = mu
        self._position = position
        return

    def set_position(self,position):
        self._position = position
        return

    def get_acceleration(self,object_position):
        r_vec = object_position - self._position
        acceleration = -self._mu/(np.linalg.norm(r_vec)**3)*r_vec
        return acceleration