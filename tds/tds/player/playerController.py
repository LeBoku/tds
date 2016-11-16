import pygame.locals

from character.characterController import CharacterController
from player.playerDisplay import PlayerDisplay

from pygameUtil.EventHandling import EventListener

class PlayerController(CharacterController):
	def __init__(self, map):
		super().__init__(map)
		self.speed = 5
		self.displayHandler = PlayerDisplay(self)

	def registerEvents(self):
		super().registerEvents()
		
		@EventListener("KEY_IS_DOWN", key=pygame.locals.K_w)
		def onMouseDown(event):
			self.coord[1] -= self.speed		

		@EventListener("KEY_IS_DOWN", key=pygame.locals.K_d)
		def onMouseDown(event):
			self.coord[0] += self.speed

		@EventListener("KEY_IS_DOWN", key=pygame.locals.K_s)
		def onMouseDown(event):
			self.coord[1] += self.speed
	
		@EventListener("KEY_IS_DOWN", key=pygame.locals.K_a)
		def onMouseDown(event):
			self.coord[0] -= self.speed
