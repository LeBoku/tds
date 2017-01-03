from ._entity import Entity
from ._move import Move

from .milestones import Attack

def rightAttack():
	milestones = {
		Attack.woundUp: 25,
		Attack.attacked: 50,
		Attack.cooledDown: 60
	}

	rightHand = Entity();
	rightHand.animateTo(5, (5, -3), -35)
	rightHand.repeatFrame(15)
	rightHand.rotateAround(5, -60)
	rightHand.repeatFrame(15)
	rightHand.backToDefault(10)
	
	weapon = Entity()
	weapon.animateTo(5, (0, -10))
	weapon.repeatFrame(40)
	weapon.backToDefault(5)
	weapon.repeatFrame(5)
	

	move = Move(rightHand=rightHand,weapon=weapon)
	move.mileStones.update(milestones)
	return move

def leftAttack():
	milestones = {
		Attack.woundUp: 30,
		Attack.attacked: 40,
		Attack.cooledDown: 65
	}

	rightHand = Entity()
	rightHand.rotateAround(15, -200, (-7, 0))
	rightHand.repeatFrame(15)
	rightHand.rotateAround(10, 300, (-7, 0))
	rightHand.repeatFrame(15)
	rightHand.backToDefault(20) # AllPlanned rotates the wrong way but its cool. correct would be: rightHand.rotateAround(10, -100, (-7, 0))
	
	weapon = Entity()
	weapon.repeatFrame(30)
	weapon.animateTo(5, (0, -15))
	weapon.repeatFrame(20)
	weapon.backToDefault(20)

	move = Move(rightHand=rightHand, weapon=weapon)
	move.mileStones.update(milestones)

	return move

def forwardAttack():
	milestones = {
		Attack.woundUp: 10,
		Attack.attacked: 30,
		Attack.cooledDown: 35
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