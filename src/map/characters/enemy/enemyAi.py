from pygame.math import Vector2

from map.ai import Ai


class EnemyAi(Ai):
	def __init__(self, character):
		super().__init__(character)
		self.thresholdToPlayer = 50

	def loopCall(self):
		player = self.character.map.player

		distanceToPlayerVector = player.coord - self.character.coord
		distanceToPlayer = distanceToPlayerVector.length()

		if distanceToPlayer < self.thresholdToPlayer:
			distanceToPlayerVector.rotate(180)
			distanceToPlayerVector.scale_to_length(self.thresholdToPlayer - distanceToPlayer)
			self.character.setDestination(distanceToPlayerVector)

		elif distanceToPlayer > self.thresholdToPlayer:
			distanceToPlayerVector.scale_to_length(distanceToPlayer - self.thresholdToPlayer)
			self.character.setDestination(self.character.coord + distanceToPlayerVector)

		else:
			self.character.setDestination(None)