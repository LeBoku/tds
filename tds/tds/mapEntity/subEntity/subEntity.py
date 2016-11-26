import math
import pygame.transform

from pygame.math import Vector2

from mapEntity.MapEntityController import MapEntityController

from pygameUtil import math_

class SubEntity(MapEntityController):
	def __init__(self, map):
		super().__init__(map)
		self.parent = None
		self.name = None
		self.offsetVector = Vector2(10, 0)
		self.offsetAngle = 0

	def alignToParent(self):
		offset = self.parent.moveSetController.getOffsetForEntity(self.name)
		movement = offset.vector
		baseOffset = self.offsetVector + movement

		characterAngle = self.parent.angle
		offset = baseOffset.rotate(180 - characterAngle)

		self.coord = self.parent.coord - offset

		self.angle = self.parent.angle + self.offsetAngle

	def display(self):
		self.alignToParent()
		return super().display()