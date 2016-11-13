from base.controller import Controller
from config import mapBounds

from map.mapDisplay import MapDisplay
from player.playerController import PlayerController

class MapController(Controller):
	def __init__(self):
		super().__init__()
		self.displayHandler = MapDisplay(self)
		self.entities = []
		self.bounds = mapBounds
		
		player = PlayerController(self)
		self.entities.append(player)
		

	def display(self):
		for entity in self.entities:
			entityDisplay = entity.display()

		return self.displayHandler.display()