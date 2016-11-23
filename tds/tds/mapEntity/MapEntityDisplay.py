import pygame.transform

from base.displayHandler import DisplayHandler
from pygame.math import Vector2

class MapEntityDisplay(DisplayHandler):
	def display(self):
		return pygame.transform.rotozoom(super().display(), self.controller.angle.angle_to(Vector2(0, -1)), 1)