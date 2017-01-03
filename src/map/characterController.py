from map.mapEntityController import MapEntityController

from store.moveSetController import MoveSetController


class CharacterController(MapEntityController):
	def __init__(self, map):
		super().__init__(map)
		self._weapon = None

		self.isAttacking = False

		self.moveSetEntityName = "character"
		self.moveSetController = MoveSetController()

	def dealWithMoveOffset(self):
		self.offset = self.moveSetController.getOffsetForEntity(self.moveSetEntityName)

	def loopCall(self):
		self.moveSetController.moveOn()
		self.dealWithMoveOffset()
		return super().loopCall()