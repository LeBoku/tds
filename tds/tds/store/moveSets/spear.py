from ._entity import Entity
from ._move import Move

from .milestones import AttackMilestones

def forwardAttack():
	milestones = {
		AttackMilestones.windUp: 0,
		AttackMilestones.woundUp: 10,
		AttackMilestones.attack: 10,
		AttackMilestones.attacked: 30,
		AttackMilestones.coolDown: 30,
		AttackMilestones.cooledDown: 35
	}

	rightHand = Entity()
	rightHand.animateTo(5, (0, 10))
	rightHand.repeatFrame(5)
	rightHand.animateTo(5, (0, -10))
	rightHand.repeatFrame(15)
	rightHand.backToDefault(5)
		
	leftHand = Entity()
	leftHand.animateTo(10, (0, -10))
	leftHand.animateTo(5, (0, 5))
	leftHand.repeatFrame(10)
	leftHand.backToDefault(5)

	weapon = Entity()
	weapon.repeatFrame(10)
	weapon.animateTo(5, (0,-15))
	weapon.repeatFrame(15)
	weapon.backToDefault(5)

	character = Entity()
	character.animateTo(5, toAngle=-45)
	character.repeatFrame(5)
	character.animateTo(5, toAngle=45, clockwise=True)
	character.repeatFrame(15)
	character.backToDefault(5)

	move = Move(rightHand=rightHand,
		leftHand=leftHand,
		weapon=weapon,
		character=character)

	move.mileStones.update(milestones)

	return move