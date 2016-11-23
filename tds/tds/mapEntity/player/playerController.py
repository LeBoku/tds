import pygame.locals
import pygame.mouse
from pygame.math import Vector2

from mapEntity.character.characterController import CharacterController
from .playerDisplay import PlayerDisplay

from pygameUtil.EventHandling import EventListener
from pygameUtil import math_



class PlayerController(CharacterController):
	def __init__(self, map):
		super().__init__(map)
		self.speed = 5

	def setUpDisplayHandler(self):
		self.displayHandler = PlayerDisplay(self)

	def display(self):
		mousePosVector = Vector2(pygame.mouse.get_pos())
		self.angle = mousePosVector - self.coord
		return super().display()

	def registerEvents(self):
		super().registerEvents()
		self.registerMovement()

	def registerMovement(self):
		@EventListener("KEY_IS_DOWN", key=pygame.locals.K_w)
		def li(event):
			movement = Vector2(0, -5)
			movement.scale_to_length(5)
			self.coord += movement

		@EventListener("KEY_IS_DOWN", key=pygame.locals.K_d)
		def li(event):
			movement = Vector2(5, 0)
			movement.scale_to_length(5)
			self.coord += movement

		@EventListener("KEY_IS_DOWN", key=pygame.locals.K_s)
		def li(event):
			movement = Vector2(0, 5)	
			movement.scale_to_length(5)
			self.coord += movement
	
		@EventListener("KEY_IS_DOWN", key=pygame.locals.K_a)
		def li(event):
			movement = Vector2(-5, 0)
			movement.scale_to_length(5)
			self.coord += movement
