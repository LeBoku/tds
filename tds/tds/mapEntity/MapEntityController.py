from pygame.math import Vector2

from base.controller import Controller
from mapEntity.MapEntityDisplay import MapEntityDisplay

import pygameUtil.imageHelper

class MapEntityController(Controller):
	def __init__(self, map):
		super().__init__()
		self.map = map
		self.coord = Vector2(0, 0)
		self.angle = 0
		self.subEntities = {}
		self.offset = None
	
	def addSubEntity(self, name, entity):
		entity.name = name
		entity.parent = self
		self.subEntities[name] = entity
		self.map.addEntity(entity)

	def setUpDisplayHandler(self):
		self.displayHandler = MapEntityDisplay(self)
