import pygame.transform

from map.base.displayHandler import DisplayHandler


class MapEntityDisplay(DisplayHandler):
	def display(self):
		angle = self.controller.angle
		if self.controller.offset is not None:
			angle += self.controller.offset.angle

		display = super().display()

		if display is not None:
			if angle != 0:
				return pygame.transform.rotozoom(display, angle, 1)
			else:
				return display