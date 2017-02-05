from map.characters.NPCController import NPCController
from map.characters.enemy.enemyAi import EnemyAi


class EnemyController(NPCController):
	def setUpAI(self):
		self.ai = EnemyAi(self, self.map)
