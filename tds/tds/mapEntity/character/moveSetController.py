from pygame.math import Vector2

from store.moveSets.offset import Offset

class MoveSetController:
	def __init__(self, **kwargs):
		self.moves = {}

	def moveOn(self):
		for key, move in self.moves.items():
			move.moveOn()

	def getOffsetForEntity(self, entity):
		offset = Offset()

		for key, move in self.moves.items():
			if move.isActive:
				moveOffset = move.getOffsetForEntity(entity)
				if moveOffset is not None:
					offset = moveOffset

		return offset

	def startMove(self, name):
		self.moves[name].start()

	def registerMove(self, name, move):
		self.moves[name] = move
