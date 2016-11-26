from ._entity import Entity
from ._move import Move

def forwardAttack():
	rightHand = Entity()
	rightHand.animateTo((0, 10), 5)
	rightHand.repeatFrame(5)
	rightHand.animateTo((0, -10), 5)
	rightHand.repeatFrame(15)
	rightHand.backToDefault(5)
		
	leftHand = Entity()
	leftHand.animateTo((0, -10), 10)
	leftHand.animateTo((0, 5), 5)
	leftHand.repeatFrame(10)
	leftHand.backToDefault(5)

	weapon = Entity()
	weapon.repeatFrame(10)
	weapon.animateTo((0,-15), 5)
	weapon.repeatFrame(15)
	weapon.backToDefault(5)

	move = Move(
		rightHand=rightHand,
		leftHand=leftHand,
		weapon=weapon
	)

	return move