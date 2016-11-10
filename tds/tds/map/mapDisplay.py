import pygame

from base.displayHandler import DisplayHandler

class MapDisplay(DisplayHandler):
	def __init__(self):
		self.backgroundColor = 255, 255, 255
		super().__init__()

	def display(self, display):
		rect = display.get_size()
		mapDisplay = pygame.surface.Surface(rect)
		mapDisplay.fill(self.backgroundColor)
		return mapDisplay
