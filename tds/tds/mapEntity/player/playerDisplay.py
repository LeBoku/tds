import pygame
import pygame.gfxdraw
import pygame.draw

from mapEntity.MapEntityDisplay import MapEntityDisplay
from store.images import character

class PlayerDisplay(MapEntityDisplay):
	def setUpBaseImage(self):
		super().setUpBaseImage()
		
		self.baseImage = character.player()