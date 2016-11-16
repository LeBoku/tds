import pygame.transform

from base.displayHandler import DisplayHandler

class MapEntityDisplay(DisplayHandler):
	def display(self):
		return pygame.transform.rotozoom(super().display(), self.controller.angle, 1)