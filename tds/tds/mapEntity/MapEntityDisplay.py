import pygame.transform

from base.displayHandler import DisplayHandler
from pygame.math import Vector2

class MapEntityDisplay(DisplayHandler):
	def display(self):
		angle = self.controller.angle
		if self.controller.offset is not None:
			angle += self.controller.offset.angle

		return pygame.transform.rotozoom(super().display(), angle, 1)