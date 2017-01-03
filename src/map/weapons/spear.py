from map.subEntity import SubEntity

from store.collisionPoints.weapons import spear as spearCollision
from store.images.weapons import spear as spearImage


class Spear(SubEntity):
	def __init__(self, name, parent):
		self.name = name
		self.parent = parent

		super().__init__(parent.map)

		self.collisionPoints = spearCollision()		
		self.setBaseImage(spearImage())
		parent.addSubEntity(name, self)
