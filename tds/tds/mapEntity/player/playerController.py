import pygame.locals
import pygame.mouse

from mapEntity.character.characterController import CharacterController
from .playerDisplay import PlayerDisplay

from pygameUtil.EventHandling import EventListener

import pygameUtil.math

class PlayerController(CharacterController):
	def __init__(self, map):
		super().__init__(map)
		self.speed = 5

	def setUpDisplayHandler(self):
		self.displayHandler = PlayerDisplay(self)

	def display(self):
		self.angle = pygameUtil.math.calcAngleBetweenPositions(self.coord, pygame.mouse.get_pos())
		return super().display()

	def registerEvents(self):
		super().registerEvents()
		self.registerMovement()

	def registerMovement(self):
		@EventListener("KEY_IS_DOWN", key=pygame.locals.K_w)
		def li(event):
			self.coord[1] -= self.speed		

		@EventListener("KEY_IS_DOWN", key=pygame.locals.K_d)
		def li(event):
			self.coord[0] += self.speed

		@EventListener("KEY_IS_DOWN", key=pygame.locals.K_s)
		def li(event):
			self.coord[1] += self.speed
	
		@EventListener("KEY_IS_DOWN", key=pygame.locals.K_a)
		def li(event):
			self.coord[0] -= self.speed
