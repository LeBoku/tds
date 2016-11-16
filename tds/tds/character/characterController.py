from mapEntity.MapEntityController import MapEntityController

from character.characterDisplay import CharacterDisplay

class CharacterController(MapEntityController):
	def __init__(self, map):
		super().__init__(map)
		self.displayHandler = CharacterDisplay(self)
		self._weapon = None

	@property
	def weapon(self):
		return self._weapon
	@weapon.setter
	def weapon(self, weapon):
		self._weapon = weapon