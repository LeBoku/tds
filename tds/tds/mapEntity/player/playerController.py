import pygame.locals
import pygame.mouse
from pygame.math import Vector2

from mapEntity.character.characterController import CharacterController

from pygameUtil.EventHandling import EventListener, EventHandler
from pygameUtil import math_

from mapEntity.subEntity.subEntity import SubEntity
from store import images
from store import moveSets

class PlayerController(CharacterController):
	def __init__(self, map):
		super().__init__(map)
		self.speed = 5
		self.eventHandler = EventHandler.get()
		
		self.isMovementLocked = False
		self.isStopingMovementAnimation = False

		self.movementKeys = {
			pygame.locals.K_w: ["y", -1],
			pygame.locals.K_d: ["x", 1],
			pygame.locals.K_s: ["y", 1],
			pygame.locals.K_a: ["x", -1]
		}

	def lockMovement(self):
		self.isMovementLocked = True
	def unLockMovement(self):
		self.isMovementLocked = False

	def loopCall(self):
		super().loopCall()
		self.updateAngle()
		self.updateMovement()

	def updateMovement(self):
		pressedKeys = self.eventHandler.orderKeysByLoopsDown(self.movementKeys.keys())

		if len(pressedKeys) > 0 and not self.isMovementLocked:
			forwardMovement = Vector2(0,0)
			self.startMoveAnimation()
			movement = {"x":0,"y":0}
			for key in reversed(pressedKeys):
				movement[self.movementKeys[key][0]] = self.movementKeys[key][1]

			forwardMovement = Vector2(movement["x"], movement["y"])

			if forwardMovement.length() > 0:
				forwardMovement.scale_to_length(self.speed)
				oldCord = Vector2(self.coord)
				self.coord += forwardMovement
				
				if self.isCollidingWithSomething():
					self.coord = oldCord
		else:
			self.stopMoveAnimation()

	def startMoveAnimation(self):
		move = self.moveSetController.getMove("move")
		if not move.isActive:
			move.start()

	def stopMoveAnimation(self):
		move = self.moveSetController.getMove("move")
		if not self.isStopingMovementAnimation:
			move.listenForMilestone(moveSets.milestones.WalkMilestones.halfWay, lambda: move.stop())

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
			move = self.moveSetController.getMove("attack_forward")
			if not move.isActive:
				move.start()
				move.listenForMilestone(moveSets.milestones.AttackMilestones.woundUp, lambda: self.lockMovement())
				move.listenForMilestone(moveSets.milestones.AttackMilestones.attacked, lambda: self.unLockMovement())

			elif move.framesLeft < quequeWindow:
				move.listenForEnd(lambda: move.start())

	def setUpSubEntities(self):
		self.collisionPoints = [(-3, -1.5),
			(3, -1.5),
			(3, 1.5),
			(-3, 1.5)]

		self.coord = Vector2(500, 400)
		
		self.moveSetController.registerMove("attack_forward", moveSets.spear.forwardAttack())
		self.moveSetController.registerMove("move", moveSets.character.move())
		
		self.createSubEntity("leftHand", images.character.hand(), Vector2(-5, 0))
		rightHand = self.createSubEntity("rightHand", images.character.hand(), Vector2(5, 0))

		self.createSubEntity("weapon", images.weapons.spear(), parent=rightHand)
