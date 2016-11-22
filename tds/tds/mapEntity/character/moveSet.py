class MoveSetController:
	def __init__(self, **kwargs):
		self.moves = {} # {"attackLeft": {"frames": [{ "character":[-2, 4], ...}, {...}]},...}

	def startMove(self):
		pass

	def registerMove(self, name, move):
		self.moves[name] = move

