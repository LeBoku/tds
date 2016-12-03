from enum import Enum

class Default(Enum):
	end = 1

class Attack(Enum):
	windUp = 1
	woundUp = 2
	attack = 3
	attacked = 4
	coolDown = 5
	cooledDown = 6

class Walk(Enum):
	halfWay = 1
	