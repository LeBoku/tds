from map.ai import Ai
from .characterController import CharacterController


class NPCController(CharacterController):
	def __init__(self, map):
		super().__init__(map)

		self.ai = None
		self.setUpAI()

		self.destination = None

	def loopCall(self):
		super().loopCall()

		if self.ai is not None:
			self.ai.loopCall()

		self._moveTowardsDestination()

	def setDestination(self, destination):
		self.destination = destination

	def setUpAI(self):
		self.ai = Ai(self, self.map)

	def _moveTowardsDestination(self):
		if self.destination is not None:
			self.startMoveAnimation()
			direction = self.destination - self.coord
			distance = direction.length()
			if distance < self.speed:
				self.coord = self.destination

			elif distance > 0:
				direction.scale_to_length(self.speed)
				self.coord += direction

		else:
			self.stopMoveAnimation()
