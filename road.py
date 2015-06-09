"""This module defines the road class."""

import constants
import distributions
import random
import spot
import traffic_light

class Road(object):
    """A class representing a road. A road holds traffic lights and cars."""
    def __init__(self, color, distribution):
        """Initialize the road with length constants.ROAD_LENGTH"""
        self._spots = [spot.Spot() for _ in xrange(0, constants.ROAD_LENGTH)]
        self._spots[constants.CROSSING_LOCATION - 1].add_light(color, 0)
        self._spots[constants.CROSSING_LOCATION + constants.NUM_LANES].add_light(color, 1)
        self._steps = 0
        self._num_queued = 0
        self._car_distro = distributions.Probability()
        self._distribution = distribution

    def update(self):
        """Update the cars on the road to move in a time increment."""
        self._spots[constants.ROAD_LENGTH - 1].remove_car(0)
        self._spots[0].remove_car(1)

        for i in xrange(constants.ROAD_LENGTH - 1):
            self._num_queued += (self._spots[constants.ROAD_LENGTH - i - 2].
                update_spot(self._spots[constants.ROAD_LENGTH - i - 1], 0))
            self._num_queued += self._spots[i + 1].update_spot(
                self._spots[i], 1)

        self.create_car(self._distribution)
        self._steps += 1

    def has_car(self, i, lane_index):
        """Returns whether spot i on the road has a car."""
        return self._spots[i].has_car(lane_index)

    def light_color(self):
        """Returns the color of the traffic light on this road."""
        return self._spots[constants.CROSSING_LOCATION - 1].light_color()

    def crossing_location(self):
        """Returns the location of the traffic light on this road."""
        return constants.CROSSING_LOCATION

    def flip_color(self):
        """Change the color of the traffic lights on this road."""
        self._spots[constants.CROSSING_LOCATION - 1].flip_color()
        self._spots[constants.CROSSING_LOCATION + constants.NUM_LANES].flip_color()

    def get_amount_queued(self):
        """Return the total number of steps queued over the whole road"""
        return self._num_queued

    def reset_queueing(self):
        """Reset the queueing counters for each spot"""
        self._num_queued = 0

    def create_car(self, distribution):
        """Return true if a car should be created"""
        for (lane_index, spot_index) in [(0, 1), (1, constants.ROAD_LENGTH - 1)]:
            if distribution == distributions.Probability.STANDARD:
                if self._steps % (random.randint(0, 9) + 5) == 0:
                    self._spots[spot_index].add_car(lane_index)
            elif self._car_distro.get_value(distribution):
                self._spots[spot_index].add_car(lane_index)
