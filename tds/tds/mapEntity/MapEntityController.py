from base.controller import Controller
from mapEntity.MapEntityDisplay import MapEntityDisplay

class MapEntityController(Controller):
	def __init__(self, map):
		super().__init__()
		self.map = map
		self.coord = 0, 0
		self.displayHandler = MapEntityDisplay(self)
