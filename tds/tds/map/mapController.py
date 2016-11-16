from base.controller import Controller
from config import mapBounds

from map.mapDisplay import MapDisplay
from player.playerController import PlayerController

class MapController(Controller):
	def __init__(self):
		super().__init__()
		self.player = None
		self.entities = []

		self.displayHandler = MapDisplay(self)
		self.bounds = mapBounds

		self.setUpEntities()

	def setUpEntities(self):	
		self.player = PlayerController(self)
		self.player.coord = [500, 400]
		self.entities.append(self.player)

	def display(self):
		display = self.displayHandler.display()

		for entity in self.entities:
			entityDisplay = entity.display()

			entityRect = entityDisplay.get_rect()
			entityRect.center = entity.coord;

			display.blit(entityDisplay, entityRect.topleft)

		return display