import sys

import pygame

import pygameUtil
import pygameUtil.EventHandling

from map.mapCtrl import MapCtrl

import config 

isRunning = True


display = pygame.display.set_mode(config.resolution)
clock = pygame.time.Clock()
eventHandler = pygameUtil.EventHandling.EventHandler.get()

map = MapCtrl()

def mainLoop():
	while isRunning:
		eventHandler.postCustomEvents()
		eventHandler.handleEvents()

		mapDisplay = map.display(display)
		
		clock.tick(config.fps)
		display.blit(mapDisplay, (0,0))
		pygame.display.update()

@pygameUtil.EventHandling.EventListener(pygame.locals.QUIT)
def onClose(event):
	pygame.quit()
	sys.exit()