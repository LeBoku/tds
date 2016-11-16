import pygame
import pygame.gfxdraw

from base.displayHandler import DisplayHandler

class PlayerDisplay(DisplayHandler):
	def display(self):
		display = pygame.Surface((10, 10)).convert_alpha()
		display.fill((255,255,255,0))
		
		pygame.gfxdraw.filled_polygon(display, [(5,0), (10,10), (0,10)], (0,0,0))
		
		return display 