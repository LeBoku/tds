import pygame
import pygame.image

def createAlphaSurface(dimensions):
	surface = pygame.Surface(dimensions).convert_alpha()
	surface.fill((255,255,255,0))
	
	return surface

def loadImage(path, isTransparent=True):
	img = pygame.image.load(path)
	if isTransparent:
		img = img.convert_alpha()
	else:
		img = img.convert()
	return img