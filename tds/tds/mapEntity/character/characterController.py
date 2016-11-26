from mapEntity.MapEntityController import MapEntityController

from .moveSetController import MoveSetController

class CharacterController(MapEntityController):
	def __init__(self, map):
		super().__init__(map)
		self._weapon = None
		self.moveSetController = MoveSetController()

	def display(self):
		self.moveSetController.moveOn()
		return super().display()