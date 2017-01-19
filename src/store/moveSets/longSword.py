from store.enums import CharacterParts, AttackMilestones
from store.types import Entity, Move


def rightAttack():
	milestones = {
		AttackMilestones.woundUp: 20,
		AttackMilestones.attackOver: 25,
		AttackMilestones.attacked: 40,
		AttackMilestones.cooledDown: 50
	}

	rightHand = Entity()
	rightHand.animateTo(5, (5, -3), -45)
	rightHand.repeatFrame(15)
	rightHand.rotateAround(5, -90)
	rightHand.repeatFrame(15)
	rightHand.backToDefault(10)

	entities = dict()
	entities[CharacterParts.rightHand] = rightHand

	move = Move(entities)

	move.mileStones.update(milestones)
	return move


def leftAttack():
	milestones = {
		AttackMilestones.woundUp: 30,
		AttackMilestones.attackOver: 40,
		AttackMilestones.attacked: 65,
		AttackMilestones.cooledDown: 85
	}

	rightHand = Entity()
	rightHand.rotateAround(15, -200, (-10, 0))
	rightHand.repeatFrame(15)
	rightHand.rotateAround(10, 300, (-10, 0))
	rightHand.repeatFrame(15)
	rightHand.rotateAround(10, -100, (-10, 0))

	entities = dict()
	entities[CharacterParts.rightHand] = rightHand

	move = Move(entities)

	move.mileStones.update(milestones)

	return move


def forwardAttack():
	milestones = {
		AttackMilestones.woundUp: 10,
		AttackMilestones.attackOver: 15,
		AttackMilestones.attacked: 30,
		AttackMilestones.cooledDown: 35
	}

	rightHand = Entity()
	rightHand.animateTo(5, (0, 15))
	rightHand.repeatFrame(5)
	rightHand.animateTo(5, (10, -15), toAngle=-45)
	rightHand.repeatFrame(15)
	rightHand.animateTo(5, (0, 0), toAngle=0, clockwise=True)

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

	move = Move(entities)

	move.mileStones.update(milestones)

	return move
