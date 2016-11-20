import math
import pygame.transform

from mapEntity.MapEntityController import MapEntityController

from pygameUtil import math_

class WeaponController(MapEntityController):
	def __init__(self, map):
		super().__init__(map)
		self.character = None
		self.offsetToCharacter = [10, 0]
		self.offsetToCharacterAngle = 0

	def alignToCharacter(self):
		offsetAngle = (math_.calcAngleBetweenPositions((0,0), self.offsetToCharacter) + self.character.angle) % 360
		offsetDistance = math.sqrt(self.offsetToCharacter[0] ** 2 + self.offsetToCharacter[1] ** 2)


		self.coord = math_.calcNewPosByAngleAndDistance(self.character.coord, offsetAngle, offsetDistance)
		self.angle = (self.character.angle + self.offsetToCharacterAngle) % 360

	def display(self):
		self.alignToCharacter()
		return super().display()