from pygame.math import Vector2

from map.mapEntityController import MapEntityController

from store.moveSetController import MoveSetController
from store import moveSets
from store import images
from store.moveSets import milestones
from store.enums import CharacterParts, attackTypes, MoveTypes


class CharacterController(MapEntityController):
	def __init__(self, map):
		super().__init__(map)
		self._weapon = None

		self.isAttacking = False

		self.moveSetEntityName = CharacterParts.character
		self.moveSetController = MoveSetController()

		self.torso = None
		self.leftHand = None
		self.rightHand = None
		self.weapon = None

		self.setUpSubEntities()

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

	def stopMoveAnimation(self):
		move = self.moveSetController.getMove(MoveTypes.walk)
		if not self.isStopingMovementAnimation:
			move.listenForMilestone(milestones.Walk.halfWay, lambda: move.stop())

	def setUpSubEntities(self):
		self.moveSetController.registerMove(MoveTypes.walk, moveSets.character.walk())

		self.collisionPoints = [(-3, -1.5),
			(3, -1.5),
			(3, 1.5),
			(-3, 1.5)]

		self.torso = self.createSubEntity(CharacterParts.torso, images.character.torso(), Vector2(0, 0))

		self.leftHand = self.createSubEntity(CharacterParts.leftHand, images.character.hand(), Vector2(-10, 0))
		self.rightHand = self.createSubEntity(CharacterParts.rightHand, images.character.hand(), Vector2(10, 0))

	def loopCall(self):
		self.moveSetController.moveOn()
		self.dealWithMoveOffset()
		return super().loopCall()