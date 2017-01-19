from .characterController import CharacterController
from map.ais.ai import Ai


class NPCController(CharacterController):
	def __init__(self, map):
		super().__init__(map)

		self.ai = None
		self.setUpAI()

	def setUpAI(self):
		self.ai = Ai(self)