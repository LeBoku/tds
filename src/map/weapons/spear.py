from map.subEntity import SubEntity
from map.characterController import CharacterController

from store.collisionPoints.weapons import spear as spearCollision
from store.images.weapons import spear as spearImage

from store.types import Particle


class Spear(SubEntity):
	def __init__(self, name, parent: CharacterController):
		self.name = name
		self.parent = parent
		self.character = parent.parent
		super().__init__(parent.map)

		self.lastAttackParticle = None

		self.collisionPoints = spearCollision()
		self.setBaseImage(spearImage())
		parent.addSubEntity(name, self)

	def display(self):
		if self.character.isAttacking:
			if self.lastAttackParticle is not None:
				particle = self.lastAttackParticle.union(self.collisionPolygon).convex_hull
				self.lastAttackParticle = self.collisionPolygon

			else:
				particle = self.collisionPolygon
				self.lastAttackParticle = self.collisionPolygon

			self.map.addParticle(Particle(particle, (200, 200, 200)))

		else:
			self.lastAttackParticle = None

		return super().display()

