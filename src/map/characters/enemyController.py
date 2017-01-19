from .NPCController import NPCController
from map.ais.enemyAi import EnemyAi


class EnemyController(NPCController):
	def setUpAI(self):
		self.ai = EnemyAi(self)
