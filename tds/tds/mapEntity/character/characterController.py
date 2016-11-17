from mapEntity.MapEntityController import MapEntityController

class CharacterController(MapEntityController):
	def __init__(self, map):
		super().__init__(map)
		self._weapon = None

	@property
	def weapon(self):
		return self._weapon
	@weapon.setter
	def weapon(self, weapon):
		if(self.weapon is not None):
			self.map.removeEntity(self.weapon)

		self.map.addEntity(weapon)

		self._weapon = weapon