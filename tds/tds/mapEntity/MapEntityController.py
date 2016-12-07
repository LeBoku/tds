from pygame.math import Vector2
from shapely.geometry import Polygon

from base.controller import Controller
from base.types.collision import Collison
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
	def collisionPolygon(self):
		if len(self.collisionPoints) == 0:
			return None
		
		collisionPolygonPoints = []
		for point in self.collisionPoints:
			offsetVector = Vector2(point).rotate(-self.angle)
			vector = self.coord + offsetVector
			collisionPolygonPoints.append((vector.x,vector.y))

		return Polygon(collisionPolygonPoints)

	def isCollidingWithSomething(self):
		return self.map.isCollidingWithSomeThing(self).isColliding

	def isCollidingWith(self, initiator):
		poly = self.collisionPolygon
		initiatorPolygon = initiator.collisionPolygon

		if (poly is not None) and poly.intersects(initiatorPolygon):
			return Collison(initiator, self, initiatorPolygon, poly, poly.intersection(initiatorPolygon))

	def loopCall(self):
		pass

	def addSubEntity(self, name, entity):
		entity.name = name
		entity.parent = self
		self.subEntities[name] = entity
		self.map.addEntity(entity)

	def setUpDisplayHandler(self):
		self.displayHandler = MapEntityDisplay(self)

	def createSubEntity(self, name, image, offset=Vector2(0,0), parent=None):
		if (parent is None):
			parent = self

		e = SubEntity(self.map)
		e.offsetVector = offset
		e.setBaseImage(image)

		parent.addSubEntity(name, e)

		return e

from mapEntity.subEntity.subEntity import SubEntity # down here because of circular dependency