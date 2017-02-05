from enum import Enum


class MoveTypes(Enum):
	walk = 0
	dodge = 1
	attackForward = 2
	attackLeft = 3
	attackRight = 4


attackTypes = [
	MoveTypes.attackForward,
	MoveTypes.attackRight,
	MoveTypes.attackLeft
]


class CharacterParts(Enum):
	character = 0
	torso = 1
	leftHand = 2
	rightHand = 3
	weapon = 4


class WalkMilestones(Enum):
	halfWay = 1


class DefaultMilestones(Enum):
	end = 1


class PerceptionTypes(Enum):
	gainSight = 1
	inSight = 2
	lostSight = 3


class AttackMilestones(Enum):
	woundUp = 2
	attackOver = 3
	attacked = 4
	cooledDown = 6
