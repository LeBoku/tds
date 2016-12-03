from ._entity import Entity
from ._move import Move

from .milestones import Walk

def move():
	armSwing = 5
	armSwingTime = 5

	rightHand = Entity()
	rightHand.animateTo(armSwingTime, (0, armSwing))
	rightHand.animateTo(armSwingTime, (0, 0))
	rightHand.animateTo(armSwingTime, (0, -armSwing))
	rightHand.animateTo(armSwingTime, (0, 0))
		
	leftHand = Entity()
	leftHand.animateTo(armSwingTime, (0, -armSwing))
	leftHand.animateTo(armSwingTime, (0, 0))
	leftHand.animateTo(armSwingTime, (0, armSwing))
	leftHand.animateTo(armSwingTime, (0, 0))

	move = Move(
		rightHand=rightHand,
		leftHand=leftHand
	)

	move.mileStones[Walk.halfWay] = armSwingTime * 2

	return move