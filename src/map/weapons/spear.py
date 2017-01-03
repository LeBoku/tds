from map.subEntity import SubEntity
from map.characterController import CharacterController

from store.collisionPoints.weapons import spear as spearCollision
from store.images.weapons import spear as spearImage


class Spear(SubEntity):
	def __init__(self, name, parent: CharacterController):
		self.name = name
		self.parent = parent
		self.character = parent.parent
		super().__init__(parent.map)

		self.originalCollisionPoints = spearCollision()
		self.setBaseImage(spearImage())
		parent.addSubEntity(name, self)

	def display(self):
		if self.character.isAttacking:
			self.collisionPoints = self.originalCollisionPoints

		return super().display()

