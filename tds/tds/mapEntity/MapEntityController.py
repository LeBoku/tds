from base.controller import Controller
from mapEntity.MapEntityDisplay import MapEntityDisplay

import pygameUtil.imageHelper

class MapEntityController(Controller):
	def __init__(self, map):
		super().__init__()
		self.map = map
		self.coord = [0, 0]
		self.angle = 0
		self.displayHandler = MapEntityDisplay(self)