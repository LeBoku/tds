import pygame
import pygame.gfxdraw

from store.images import util

def player():
	img = util.createAlphaSurface((5, 2))
	img.fill((0,0,0))
	
	return img

def hand():
	img = util.createAlphaSurface((1, 1))
	img.fill((0,0,0))

	return img