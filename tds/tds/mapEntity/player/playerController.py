import pygame.locals
import pygame.mouse
from pygame.math import Vector2

from mapEntity.character.characterController import CharacterController

from pygameUtil.EventHandling import EventListener, EventHandler
from pygameUtil import math_

class PlayerController(CharacterController):
	def __init__(self, map):
		super().__init__(map)
		self.speed = 5
		self.eventHandler = EventHandler.get()

		self.movementKeys = {
			pygame.locals.K_w: Vector2(0,-1),
			pygame.locals.K_d: Vector2(1,0),
			pygame.locals.K_s: Vector2(0,1),
			pygame.locals.K_a: Vector2(-1,0)
		}

	def display(self):
		self.updateAngle()
		self.updateMovement()

		print(self.isCollidingWithSomething())

		return super().display()

	def updateMovement(self):
		pressedKeys = self.eventHandler.orderKeysByLoopsDown(self.movementKeys.keys())

		if len(pressedKeys) > 0:
			forwardMovement = Vector2(0,0)
			self.startMoveAnimation()
			for key in pressedKeys:
				forwardMovement += self.movementKeys[key]
				if not forwardMovement.length() == 0:
					forwardMovement.normalize()

			if forwardMovement.length() > 0:
				forwardMovement.scale_to_length(self.speed)
				self.coord += forwardMovement

			
			

	def startMoveAnimation(self):
		move = self.moveSetController.getMove("move")
		if not move.isActive:
			move.start()

	def updateAngle(self):
		mousePosVector = Vector2(pygame.mouse.get_pos())
		self.angle = (mousePosVector - self.coord).angle_to(Vector2(0, -1)) % 360

	def registerEvents(self):
		super().registerEvents()
		self.registerCombat()

	def registerCombat(self):
		qWindow = 20
	
		@EventListener(pygame.locals.MOUSEBUTTONDOWN, button=1)
		def startAttack(event):
			move = self.moveSetController.getMove("attack_forward")
			if not move.isActive:
				move.start()
			elif move.framesLeft < qWindow:
				move.listenForEnd(lambda: move.start())
