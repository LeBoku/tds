import pygame

def createAlphaSurface(dimensions):
	surface = pygame.Surface(dimensions).convert_alpha()
	surface.fill((255,255,255,0))
	
	return surface
