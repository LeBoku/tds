from ._entity import Entity
from ._move import Move

from .milestones import Attack
from store.enums import CharacterParts


def rightAttack():
	milestones = {
		Attack.woundUp: 20,
		Attack.attacked: 40,
		Attack.cooledDown: 50
	}

	rightHand = Entity()
	rightHand.animateTo(5, (5, -3), -45)
	rightHand.repeatFrame(15)
	rightHand.rotateAround(5, -90)
	rightHand.repeatFrame(15)
	rightHand.backToDefault(10)

	weapon = Entity()
	weapon.animateTo(5, (0, -10))
	weapon.repeatFrame(40)
	weapon.backToDefault(5)
	weapon.repeatFrame(5)

	entities = dict()
	entities[CharacterParts.rightHand] = rightHand
	entities[CharacterParts.weapon] = weapon

	move = Move(entities)

	move.mileStones.update(milestones)
	return move


def leftAttack():
	milestones = {
		Attack.woundUp: 30,
		Attack.attacked: 40,
		Attack.cooledDown: 65
	}

	rightHand = Entity()
	rightHand.rotateAround(15, -200, (-10, 0))
	rightHand.repeatFrame(15)
	rightHand.rotateAround(10, 300, (-10, 0))
	rightHand.repeatFrame(15)
	rightHand.backToDefault(20)
	# #AllPlanned rotates the wrong way but its cool. correct would be: rightHand.rotateAround(10, -100, (-10, 0))

	weapon = Entity()
	weapon.repeatFrame(30)
	weapon.animateTo(5, (0, -10))
	weapon.repeatFrame(20)
	weapon.backToDefault(20)

	entities = dict()
	entities[CharacterParts.rightHand] = rightHand
	entities[CharacterParts.weapon] = weapon

	move = Move(entities)

	move.mileStones.update(milestones)

	return move


def forwardAttack():
	milestones = {
		Attack.woundUp: 10,
		Attack.attacked: 30,
		Attack.cooledDown: 35
	}

	rightHand = Entity()
	rightHand.animateTo(5, (0, 15))
	rightHand.repeatFrame(5)
	rightHand.animateTo(5, (0, -15))
	rightHand.repeatFrame(15)
	rightHand.backToDefault(5)

	leftHand = Entity()
	leftHand.animateTo(10, (0, -10))
	leftHand.animateTo(5, (0, 10))
	leftHand.repeatFrame(10)
	leftHand.backToDefault(5)

	torso = Entity()
	torso.animateTo(5, toAngle=-45)
	torso.repeatFrame(5)
	torso.animateTo(5, toAngle=45, clockwise=True)
	torso.repeatFrame(15)
	torso.animateTo(5, toAngle=0)

	entities = dict()
	entities[CharacterParts.torso] = torso
	entities[CharacterParts.rightHand] = rightHand
	entities[CharacterParts.leftHand] = leftHand
	# entities[CharacterParts.weapon] = weapon

	move = Move(entities)

	move.mileStones.update(milestones)

	return move