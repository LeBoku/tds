import pygame
import pygame.draw
import pygame.gfxdraw

from store.images import util


def spear():
	color = (0,0,0)
	spearHeight = 60
	spearWidth = 2

	spearImage = util.createAlphaSurface((5, spearHeight))
	pygame.draw.rect(spearImage, color, pygame.Rect((2, 0), (spearWidth, spearHeight)))
	pygame.draw.rect(spearImage, color, pygame.Rect((1, 10), (4, 2)))

	return spearImage
