from ._entity import Entity
from ._move import Move

def move():
	armSwing = 10
	armSwingTime = 10

	rightHand = Entity()
	rightHand.animateTo((0, armSwing), armSwingTime)
	rightHand.animateTo((0, -armSwing), armSwingTime*2)
	rightHand.backToDefault(armSwingTime)
		
	leftHand = Entity()
	leftHand.animateTo((0, -armSwing), armSwingTime)
	leftHand.animateTo((0, armSwing), armSwingTime*2)
	leftHand.backToDefault(armSwingTime)

	move = Move(
		rightHand=rightHand,
		leftHand=leftHand
	)

	return move