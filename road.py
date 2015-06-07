"""This module defines the road class."""

import constants
import random
import spot
import traffic_light

class Road(object):
    """A class representing a road. A road holds traffic lights and cars."""
    def __init__(self):
        """Initialize the road with length constants.ROAD_LENGTH"""
        self._spots = constants.ROAD_LENGTH * [spot.Spot()]
        self._spots[constants.LIGHT_LOCATION].add_light()
        self._steps = 0

    def update(self):
        """Update the cars on the road to move in a time increment."""
        self._spots[constants.ROAD_LENGTH].remove_car()

        for i in xrange(constants.ROAD_LENGTH - 2, -1, -1):
            if (i == constants.LIGHT_LOCATION and
                self._spots[constants.LIGHT_LOCATION].light_color() ==
                traffic_light.TrafficLight.RED):
                continue
            if self._spots[i].has_car() and not self._spots[i + 1].has_car():
                self._spots[i].move_car(self._spots[i + 1])

        if self._steps % (random.randint(0, 9) + 5) == 0:
            self._spots[0].add_car()

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
