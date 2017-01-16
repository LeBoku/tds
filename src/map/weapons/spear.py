from .weapon import Weapon

from store.enums import MoveTypes
from store import images, moveSets, collisionPoints


class Spear(Weapon):
	def setUpBaseImage(self):
		self.setBaseImage(images.weapons.spear())

	def setUpCollisionPoints(self):
		self.collisionPoints = collisionPoints.weapons.spear()

	def setUpWeaponMoveSet(self):
		self.moveSetController.registerMove(MoveTypes.attackForward, moveSets.spear.forwardAttack())
		self.moveSetController.registerMove(MoveTypes.attackLeft, moveSets.spear.leftAttack())
		self.moveSetController.registerMove(MoveTypes.attackRight, moveSets.spear.rightAttack())
