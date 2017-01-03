from enum import Enum


class Default(Enum):
	end = 1


class Attack(Enum):
	woundUp = 2
	attacked = 4
	cooledDown = 6


class Walk(Enum):
	halfWay = 1
