import pygame

from base.displayHandler import DisplayHandler
from config import resolution

class MapDisplay(DisplayHandler):
	def __init__(self, controller):
		self.backgroundColor = 255, 255, 255
		self.baseDisplay =  pygame.surface.Surface(resolution)
		super().__init__(controller)

	def display(self):
		mapDisplay = self.baseDisplay.copy()
		mapDisplay.fill(self.backgroundColor)

		return mapDisplay
