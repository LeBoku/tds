from map.mapEntityController import MapEntityController
from store.images import props


class Boundry(MapEntityController):
	def __init__(self, map, rect, color=(0, 0, 0)):
		super().__init__(map)
		self.setBaseImage(props.boundry(rect, color))
		self.coord = rect.center
		rect.center = 0, 0

		self.collisionPoints = [rect.topleft, rect.topright, rect.bottomright, rect.bottomleft]
		map.addCollisionEntity(self)
