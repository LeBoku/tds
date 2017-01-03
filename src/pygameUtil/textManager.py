import pygame
import pygame.font

pygame.font.init()


def renderText(text, color=(0,0,0), size=15):
	font = pygame.font.SysFont("tmp", size)
	return font.render(str(text),True, color)