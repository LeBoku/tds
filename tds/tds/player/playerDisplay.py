import pygame

from base.displayHandler import DisplayHandler

class PlayerDisplay(DisplayHandler):
	def display(self):
		display = pygame.Surface((5, 5))
		display.fill((0, 0, 0))
		
		return display 