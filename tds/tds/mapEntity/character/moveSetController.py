from copy import copy

from pygame.math import Vector2

class MoveSetController:
	def __init__(self, **kwargs):
		self.moves = {}
		self.activeMoves = {}

	def moveOn(self):
		movesToStop = []

		for key, move in self.activeMoves.items():
			if(move["activeFrameNr"] < move["frameCount"]):
				move["activeFrameNr"] += 1
			else:
				movesToStop.append(key)
			
		for move in movesToStop:
			self.activeMoves.pop(move)

	def getMovementFor(self, entity):
		pos = Vector2(0,0)

		for key, move in self.activeMoves.items():
			activeFrame = move["frames"][move["activeFrameNr"]-1]
			if entity in activeFrame:
				pos = activeFrame[entity]

		return pos

	def startMove(self, name):
		self.activeMoves[name] = copy(self.moves[name])
		self.activeMoves[name]["activeFrameNr"] = 0

	def registerMove(self, name, move):
		move["activeFrameNr"] = None
		move["frameCount"] = len(move["frames"])
		self.moves[name] = move

