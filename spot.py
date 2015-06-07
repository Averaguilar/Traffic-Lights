"""A module that defines the class for a spot along a road."""
# TODO(karl): create car module
# import car
import traffic_light

class Spot(object):
    """A spot is an area along a road.

    A spot can be populated by a car or a traffic light or both.
    """

    def __init__(self):
        """Initialize an empty spot."""
        self._car = None
        self._traffic_light = None

    def has_car(self):
        """Return true if a car is on this spot."""
        return self._car is not None

    def add_car(self):
        """Add a car to the spot."""
        assert self._car is None
        # TODO(karl): change this when car module is implemented
        self._car = True

    def remove_car(self):
        """Remove the car from this spot."""
        self._car = None

    def move_car(self, destination_spot):
        """Move a car from this spot to another given spot."""
        assert self._car is not None
        destination_spot.add_car()
        self._car = None

    def add_light(self, color):
        """Add a traffic light to this spot initially set to the given color."""
        assert self._traffic_light is None
        self._traffic_light = traffic_light.TrafficLight(color)

    def flip_color(self):
        """Flip he color of the traffic light on this spot."""
        assert self._traffic_light is not None
        self._traffic_light.flip_color()

    def light_color(self):
        """Returns the color of the traffic light on this spot."""
        assert self._traffic_light is not None
        return self._traffic_light.get_color()
