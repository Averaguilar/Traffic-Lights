"""This module defines the viewer class."""

import constants as c
import pygame
import traffic_light

class Viewer(object):
    """A class representing the viewer, which renders the simulation in a window"""
    def __init__(self):
        """Initialise pygame, load all image files, draw the background"""
        pygame.init()
        self.screen = pygame.display.set_mode([c.SCREEN_WIDTH, c.SCREEN_HEIGHT])

        # initialise background to grey
        self.screen.fill(pygame.Color(100, 100, 100, 100))

        self.car = pygame.image.load(c.CAR_IMAGE).convert()
        self.red_light = pygame.image.load(c.LIGHT_IMAGE_RED).convert()
        self.green_light = pygame.image.load(c.LIGHT_IMAGE_GREEN).convert()

    def update_roads(self, road1, road2):
        """Render the roads for each step. road1 MUST be the north road"""
        color = pygame.Color(0, 0, 0, 0)

        pygame.draw.rect(self.screen, color,
                         pygame.Rect(c.ROAD_NORTH_LEFT, c.ROAD_NORTH_TOP,
                                     c.ROAD_WIDTH, c.ROAD_HEIGHT)) 

        # draw east road
        pygame.draw.rect(self.screen, color,
                         pygame.Rect(c.ROAD_EAST_LEFT, c.ROAD_EAST_TOP,
                                     c.ROAD_HEIGHT, c.ROAD_WIDTH))
        # update that road
        self._update_north_road(road1)
        
        # update that road
        self._update_east_road(road2)

        # update display changes
        pygame.display.flip()

    def _update_north_road(self, curr_road):
        """Draw the north-bound traffic, and the light"""
        # Draw in the traffic light
        x_coord = c.ROAD_NORTH_LEFT 
        y_coord = (curr_road.crossing_location()  - 1)* c.SPOT_SIZE
        if curr_road.light_color() == traffic_light.TrafficLight.GREEN:
            image = self.green_light
        else:
            image = self.red_light
        self.screen.blit(image, (x_coord + 1, y_coord + 3))
        self.screen.blit(image, (x_coord + 7, y_coord + 15))

        car_coord = x_coord + 1
        # draw cars onto the road
        for lane_index in xrange(c.NUM_LANES):
            for i in xrange(c.ROAD_LENGTH):
                y_coord = i * c.SPOT_SIZE
                if curr_road.has_car(i, lane_index):
                    self.screen.blit(self.car, (car_coord, y_coord + 1))
            car_coord += 5

    def _update_east_road(self, curr_road):
        """Draw the east-bound traffic, and the light"""
        # Draw in the traffic light
        y_coord = c.ROAD_EAST_TOP
        x_coord = (curr_road.crossing_location() - 1) * c.SPOT_SIZE
        if curr_road.light_color() == traffic_light.TrafficLight.GREEN:
            image = self.green_light
        else:
            image = self.red_light
        self.screen.blit(image, (x_coord + 3, y_coord + 1))
        self.screen.blit(image, (x_coord + 15, y_coord + 7))

        car_coord = y_coord + 1 
        # draw cars onto the road
        for lane_index in xrange(c.NUM_LANES):
            for i in xrange(c.ROAD_LENGTH):
                x_coord = i * c.SPOT_SIZE
                if curr_road.has_car(i, lane_index):
                    self.screen.blit(self.car, (x_coord + 2, car_coord))
            car_coord += 5
