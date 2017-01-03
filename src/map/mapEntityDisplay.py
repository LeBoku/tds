import pygame.transform

from map.base.displayHandler import DisplayHandler


class MapEntityDisplay(DisplayHandler):
	def display(self):
		angle = self.controller.angle
		if self.controller.offset is not None:
			angle += self.controller.offset.angle

		return pygame.transform.rotozoom(super().display(), angle, 1)