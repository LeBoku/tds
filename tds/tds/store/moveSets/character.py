from ._entity import Entity
from ._move import Move

def move():
	armSwing = 10
	armSwingTime = 10

	rightHand = Entity()
	rightHand.animateTo(armSwingTime, (0, armSwing))
	rightHand.animateTo(armSwingTime*2, (0, -armSwing))
	rightHand.backToDefault(armSwingTime)
		
	leftHand = Entity()
	leftHand.animateTo(armSwingTime, (0, -armSwing))
	leftHand.animateTo(armSwingTime*2, (0, armSwing))
	leftHand.backToDefault(armSwingTime)

	move = Move(
		rightHand=rightHand,
		leftHand=leftHand
	)

	return move