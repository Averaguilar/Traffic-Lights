"""This module holds the implementation of the Intersection class."""

import copy
import distributions
import road
import state
import traffic_light

class Intersection(object):
    """Models the state of all roads and their interaction."""
    def __init__(self):
        """Initialize the intersection with two roads."""
        self._roads = [road.Road(traffic_light.TrafficLight.RED,
                           distributions.Probability.STANDARD),
                 road.Road(traffic_light.TrafficLight.GREEN,
                           distributions.Probability.STANDARD)]
        self._switch_time = 0
        self._to_switch = None

    def get_state(self):
        """Returns the state of the intersection used by the learning module."""
        return state.State(self._roads, self._switch_time)

    def get_performance(self):
        """Gets the number of cars waiting since it was last called."""
        performance = 0
        for curr_road in self._roads:
            performance += curr_road.get_amount_queued()
            curr_road.reset_queueing()
        return performance

    def update_state(self, switch_lights):
        """Update the state of the roads and potentially switches the lights."""
        if switch_lights:
            assert self._switch_time == 0
            for curr_road in self._roads:
                if curr_road.light_color() == traffic_light.TrafficLight.GREEN:
                    curr_road.flip_color()
                else:
                    self._to_switch = curr_road
            self._switch_time = 3 
        elif self._switch_time != 0:
            self._switch_time -= 1
            if self._switch_time == 1:
                self._to_switch.flip_color()

        for curr_road in self._roads:
            curr_road.update()

    def get_roads(self):
        """Get a copy of the roads in the intersection."""
        return copy.deepcopy(self._roads)
