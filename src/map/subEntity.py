from pygame.math import Vector2

from map.mapEntityController import MapEntityController


class SubEntity(MapEntityController):
	def __init__(self, map):
		super().__init__(map)
		self.parent = None
		self.name = None
		self.offsetVector = Vector2(0, 0)
		self.offsetAngle = 0
		self._moveSetController = None

	@property
	def depth(self):
		depth = 1
		parent = self.parent

		while parent is not None:
			depth += 1
			if hasattr(parent, "parent"):
				parent = parent.parent
			else:
				break

		return depth

	@property
	def moveSetController(self):
		if self._moveSetController is None:
			return self.parent.moveSetController
		else:
			return self._moveSetController

	@moveSetController.setter
	def moveSetController(self, controller):
		self._moveSetController = controller

	def alignToParent(self):
		offset = self.moveSetController.getOffsetForEntity(self.name)
		base_offset = self.offsetVector + offset.vector

		parent_angle = self.parent.angle
		offsetVector = base_offset.rotate(180 - parent_angle)

		self.coord = self.parent.coord - offsetVector
		self.angle = self.parent.angle + self.offsetAngle + offset.angle

	def loopCall(self):
		self.alignToParent()
		super().loopCall()