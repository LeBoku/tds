from .weapon import Weapon

from store import images, moveSets, collisionPoints
from store.enums import MoveTypes


class LongSword(Weapon):
	def setUpBaseImage(self):
		self.setBaseImage(images.weapons.longSword())

	def setUpWeaponMoveSet(self):
		self.moveSetController.registerMove(MoveTypes.attackForward, moveSets.longSword.forwardAttack())
		self.moveSetController.registerMove(MoveTypes.attackLeft, moveSets.longSword.leftAttack())
		self.moveSetController.registerMove(MoveTypes.attackRight, moveSets.longSword.rightAttack())

	def setUpCollisionPoints(self):
		self.collisionPoints = collisionPoints.weapons.longsSword()
