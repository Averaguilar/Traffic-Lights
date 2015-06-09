"""This module holds a class defining a state in the Q-learning algorithm"""
import traffic_light

class State(object):
    """The state of the roads for our Q-learning algorithm.

    Note that a state is immutable. A new state should be created if need be.
    """
    def __init__(self, roads, wait_time):
        """Create a new state according to the roads and traffic light wait."""
        self._closest = []
        for road in roads:
            start = road.light_location() + 1
            i = 0
            while i < 9:
                if road.has_car(start - i):
                    break
                i += 1
            self._closest.append(i)
        for i in xrange(0, len(roads)):
            if roads[i].light_color() == traffic_light.TrafficLight.GREEN:
                self._green_road = i
        self._wait_time = wait_time

    def __eq__(self, other):
        """Returns whether two states are the same."""
        for i in xrange(len(self._closest)):
            if self._closest[i] != other.closest_car(i):
                return False
        return (self._green_road == other.green_road() and
                self._wait_time == other.wait_time())

    def __hash__(self):
        """Returns a hash of the state."""
        hash_list = list(self._closest)
        hash_list.append(self._green_road)
        hash_list.append(self._wait_time)
        return hash(tuple(hash_list))

    def green_road(self):
        """Returns the road number of the road with a green light."""
        return self._green_road

    def red_road(self):
        """Returns the road number of the road with a red light."""
        return (self._green_road + 1) % 2

    def closest_car(self, road_num):
        """Returns the distance of the closest car from the intersection."""
        return self._closest[road_num]

    def wait_time(self):
        """Returns the number of timesteps before a light switch can occur."""
        return self._wait_time
