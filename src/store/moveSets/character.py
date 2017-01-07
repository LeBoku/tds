from ._entity import Entity
from ._move import Move

from .milestones import Walk

from store.enums import CharacterParts


def walk():
	armSwing = 10
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

	entities = dict()
	entities[CharacterParts.rightHand] = rightHand
	entities[CharacterParts.leftHand] = leftHand

	move = Move(entities)

	move.mileStones[Walk.halfWay] = armSwingTime * 2

	return move