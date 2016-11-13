from character.characterController import CharacterController
from player.playerDisplay import PlayerDisplay

class PlayerController(CharacterController):
	def __init__(self, map):
		super().__init__(map)
		self.displayHandler = PlayerDisplay(self)