import sys

import pygame

import pygameUtil
from pygameUtil.eventHandling import EventHandler, EventListener

from map.map.mapController import MapController

import config 

isRunning = True

display = pygame.display.set_mode(config.resolution)
clock = pygame.time.Clock()
eventHandler = EventHandler.get()

map = MapController()

def mainLoop():
	while isRunning:
		eventHandler.postCustomEvents()
		eventHandler.handleEvents()

		mapDisplay = map.display()
		
		clock.tick(config.fps)
		display.blit(mapDisplay, (0,0))
		pygame.display.update()

@EventListener(pygame.locals.QUIT)
def onClose(event):
	pygame.quit()
	sys.exit()