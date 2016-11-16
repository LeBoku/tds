import pygame
import pygame.gfxdraw
import pygame.draw

from base.displayHandler import DisplayHandler

class PlayerDisplay(DisplayHandler):
	def display(self):
		display = pygame.Surface((10, 10)).convert_alpha()
		display.fill((255,255,255,0))
		
		pygame.gfxdraw.filled_polygon(display, [(5,1), (8,10), (2,10)], (0,0,0))
		
		return display 