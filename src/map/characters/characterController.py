from pygame.math import Vector2

from map.mapEntityController import MapEntityController

from store.moveSetController import MoveSetController
from store import moveSets,images
from store.enums import CharacterParts, attackTypes, MoveTypes, AttackMilestones, DefaultMilestones, WalkMilestones


class CharacterController(MapEntityController):
	def __init__(self, map):
		super().__init__(map)
		self.baseSpeed = 3
		self.runningSpeedModificator = 2
		self.isRunning = True
		self.viewRange = 500

		self.isAttacking = False
		self.isStopingMovementAnimation = False

		self.moveSetController = None
		self.setUpMoveSetController()

		self.moveSetEntityName = CharacterParts.character

		self.torso = None
		self.leftHand = None
		self.rightHand = None
		self.weapon = None
		self.setUpSubEntities()

	@property
	def speed(self):
		return self.baseSpeed if not self.isRunning else self.baseSpeed * self.runningSpeedModificator

	def dealWithMoveOffset(self):
		offset = self.moveSetController.getOffsetForEntity(self.moveSetEntityName)

		if offset.vector.length() > 0:
			angle = self.angle + offset.angle
			vector = offset.vector.rotate(-angle)
			self.coord += vector

	def getActiveAttackMove(self):
		for attack in attackTypes:
			move = self.moveSetController.getMove(attack)
			if move.isActive:
				return move

	def startMoveAnimation(self):
		move = self.moveSetController.getMove(MoveTypes.walk)
		if not move.isActive:
			move.start()
			self.isStopingMovementAnimation = False

	def stopMoveAnimation(self):
		move = self.moveSetController.getMove(MoveTypes.walk)
		if not self.isStopingMovementAnimation:
			move.listenForMilestone(WalkMilestones.halfWay, lambda: move.stop())
			self.isStopingMovementAnimation = True

	def setUpMoveSetController(self):
		self.moveSetController = MoveSetController()
		self.moveSetController.registerMove(MoveTypes.walk, moveSets.character.walk())

	def setUpSubEntities(self):
		self.collisionPoints = [(-3, -1.5),
			(3, -1.5),
			(3, 1.5),
			(-3, 1.5)]

		self.torso = self.createSubEntity(CharacterParts.torso, images.character.torso(), Vector2(0, 0))

		self.leftHand = self.createSubEntity(CharacterParts.leftHand, images.character.hand(), Vector2(-10, 0), self.torso)
		self.rightHand = self.createSubEntity(CharacterParts.rightHand, images.character.hand(), Vector2(10, 0), self.torso)

	def loopCall(self):
		self.moveSetController.moveOn()
		self.dealWithMoveOffset()
		return super().loopCall()