from .weapon import Weapon

from store.enums import MoveTypes
from store.images.weapons import spear as spearImage
from store.moveSets import spear as spearMoves
from store.collisionPoints.weapons import spear as spearCollision


class Spear(Weapon):
	def setUpBaseImage(self):
		self.setBaseImage(spearImage())

	def setUpCollisionPoints(self):
		self.collisionPoints = spearCollision()

	def setUpWeaponMoveSet(self):
		self.moveSetController.registerMove(MoveTypes.attackForward, spearMoves.forwardAttack())
		self.moveSetController.registerMove(MoveTypes.attackLeft, spearMoves.leftAttack())
		self.moveSetController.registerMove(MoveTypes.attackRight, spearMoves.rightAttack())
