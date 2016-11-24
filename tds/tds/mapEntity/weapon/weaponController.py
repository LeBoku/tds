import math
import pygame.transform

from pygame.math import Vector2

from mapEntity.MapEntityController import MapEntityController

from pygameUtil import math_

class WeaponController(MapEntityController):
	def __init__(self, map):
		super().__init__(map)
		self.character = None
		self.offsetVector = Vector2(10, 0)
		self.offsetAngle = 0

	def alignToCharacter(self):
		movement = self.character.moveSetController.getMovementFor("weapon")
		baseOffset = self.offsetVector + movement

		characterAngle = self.character.angle
		offset = baseOffset.rotate(180 - characterAngle)

		self.coord = self.character.coord - offset

		self.angle = self.character.angle + self.offsetAngle

	def display(self):
		self.alignToCharacter()
		return super().display()