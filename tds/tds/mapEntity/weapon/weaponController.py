import math
import pygame.transform

from pygame.math import Vector2

from mapEntity.MapEntityController import MapEntityController

from pygameUtil import math_

class WeaponController(MapEntityController):
	def __init__(self, map):
		super().__init__(map)
		self.character = None
		self.offsetToCharacter = Vector2(10, 0)
		self.offsetToCharacterAngle = Vector2(0, 0)

	def alignToCharacter(self):
		self.coord = self.character.coord + self.offsetToCharacter
		self.coord += self.character.moveSetController.getMovementFor("weapon")

		self.angle = self.character.angle + self.offsetToCharacterAngle

	def display(self):
		self.alignToCharacter()
		return super().display()