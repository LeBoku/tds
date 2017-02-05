from map.ai import Ai

from store.perception import PerceptionListener
from store.enums import PerceptionTypes

from map.characters.player.playerController import PlayerController


class EnemyAi(Ai):
	def __init__(self, character, map):
		super().__init__(character, map)
		self.thresholdToPlayer = 50

	def setUpPerceptionListeners(self):
		def isSeeingPlayer(perception):
			return perception.type == PerceptionTypes.inSight and isinstance(perception.data["entity"], PlayerController)

		def onSeeingPlayer(perception):
			self.moveTowardsPlayer()
			self.lookTowardsPlayer()

		self.perceptionListeners.append(PerceptionListener(isSeeingPlayer, onSeeingPlayer))

	def lookTowardsPlayer(self):
		self.lookTowardsEntity(self.character.map.player)

	def moveTowardsPlayer(self):
		self.moveTowardsMapEntity(self.character.map.player, self.thresholdToPlayer)