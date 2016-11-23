import math
import pygame.transform

from pygame.math import Vector2

from mapEntity.MapEntityController import MapEntityController

from pygameUtil import math_

class WeaponController(MapEntityController):
	def __init__(self, map):
		super().__init__(map)
		self.character = None
		self.offsetVector = Vector2(-10, 0)
		self.offsetAngle = 0

	def alignToCharacter(self):
		offset = self.offsetVector.rotate(180 - self.character.angle.angle_to(Vector2(0, -1)))

		self.coord = self.character.coord + offset
		self.coord += self.character.moveSetController.getMovementFor("weapon")

		self.angle = self.character.angle.rotate(self.offsetAngle)

	def display(self):
		self.alignToCharacter()
		return super().display()