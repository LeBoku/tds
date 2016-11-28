from pygame.math import Vector2
from shapely.geometry import Polygon

from base.controller import Controller
from mapEntity.MapEntityDisplay import MapEntityDisplay


class MapEntityController(Controller):
	def __init__(self, map):
		super().__init__()
		self.map = map
		self.coord = Vector2(0, 0)
		self.angle = 0
		self.subEntities = {}
		self.offset = None
		self.collisionPoints = []
	
	@property
	def collsionPolygon(self):
		if len(self.collisionPoints) == 0:
			return None
		
		collisionPolygonPoints = []
		for point in self.collisionPoints:
			vector = self.coord + Vector2(point)
			collisionPolygonPoints.append((vector.x,vector.y))

		return Polygon(collisionPolygonPoints)

	def isCollidingWith(self, collisionPolygon):
		if len(collisionPoints) == 0 or len(collisionPoints) == 0:
			return False

		return self.collsionPolygon.intersects(collsionPolygon)

	def addSubEntity(self, name, entity):
		entity.name = name
		entity.parent = self
		self.subEntities[name] = entity
		self.map.addEntity(entity)

	def setUpDisplayHandler(self):
		self.displayHandler = MapEntityDisplay(self)
