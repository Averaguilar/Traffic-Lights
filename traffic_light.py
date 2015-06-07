class Color:
    red = 1
    green = 2

class TrafficLight():
    def __init__(self, color):
        self._color = color

    def flip_color(self):
        if self._color == red:
            self._color = green
        elif self._color == green
            self._color = red

    def get_color(self):
        return self._color
