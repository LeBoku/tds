from pygame.math import Vector2

class MoveSetController:
	def __init__(self, **kwargs):
		self.moves = {}

	def getMovementFor(self, entity):
		pos = Vector2(0,0)

		for key, move in self.moves.items():
			if move["activeFrameNr"] is not None:
				activeFrame = move["frames"][move["activeFrameNr"]]
				if hasattr(activeFrame, entity):
					pos = activeFrame[entity]

		return pos

	def startMove(self, name):
		self.moves[name].activeFrame = -1

	def registerMove(self, name, move):
		move["activeFrameNr"] = None
		move["frameCount"] = len(move["frames"])
		self.moves[name] = move

