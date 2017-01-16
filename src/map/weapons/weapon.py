from map.characters.characterController import CharacterController
from map.subEntity import SubEntity
from store.types import Particle


class Weapon(SubEntity):
	def __init__(self, name, parent: CharacterController):
		super().__init__(parent.map)
		self.name = name
		self.parent = parent
		self.character = parent.parent

		self.setUpCollisionPoints()
		self.setUpWeaponMoveSet()

		self.lastAttackParticle = None

		parent.addSubEntity(name, self)

	def setUpCollisionPoints(self):
		pass

	def setUpWeaponMoveSet(self):
		pass

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
