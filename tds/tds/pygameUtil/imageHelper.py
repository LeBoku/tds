import pygame
import pygame.image

def loadImage(path, isTransparent=True):
	img = pygame.image.load(path)
	if isTransparent:
		img = img.convert_alpha()
	else:
		img = img.convert()
	return img