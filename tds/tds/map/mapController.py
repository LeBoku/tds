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
		self.setUpEntities()
		self.player = None

	def setUpEntities(self):	
		self.player = PlayerController(self)
		self.player.coord = 500, 400
		self.entities.append(self.player)

	def display(self):
		display = self.displayHandler.display()

		for entity in self.entities:
			entityDisplay = entity.display()
			
			display.blit(entityDisplay, entity.coord)

		return display