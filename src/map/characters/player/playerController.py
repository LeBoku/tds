import pygame.locals
import pygame.mouse
from pygame.math import Vector2

from map.characters.characterController import CharacterController
from map.weapons import LongSword
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

	def lockMovement(self):
		self.isAttacking = True

	def unlockMovement(self):
		self.isAttacking = False

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

	def getAttack(self):
		movement = self.getMovementVector()
		if movement.length() == 0:
			movement = Vector2(0, -1)
		angle = (movement.angle_to(Vector2(0,-1)) + 360) % 360

		if 45 < angle < 135:
			attack = MoveTypes.attackRight

		elif 225 < angle < 315:
			attack = MoveTypes.attackLeft
	
		else:
			attack = MoveTypes.attackForward

		return attack

	def updateAngle(self):
		mousePosVector = Vector2(pygame.mouse.get_pos())
		self.angle = (mousePosVector - self.coord).angle_to(Vector2(0, -1)) % 360

	def setUpEventListeners(self):
		super().setUpEventListeners()
		self.registerCombat()

	def registerCombat(self):
		@EventListener(pygame.locals.MOUSEBUTTONDOWN, button=1)
		def startAttack(event):
			activeMove = self.getActiveAttackMove()
			if activeMove is None:
				move = self.moveSetController.getMove(self.getAttack())
				move.start()
				move.listenForMilestone(AttackMilestones.woundUp, lambda: self.lockMovement())
				move.listenForMilestone(AttackMilestones.attacked, lambda: self.unlockMovement())

			elif activeMove.hasPassedMileStone(AttackMilestones.attackOver):
				activeMove.listenForEnd(lambda: self._startQedMove())

	def setUpSubEntities(self):
		super().setUpSubEntities()
		self.weapon = LongSword(CharacterParts.weapon, self.rightHand, self)

	def _startQedMove(self):
		move = self.moveSetController.getMove(self.getAttack())
		move.start()
