from pygame.math import Vector2

from map.ai import Ai


class EnemyAi(Ai):
	def __init__(self, character):
		super().__init__(character)
		self.thresholdToPlayer = 50

	def loopCall(self):
		super().loopCall()

		self.moveTowardsPlayer()
		self.lookTowardsPlayer()

	def lookTowardsPlayer(self):
		self.lookTowardsEntity(self.character.map.player)

	def moveTowardsPlayer(self):
		self.moveTowardsMapEntity(self.character.map.player, self.thresholdToPlayer)