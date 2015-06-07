"""A module that defines the class for a spot along a road."""
# TODO(karl): create car module
# import car
# TODO(karl): actually use traffic light module
# import traffic_light

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

    def move_car(self, destination_spot):
        """Move a car from this spot to another given spot."""
        assert self._car is not None
        destination_spot.add_car()
        self._car = None

    def get_images(self):
        """Return the image file for the car in this spot, or None"""
        if has_car():
            return self._car.get_image()
        else:
            return None
