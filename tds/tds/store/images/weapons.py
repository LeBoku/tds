import pygame
import pygame.draw
import pygame.gfxdraw

from store.images import util

def spear():
	color = (0,0,0)
	spearHeight = 35
	spearWidth = 1

	spearImage = util.createAlphaSurface((3, spearHeight))
	pygame.draw.rect(spearImage, color, pygame.Rect((1,0), (spearWidth, spearHeight)))
	pygame.draw.rect(spearImage, color, pygame.Rect((0,3), (5, 2)))

	return spearImage