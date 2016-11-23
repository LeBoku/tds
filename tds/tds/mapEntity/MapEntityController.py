from pygame.math import Vector2

from base.controller import Controller
from mapEntity.MapEntityDisplay import MapEntityDisplay

import pygameUtil.imageHelper

class MapEntityController(Controller):
	def __init__(self, map):
		super().__init__()
		self.map = map
		self.coord = Vector2(0, 0)
		self._angle = None
		self.angle = Vector2(0, -1)

	@property
	def angle(self):
		return self._angle
	@angle.setter
	def angle(self, angle):
		angle.normalize_ip()
		self._angle = angle

	def setUpDisplayHandler(self):
		self.displayHandler = MapEntityDisplay(self)
