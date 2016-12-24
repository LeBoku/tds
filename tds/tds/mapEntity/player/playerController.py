import pygame.locals
import pygame.mouse
from pygame.math import Vector2

from mapEntity.character.characterController import CharacterController

from pygameUtil.EventHandling import EventListener, EventHandler
from pygameUtil import math_

from mapEntity.subEntity.subEntity import SubEntity
from store import images
from store import moveSets
from store import collisionPoints
from enum import Enum

class PlayerController(CharacterController):
	def __init__(self, map):
		super().__init__(map)
		self.speed = 5
		self.eventHandler = EventHandler.get()
		
		self.isAttacking = False
		self.isStopingMovementAnimation = False

		self.movementKeys = {
			pygame.locals.K_w: ["y", -1],
			pygame.locals.K_d: ["x", 1],
			pygame.locals.K_s: ["y", 1],
			pygame.locals.K_a: ["x", -1]
		}

	def lockMovement(self):
		self.isAttacking = True
	def unLockMovement(self):
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
			attack = Attacks.right

		elif 225 < angle < 315:
			attack = Attacks.left
	
		else:
			attack = Attacks.forward

		return attack

	def getActiveAttackMove(self):
		for attack in Attacks:
			move = self.moveSetController.getMove(attack)
			if (move.isActive):
				return move

	def startMoveAnimation(self):
		move = self.moveSetController.getMove("move")
		if not move.isActive:
			pass #move.start()

	def stopMoveAnimation(self):
		move = self.moveSetController.getMove("move")
		if not self.isStopingMovementAnimation:
			move.listenForMilestone(moveSets.milestones.Walk.halfWay, lambda: move.stop())

	def updateAngle(self):
		mousePosVector = Vector2(pygame.mouse.get_pos())
		self.angle = (mousePosVector - self.coord).angle_to(Vector2(0, -1)) % 360

	def registerEvents(self):
		super().registerEvents()
		self.registerCombat()

	def registerCombat(self):
		quequeWindow = 20
	
		@EventListener(pygame.locals.MOUSEBUTTONDOWN, button=1)
		def startAttack(event):
			activeMove = self.getActiveAttackMove()
			if activeMove is None:
				move = self.moveSetController.getMove(self.getAttack())
				move.start()
				move.listenForMilestone(moveSets.milestones.Attack.woundUp, lambda: self.lockMovement())
				move.listenForMilestone(moveSets.milestones.Attack.attacked, lambda: self.unLockMovement())

			elif activeMove.framesLeft < quequeWindow:
				move = self.moveSetController.getMove(self.getAttack())
				move.listenForEnd(lambda: move.start())

	def setUpSubEntities(self):
		self.collisionPoints = [(-3, -1.5),
			(3, -1.5),
			(3, 1.5),
			(-3, 1.5)]

		self.coord = Vector2(500, 400)
		
		self.moveSetController.registerMove(Attacks.forward, moveSets.spear.forwardAttack())
		self.moveSetController.registerMove(Attacks.right, moveSets.spear.rightAttack())
		self.moveSetController.registerMove(Attacks.left, moveSets.spear.leftAttack())
		self.moveSetController.registerMove("move", moveSets.character.move())
		
		self.createSubEntity("leftHand", images.character.hand(), Vector2(-5, 0))
		rightHand = self.createSubEntity("rightHand", images.character.hand(), Vector2(5, 0))

		self.weapon = self.createSubEntity("weapon", images.weapons.spear(), parent=rightHand)
		self.weapon.collisionPoints = collisionPoints.weapons.spear()

class Attacks(Enum):
	left = 0
	forward = 1
	right= 2
