"""This module defines the class for different car distributions."""

import numpy as np
import math
import random

class Probability(object):
    """This class contains functions for different probability distributions."""
    GAUSSIAN = 0
    POISSON = 1
    UNIFORM = 2
    STANDARD = 3

    _POISSON_MEAN = 5 
    _GAUSSIAN_MEAN = 10
    _GUASSIAN_VAR = 1
    _UNIFORM_MEAN = 0.1

    def __init__(self):
        """Initialise the class"""
        self.prob = 0

    def get_value(self, distribution):
        """Given a distribution, return whether the event occurred or not"""
        # Get the chance of the event occurring, generate a random number between 1 and 100, and
        # return 1 if less than, 0 if greater than
        return self.get_probability(distribution)

    def get_probability(self, distribution):
        """Returns the percentage of an event occurring under the given distribution"""
        # A random number is generated and used as input to the distribution
        # the chance is returned as a percentage
        if distribution == self.GAUSSIAN:
            variable = np.random.normal(self._GAUSSIAN_MEAN, self._GUASSIAN_VAR, None)
            prob = (1/(2*np.pi*self._GUASSIAN_VAR**2))*np.exp(-1*((variable - self._GAUSSIAN_MEAN)**2)/(2*self._GUASSIAN_VAR**2))
            if random.randint(0, 100) <= prob*100:
                return True
        elif distribution == self.POISSON:
            variable = np.random.poisson(self._POISSON_MEAN, None)
            prob = np.exp(-1*self._POISSON_MEAN)*(np.power([self._POISSON_MEAN], variable)[0])/np.math.factorial(variable)
            if random.randint(0, 100) <= prob*100:
                return True
        elif distribution == self.UNIFORM:
            variable = 100*self._UNIFORM_MEAN
            prob = variable
            if random.randint(0,100) <= prob:
                return True
        return False
