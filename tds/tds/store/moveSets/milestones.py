from enum import Enum

class DefaultMilestones(Enum):
	end = 1

class AttackMilestones(Enum):
	windUp = 1
	woundUp = 2
	attack = 3
	attacked = 4
	coolDown = 5
	cooledDown = 6

class WalkMilestones(Enum):
	halfWay = 1
	