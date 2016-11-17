import pygame.transform

from mapEntity.MapEntityController import MapEntityController

import pygameUtil.imageHelper

class WeaponController(MapEntityController):
	def __init__(self, map):
		super().__init__(map)
		self.character = None