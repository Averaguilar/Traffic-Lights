"""A module that defines the class for a spot along a road."""
import traffic_light

class Spot(object):
    """A spot is an area along a road.

    A spot can be populated by a car or a traffic light or both.
    """
    def __init__(self):
        """Initialize an empty spot."""
        self._cars = [False, False]
        self._traffic_lights = [None, None]

    def has_car(self, lane_index):
        """Return true if a car is on this spot."""
        return self._cars[lane_index]

    def add_car(self, lane_index):
        """Add a car to the spot."""
        self._cars[lane_index] = True

    def remove_car(self, lane_index):
        """Remove the car from this spot."""
        self._cars[lane_index] = False

    def update_spot(self, destination_spot, lane_index):
        """Move a car from this spot to another given spot."""
        if not self._cars[lane_index]:
            return 0
        elif (self._traffic_lights[lane_index] is not None and
              self._traffic_lights[lane_index].light_color() ==
              traffic_light.TrafficLight.RED):
            return 1
        elif not destination_spot.has_car(lane_index):
            self._cars[lane_index] = False
            destination_spot.add_car(lane_index)
            return 0
        else:
            return 1

    def add_light(self, color, lane_index):
        """Add a traffic light to this spot initially set to the given color."""
        assert self._traffic_lights[lane_index] is None
        self._traffic_lights[lane_index] = traffic_light.TrafficLight(color)

    def flip_color(self):
        """Flip he color of the traffic light on this spot."""
        for curr_traffic_light in self._traffic_lights:
            if curr_traffic_light is not None:
                curr_traffic_light.flip_color()

    def  light_color(self):
        """Returns the color of the traffic light on this spot."""
        for curr_traffic_light in self._traffic_lights:
            if curr_traffic_light is not None:
                return curr_traffic_light.light_color()
