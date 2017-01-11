import pygame


def createAlphaSurface(dimensions, color=(255, 255, 255, 0)):
	surface = pygame.Surface(dimensions).convert_alpha()
	surface.fill(color)

	return surface


def createSurface(dimensions, color=(255, 255, 255)):
	surface = pygame.Surface(dimensions).convert()
	surface.fill(color)

	return surface
