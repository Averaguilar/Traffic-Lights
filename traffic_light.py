"""This module defines the class representing a traffic light."""

class TrafficLight(object):
    """This class represents a traffic light that can change state."""
    RED = 1
    GREEN = 2

    def __init__(self, color):
        """Creates a new traffic light object that is initially set to color."""
        assert color == TrafficLight.RED or color == TrafficLight.GREEN
        self._color = color

    def flip_color(self):
        """Change the color of the traffic light."""
        if self._color == TrafficLight.RED:
            self._color = TrafficLight.GREEN
        elif self._color == TrafficLight.GREEN:
            self._color = TrafficLight.RED

    def get_color(self):
        """Get the current state of the traffic light."""
        return self._color
