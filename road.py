"""This module defines the road class."""

import constants
import random
import spot
import distributions
import traffic_light

class Road(object):
    """A class representing a road. A road holds traffic lights and cars."""
    def __init__(self, color, distribution):
        """Initialize the road with length constants.ROAD_LENGTH"""
        self._spots = [spot.Spot() for _ in xrange(0, constants.ROAD_LENGTH)]
        self._spots[constants.LIGHT_LOCATION].add_light(color)
        self._steps = 0
        self._num_queued = 0
        self._car_distro = distributions.Probability()
        self._distribution = distribution

    def update(self):
        """Update the cars on the road to move in a time increment."""
        self._spots[constants.ROAD_LENGTH - 1].remove_car()

        for i in xrange(constants.ROAD_LENGTH - 2, -1, -1):
            if (i == constants.LIGHT_LOCATION and
                    self._spots[constants.LIGHT_LOCATION].light_color() ==
                    traffic_light.TrafficLight.RED):
                if self._spots[i].has_car():
                    self._num_queued += 1
                continue

            if self._spots[i].has_car() and not self._spots[i + 1].has_car():
                self._spots[i].move_car(self._spots[i + 1])
            elif self._spots[i].has_car():
                self._num_queued += 1

        if not self._spots[0].has_car():
            self.create_car(self._distribution)
        self._steps += 1

    def has_car(self, i):
        """Returns whether spot i on the road has a car."""
        return self._spots[i].has_car()

    def light_color(self):
        """Returns the color of the traffic light on this road."""
        return self._spots[constants.LIGHT_LOCATION].light_color()

    def light_location(self):
        """Returns the location of the traffic light on this road."""
        return constants.LIGHT_LOCATION

    def flip_color(self):
        """Change the color of the traffic lights on this road."""
        self._spots[constants.LIGHT_LOCATION].flip_color()

    def get_amount_queued(self):
        """Return the total number of steps queued over the whole road"""
        return self._num_queued

    def reset_queueing(self):
        """Reset the queueing counters for each spot"""
        self._num_queued = 0

    def create_car(self, distribution):
        """Return true if a car should be created"""
        if distribution == distributions.Probability.STANDARD:
            if self._steps % (random.randint(0, 9) + 5) == 0:
                self._spots[0].add_car()
        elif self._car_distro.get_value(distribution):
            self._spots[0].add_car()
