import pygame
import pygame.gfxdraw
import pygame.draw

from character.characterDisplay import CharacterDisplay
from pygameUtil import imageHelper

class PlayerDisplay(CharacterDisplay):
	def setUpBaseImage(self):
		super().setUpBaseImage()

		display = imageHelper.createAlphaSurface((10, 10))
		pygame.gfxdraw.filled_polygon(display, [(5,1), (8,10), (2,10)], (0,0,0))
		
		self.baseImage = display 
