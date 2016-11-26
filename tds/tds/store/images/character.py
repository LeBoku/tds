import pygame
import pygame.gfxdraw

from store.images import util

def player():
	img = util.createAlphaSurface((5, 5))
	img.fill((0,0,0))
	#pygame.gfxdraw.filled_polygon(charImage, [(5,1), (8,10), (2,10)], (0,0,0))
	

	return img

def hand():
	img = util.createAlphaSurface((2, 2))
	img.fill((0,0,0))

	return img