import pygame
#import car
#import road
#import TrafficLight

SCREEN_WIDTH = 510
SCREEN_HEIGHT = 510

# roads are 5 pixels wide, and the length of the screen
ROAD_NORTH_TOP_X = 250
ROAD_NORTH_TOP_Y = 0
ROAD_NORTH_BOT_X = 255
ROAD_NORTH_BOT_Y = 510

ROAD_EAST_TOP_X = 250
ROAD_EAST_TOP_Y = 0
ROAD_EAST_BOT_X = 255
ROAD_EAST_BOT_Y = 510

class Viewer():

	def initialise():
		pygame.init()
		self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

		# initialise background to grey
		self.screen.fill(150,150,150)

		return self.screen

	def updateRoads(road1, road2):
		color = pygame.Color(0, 255, 255, 255)
		# draw north road. We demand that road1 be the north road
		pygame.draw.polygon(self.screen, color, [(ROAD_NORTH_TOP_X, ROAD_NORTH_TOP_Y),(ROAD_NORTH_BOT_X, ROAD_NORTH_TOP_Y),(ROAD_NORTH_BOT_X, ROAD_NORTH_BOT_Y),(ROAD_NORTH_TOP_X, ROAD_NORTH_BOT_Y),(ROAD_NORTH_TOP_X, ROAD_NORTH_TOP_Y)], width=0)

		# update that road
		__updateRoad(road1)

		# draw east road
		pygame.draw.polygon(self.screen, color, [(ROAD_EAST_TOP_X, ROAD_EAST_TOP_Y),(ROAD_EAST_BOT_X, ROAD_EAST_TOP_Y),(ROAD_EAST_BOT_X, ROAD_EAST_BOT_Y),(ROAD_EAST_TOP_X, ROAD_EAST_BOT_Y),(ROAD_EAST_TOP_X, ROAD_EAST_TOP_Y)], width=0)

		# update that road
		__updateRoad(road2)

		# update display changes
		pygame.display.flip()

	def __updateRoad(road):
		# draw anything on the road
		for o in road:
			x,y = o.getLocation()
			image = o.getImage()
			self.screen.blit(image, (x,y))
