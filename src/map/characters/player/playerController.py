import pygame.locals
import pygame.mouse
from pygame.math import Vector2

from map.characters.characterController import CharacterController
from map import weapons
from pygameUtil.eventHandling import EventListener, EventHandler

from store.enums import MoveTypes, CharacterParts, AttackMilestones


class PlayerController(CharacterController):
	def __init__(self, map):
		super().__init__(map)
		self.eventHandler = EventHandler.get()

		self.movementKeys = {
			pygame.locals.K_w: ["y", -1],
			pygame.locals.K_d: ["x", 1],
			pygame.locals.K_s: ["y", 1],
			pygame.locals.K_a: ["x", -1]
		}

	@property
	def isRunning(self):
		return not self.eventHandler.isKeyDown(pygame.locals.K_LSHIFT)

	@isRunning.setter
	def isRunning(self, value):
		pass

	def loopCall(self):
		super().loopCall()

		self.updateAngle()
		self.updateMovement()

		if self.isAttacking:
			isColliding = self.weapon.isCollidingWithSomething()
			if isColliding:
				print(isColliding)

	def updateMovement(self):
		movement = self.getMovementVector()

		if movement.length():
			self.startMoveAnimation()

			movement.scale_to_length(self.speed)
			oldCord = Vector2(self.coord)
			self.coord += movement
				
			if self.isCollidingWithSomething():
				self.coord = oldCord
		else:
			self.stopMoveAnimation()

	def getMovementVector(self):
		pressedKeys = self.eventHandler.orderKeysByLoopsDown(self.movementKeys.keys())
		forwardMovement = Vector2(0, 0)

		if len(pressedKeys) > 0:
			movement = {"x":0,"y":0}
			for key in reversed(pressedKeys):
				movement[self.movementKeys[key][0]] = self.movementKeys[key][1]

			forwardMovement = Vector2(movement["x"], movement["y"])

		return forwardMovement

	def updateAngle(self):
		mousePosVector = Vector2(pygame.mouse.get_pos())
		self.angle = (mousePosVector - self.coord).angle_to(Vector2(0, -1)) % 360

	def setUpEventListeners(self):
		super().setUpEventListeners()
		self.registerCombat()

	def registerCombat(self):
		@EventListener(pygame.locals.MOUSEBUTTONDOWN, button=1)
		def startAttack(event):
			self._startOrQAttack(MoveTypes.attackFast)

		@EventListener(pygame.locals.MOUSEBUTTONDOWN, button=3)
		def startAttack(event):
			self._startOrQAttack(MoveTypes.attackWide)

	def setUpSubEntities(self):
		super().setUpSubEntities()
		self.weapon = weapons.LongSword(CharacterParts.weapon, self.rightHand, self)

	def _startOrQAttack(self, attackType):
		activeMove = self.getActiveAttackMove()
		if activeMove is None:
			self._startAttack(attackType)

		elif activeMove.hasPassedMileStone(AttackMilestones.attacked):
			activeMove.listenForEnd(lambda: self._startAttack(attackType))

	def _startAttack(self, attackType):
		move = self.moveSetController.getMove(attackType)
		move.start()
