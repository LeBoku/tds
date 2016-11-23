import pygame.transform

from base.displayHandler import DisplayHandler

class MapEntityDisplay(DisplayHandler):
	def display(self):
		return pygame.transform.rotozoom(super().display(), self.controller.angle.angle_to([0, -1]), 1)