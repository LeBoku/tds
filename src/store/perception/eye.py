from shapely.geometry import Point

from .perciver import Perciver
from store.enums import PerceptionTypes
from store.types.dicts import Peception


class Eye(Perciver):
	def __init__(self, character, map):
		super().__init__(character, map)
		self.seenThings = []

	def percive(self):
		perceptions = []
		viewCone = Point(self.character.coord).buffer(self.character.viewRange)

		visibleEntities = self.map.getEntitesInsideShape(viewCone)
		visibleEntities = [entity for entity in visibleEntities if entity is not self.character]

		if len(visibleEntities) > 0:
			newlySeen = [e for e in visibleEntities if e not in self.seenThings]
			lostSight = [e for e in self.seenThings if e not in visibleEntities]
			self.seenThings = visibleEntities

			for e in newlySeen:
				perceptions.append(Peception(PerceptionTypes.gainSight, entity=e))

			for e in self.seenThings:
				perceptions.append(Peception(PerceptionTypes.inSight, entity=e))

			for e in lostSight:
				perceptions.append(Peception(PerceptionTypes.lostSight, entity=e))

		return perceptions
