from pygame.math import Vector2

from store.moveSets._offset import Offset

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

	def AreAnyMovesActive(self, *moves):
		for move in moves:
			if move in self.moves:
				if self.moves[move].isActive:
					return True
		else:
			return False

	def getMove(self, name):
		return self.moves[name]

	def registerMove(self, name, move):
		self.moves[name] = move