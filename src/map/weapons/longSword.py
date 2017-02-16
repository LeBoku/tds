from pygame.math import Vector2

from .weapon import Weapon

from store import images, moveSets, collisionPoints
from store.enums import MoveTypes


class LongSword(Weapon):
	def setUpOffset(self):
		self.offsetVector = Vector2((0, -15))

	def setUpBaseImage(self):
		self.setBaseImage(images.weapons.longSword())

	def setUpWeaponMoveSet(self):
		self.moveSetController.registerMove(MoveTypes.attackWide, moveSets.longSword.wideAttack())
		self.moveSetController.registerMove(MoveTypes.attackFast, moveSets.longSword.fastAttack())

	def setUpCollisionPoints(self):
		self.collisionPoints = collisionPoints.weapons.longsSword()
