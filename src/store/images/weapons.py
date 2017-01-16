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


def longSword():
	color = (0, 0, 0)

	swordImage = util.createAlphaSurface((8, 40))
	pygame.draw.rect(swordImage, color, pygame.Rect((3, 0), (2, 40)))
	pygame.draw.rect(swordImage, color, pygame.Rect((0, 30), (8, 2)))

	return swordImage
