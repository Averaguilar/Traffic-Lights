import pygame
#import car
#import road
#import TrafficLight
import constants as c

class Viewer():

    def initialise(self):
        pygame.init()
        self.screen = pygame.display.set_mode((c.SCREEN_WIDTH, c.SCREEN_HEIGHT))

        # initialise background to grey
        self.screen.fill(150,150,150)

        return self.screen

    def update_roads(self, road1, road2):
        color = pygame.Color(0, 255, 255, 255)
        # draw north road. We demand that road1 be the north road
        pygame.draw.polygon(self.screen, color, 
                [(c.ROAD_NORTH_TOP_X, c.ROAD_NORTH_TOP_Y), 
                (c.ROAD_NORTH_BOT_X, c.ROAD_NORTH_TOP_Y), 
                (c.ROAD_NORTH_BOT_X, c.ROAD_NORTH_BOT_Y), 
                (c.ROAD_NORTH_TOP_X, c.ROAD_NORTH_BOT_Y), 
                (c.ROAD_NORTH_TOP_X, c.ROAD_NORTH_TOP_Y)], width=0)

        # update that road
        __update_road(road1)

        # draw east road
        pygame.draw.polygon(self.screen, color, 
                [(c.ROAD_EAST_TOP_X, c.ROAD_EAST_TOP_Y), 
                (c.ROAD_EAST_BOT_X, c.ROAD_EAST_TOP_Y), 
                (c.ROAD_EAST_BOT_X, c.ROAD_EAST_BOT_Y), 
                (c.ROAD_EAST_TOP_X, c.ROAD_EAST_BOT_Y), 
                (c.ROAD_EAST_TOP_X, c.ROAD_EAST_TOP_Y)], width=0)

        # update that road
        __update_road(road2)

        # update display changes
        pygame.display.flip()

    def __update_road(self, road):
        # draw anything on the road
        for o in road:
            x,y = o.get_location()
            images = o.get_images()
            if len(images) > 1:
                if len(images) != 0 or images[0] != None:
                    #TODO(Dave): Modify coords to render car and lights in same box
                    self.screen.blit(images[0], (x,y)) 
            if len(images) == 2:
                    self.screen.blit(images[1], (x,y))
