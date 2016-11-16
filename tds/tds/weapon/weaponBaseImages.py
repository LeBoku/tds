import pygame
import pygame.draw
import pygame.gfxdraw

from pygameUtil import imageHelper

def spear():
	color = (0,0,0)
	spearHeight = 25
	spearWidth = 1
	spearImage = imageHelper.createAlphaSurface((3, spearHeight))
	pygame.draw.rect(spearImage, color, pygame.Rect((0,0), (spearWidth, spearHeight)))

	return spearImage