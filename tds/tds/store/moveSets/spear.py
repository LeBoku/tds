from .entity import Entity
from .move import Move

def forwardAttack():
	weapon = Entity((0, 0))
	weapon.animateTo((0, 10), 5)
	weapon.repeatFrame(5)
	weapon.animateTo((0, -20), 5)
	weapon.animateTo((0, 0), 5)
		
	move = Move(weapon=weapon)

	return move