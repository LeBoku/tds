from base.controller import Controller
from player.playerDisplay import PlayerDisplay

class PlayerController(Controller):
	def __init__(self,):
		super().__init__()
		self.displayHandler = PlayerDisplay(self)