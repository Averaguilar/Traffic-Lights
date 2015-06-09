"""A module for storing constants in the traffic light simulator."""
DISCOUNT = 0.9

ROAD_LENGTH = 102
CROSSING_LOCATION = ROAD_LENGTH / 2  - 1

NUM_LANES = 2

SCREEN_WIDTH = 510
SCREEN_HEIGHT = 510

# roads are 5 pixels wide, and the length of the screen
# Each spot in a road is 5 pixels by 5 pixels.
LANE_WIDTH = 5
ROAD_WIDTH = LANE_WIDTH * NUM_LANES
ROAD_HEIGHT = SCREEN_HEIGHT
ROAD_NORTH_LEFT = 250
ROAD_NORTH_TOP = 0
ROAD_EAST_LEFT = 0
ROAD_EAST_TOP = 250

SPOT_SIZE = 5

CAR_IMAGE = './Images/car.png'
LIGHT_IMAGE_RED = './Images/red.png'
LIGHT_IMAGE_GREEN = './Images/green.png'
