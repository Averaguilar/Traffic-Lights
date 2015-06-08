"""A module that defines the class for a spot along a road."""
import car
import traffic_light

class Spot(object):
    """A spot is an area along a road.

    A spot can be populated by a car or a traffic light or both.
    """

    def __init__(self):
        """Initialize an empty spot."""
        self._car = None
        self._traffic_light = None
        self._queued = 0
        self._car_moved = False

    def has_car(self):
        """Return true if a car is on this spot."""
        return self._car is not None

    def add_car(self):
        """Add a car to the spot."""
        assert self._car is None
        self._car = car.Car()

    def remove_car(self):
        """Remove the car from this spot."""
        self._car = None

    def move_car(self, destination_spot):
        """Move a car from this spot to another given spot."""
        assert self._car is not None
        self._car.move()
        destination_spot._car = self._car
        self._car = None
        self._car_moved = True

    def queue(self):
        """If there is a car and it hasn't changed"""
        if self._car != None:
            self._car_moved = False
            self._queued += 1

    def is_queued_for_step(self):
        """Increment the counter for steps queued for this spot"""
        self._queued += 1

    def get_steps_queued(self):
        """Get the number of steps this square has been queued on since last reset"""
        return self._queued

    def reset_queueing(self):
        """Reset the queueing counter"""
        self._queued = 0

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
