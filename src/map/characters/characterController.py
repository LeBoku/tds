from map.mapEntityController import MapEntityController

from store.moveSetController import MoveSetController
from store.images import character
from store.enums import CharacterParts


class CharacterController(MapEntityController):
	def __init__(self, map):
		super().__init__(map)
		self._weapon = None

		self.isAttacking = False

		self.moveSetEntityName = CharacterParts.character
		self.moveSetController = MoveSetController()

	def dealWithMoveOffset(self):
		offset = self.moveSetController.getOffsetForEntity(self.moveSetEntityName)

		if offset.vector.length() > 0:
			angle = self.angle + offset.angle
			vector = offset.vector.rotate(-angle)
			self.coord += vector

	def loopCall(self):
		self.moveSetController.moveOn()
		self.dealWithMoveOffset()
		return super().loopCall()