from map.characters.NPCController import NPCController
from map.characters.enemy.enemyAi import EnemyAi
from map.weapons.longSword import LongSword
from store.enums import CharacterParts


class EnemyController(NPCController):
	def setUpSubEntities(self):
		super().setUpSubEntities()
		self.weapon = LongSword(CharacterParts.weapon, self.rightHand, self)

	def setUpAI(self):
		self.ai = EnemyAi(self, self.map)
