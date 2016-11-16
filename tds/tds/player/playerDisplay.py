import pygame
import pygame.gfxdraw
import pygame.draw

from character.characterDisplay import CharacterDisplay


class PlayerDisplay(CharacterDisplay):
	def setUpBaseImage(self):
		super().setUpBaseImage()

		display = pygame.Surface((10, 10)).convert_alpha()
		display.fill((255,255,255,0))
		
		pygame.gfxdraw.filled_polygon(display, [(5,1), (8,10), (2,10)], (0,0,0))
		
		self.baseImage = display 
