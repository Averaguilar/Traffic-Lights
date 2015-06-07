"""This module defines the viewer class."""

import pygame
import spot
import road
import traffic_light
import constants as c

class Viewer():
    """A class representing the viewer, which renders the simulation in a window"""
    def __init__(self):
        """Initialise pygame, load all image files, draw the background"""
        pygame.init()
        self.screen = pygame.display.set_mode((c.SCREEN_WIDTH, c.SCREEN_HEIGHT))

        # initialise background to grey
        self.screen.fill(150, 150, 150)

        self.car = pygame.image.load(c.CAR_IMAGE).convert()
        self.red_light = pygame.image.load(c.LIGHT_IMAGE_RED).convert()
        self.green_light = pygame.image.load(c.LIGHT_IMAGE_GREEN).convert()

    def update_roads(self, road1, road2):
        """Render the roads and draw new car positions and light states for each step"""
        color = pygame.Color(0, 255, 255, 255)
        # draw north road. We demand that road1 be the north road
        pygame.draw.polygon(self.screen, color,
                            [(c.ROAD_NORTH_TOP_X, c.ROAD_NORTH_TOP_Y),
                             (c.ROAD_NORTH_BOT_X, c.ROAD_NORTH_TOP_Y),
                             (c.ROAD_NORTH_BOT_X, c.ROAD_NORTH_BOT_Y),
                             (c.ROAD_NORTH_TOP_X, c.ROAD_NORTH_BOT_Y),
                             (c.ROAD_NORTH_TOP_X, c.ROAD_NORTH_TOP_Y)], width=0)

        # update that road
        self._update_north_road(road1)

        # draw east road
        pygame.draw.polygon(self.screen, color,
                            [(c.ROAD_EAST_TOP_X, c.ROAD_EAST_TOP_Y),
                             (c.ROAD_EAST_BOT_X, c.ROAD_EAST_TOP_Y),
                             (c.ROAD_EAST_BOT_X, c.ROAD_EAST_BOT_Y),
                             (c.ROAD_EAST_TOP_X, c.ROAD_EAST_BOT_Y),
                             (c.ROAD_EAST_TOP_X, c.ROAD_EAST_TOP_Y)], width=0)

        # update that road
        self._update_east_road(road2)

        # update display changes
        pygame.display.flip()

    def _update_north_road(self, curr_road):
        """Draw the north-bound traffic, and the light"""
        # Draw in the traffic light
        x_coord = c.ROAD_NORTH_TOP_X
        y_coord = curr_road.light_location() * c.SPOT_SIZE
        image = self.red_light if road.light_color() == TrafficLight.RED else self.green_light
        self.screen.blit(image, (x_coord, y_coord))

        # draw cars onto the road
        i = 0
        while i < c.ROAD_LENGTH:
            y_coord = i * c.SPOT_SIZE
            if curr_road.has_car(i):
                self.screen.blit(self.car, (x_coord+2, y_coord+3))

            i += 1

    def _update_east_road(self, curr_road):
        """Draw the east-bound traffic, and the light"""
        # Draw in the traffic light
        y_coord = c.ROAD_EAST_BOT_Y
        x_coord = curr_road.light_location() * c.SPOT_SIZE
        image = self.red_light if r.light_color() == TrafficLight.RED else self.green_light
        self.screen.blit(image, (x_coord, y_coord))

        # draw cars onto the road
        i = 0
        while i < c.ROAD_LENGTH:
            x_coord = i * c.SPOT_SIZE
            if curr_road.has_car(i):
                self.screen.blit(self.car, (x_coord+3, y_coord-2))

            i += 1
