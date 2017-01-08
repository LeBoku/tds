import sys
import math

import pygame, pygame.locals

from pygameUtil.eventHandling import EventHandler, EventListener
from pygameUtil.textManager import renderText
from map.map.mapController import MapController

import config 

isRunning = True

display = pygame.display.set_mode(config.resolution)
clock = pygame.time.Clock()
eventHandler = EventHandler.get()

mapController = MapController()


def mainLoop():
	while isRunning:
		eventHandler.postCustomEvents()
		eventHandler.handleEvents()

		mapDisplay = mapController.display()

		clock.tick(config.fps)
		display.blit(mapDisplay, (0, 0))

		if config.showFPS:
			display.blit(renderText(round(clock.get_fps(), 2), (255, 0, 0), 25), (5, 5))

		pygame.display.update()


@EventListener(pygame.locals.QUIT)
def onClose(event):
	pygame.quit()
	sys.exit()