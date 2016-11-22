from mapEntity.MapEntityController import MapEntityController

from .moveSet import MoveSetController

class CharacterController(MapEntityController):
	def __init__(self, map):
		super().__init__(map)
		self._weapon = None
		self.moveSetController = MoveSetController()

	@property
	def weapon(self):
		return self._weapon
	@weapon.setter
	def weapon(self, weapon):
		if(self.weapon is not None):
			self.weapon.character = None;
			self.map.removeEntity(self.weapon)

		weapon.character = self
		self.map.addEntity(weapon)

		self._weapon = weapon