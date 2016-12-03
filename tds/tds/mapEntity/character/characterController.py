from mapEntity.MapEntityController import MapEntityController

from base.moveSetController import MoveSetController

class CharacterController(MapEntityController):
	def __init__(self, map):
		super().__init__(map)
		self._weapon = None
		self.moveSetEntityName = "character"
		self.moveSetController = MoveSetController()

	def dealWithMoveOffset(self):
		self.offset = self.moveSetController.getOffsetForEntity(self.moveSetEntityName)

	def loopCall(self):
		self.moveSetController.moveOn()
		self.dealWithMoveOffset()
		return super().loopCall()