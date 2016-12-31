from enum import Enum

class AttackTypes(Enum):
	left = 0
	forward = 1
	right= 2

class DefaultMilestones(Enum):
	end = 1

class AttackMilestones(Enum):
	woundUp = 2
	attacked = 4
	cooledDown = 6

class WalkMilestones(Enum):
	halfWay = 1