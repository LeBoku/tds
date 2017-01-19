from store.enums import CharacterParts, WalkMilestones
from store.types import Entity, Move


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

	move.mileStones[WalkMilestones.halfWay] = armSwingTime * 2

	return move


def dodge(frameCount, movementVector):
	character = Entity()
	character.repeatFrame(frameCount, movementVector)

	entities = dict()
	entities[CharacterParts.character] = character

	move = Move(entities)

	return move