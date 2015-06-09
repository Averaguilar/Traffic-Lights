"""A module for storing constants in the traffic light simulator."""
DISCOUNT = 0.9

ROAD_LENGTH = 101
LIGHT_LOCATION = (ROAD_LENGTH / 2) - 1

SCREEN_WIDTH = 510
SCREEN_HEIGHT = 510

# roads are 5 pixels wide, and the length of the screen
# Each spot in a road is 5 pixels by 5 pixels.
ROAD_NORTH_TOP_X = 250
ROAD_NORTH_TOP_Y = 0
ROAD_NORTH_BOT_X = 255
ROAD_NORTH_BOT_Y = 510

ROAD_EAST_TOP_X = 0
ROAD_EAST_TOP_Y = 250
ROAD_EAST_BOT_X = 510
ROAD_EAST_BOT_Y = 255

SPOT_SIZE = 5

CAR_IMAGE = './Images/car.png'
LIGHT_IMAGE_RED = './Images/red.png'
LIGHT_IMAGE_GREEN = './Images/green.png'
