from map.ai import Ai

from store.perception import PerceptionListener
from store.enums import PerceptionTypes, MoveTypes

from map.characters.player.playerController import PlayerController


class EnemyAi(Ai):
	def __init__(self, character, map):
		super().__init__(character, map)
		self.thresholdToPlayer = 50
		self.isAttacking = False

	def setUpPerceptionListeners(self):
		def isSeeingPlayer(perception):
			return perception.type == PerceptionTypes.inSight and isinstance(perception.data["entity"], PlayerController)

		def onSeeingPlayer(perception):
			self.moveTowardsPlayer()
			self.lookTowardsPlayer()

		self.perceptionListeners.append(PerceptionListener(isSeeingPlayer, onSeeingPlayer))

		def isCloseToPlayer(perception):
			distanceToPlayer = self.getDistanceVectorToMapEntity(self.character.map.player).length()
			return distanceToPlayer <= self.thresholdToPlayer

		def onCloseToPlayer(perception):
			self.attackPlayer()

		self.perceptionListeners.append(PerceptionListener(isCloseToPlayer, onCloseToPlayer))

	def attackPlayer(self):
		if not self.isAttacking:
			move = self.character.moveSetController.getMove(MoveTypes.attackFast)
			move.start()

			self.isAttacking = True

			move.listenForEnd(lambda: self.onEndOfAttack())

	def onEndOfAttack(self):
		self.isAttacking = False

	def lookTowardsPlayer(self):
		self.lookTowardsEntity(self.character.map.player)

	def moveTowardsPlayer(self):
		self.moveTowardsMapEntity(self.character.map.player, self.thresholdToPlayer)