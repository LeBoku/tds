import pygame.transform

from mapEntity.MapEntityController import MapEntityController
from weapon.weaponDisplay import WeaponDisplay

import pygameUtil.imageHelper

class WeaponController(MapEntityController):
	def __init__(self, map):
		super().__init__(map)
		self.displayHandler = WeaponDisplay(self)
