import pygame
import pygame.gfxdraw

from store.images import util

def player():
	charImage = util.createAlphaSurface((10, 10))
	pygame.gfxdraw.filled_polygon(charImage, [(5,1), (8,10), (2,10)], (0,0,0))

	return charImage