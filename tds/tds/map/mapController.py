from base.controller import Controller
from config import mapBounds

from map.mapDisplay import MapDisplay
from player.playerController import PlayerController

from weapon.weaponController import WeaponController
from weapon import weaponBaseImages 

class MapController(Controller):
	def __init__(self):
		super().__init__()
		self.player = None
		self.entities = []

		self.displayHandler = MapDisplay(self)
		self.bounds = mapBounds

		self.setUpEntities()

	def addEntity(self, entity):
		self.entities.append(entity)

	def setUpEntities(self):	
		self.player = PlayerController(self)
		self.player.coord = [500, 400]
		
		spear = WeaponController(self)
		spear.setBaseImage(weaponBaseImages.spear())

		spear.coord = [510, 400]

		self.player.weapon = spear

		self.addEntity(self.player)
		self.addEntity(spear)
		

	def display(self):
		display = self.displayHandler.display()

		for entity in self.entities:
			entityDisplay = entity.display()

			entityRect = entityDisplay.get_rect()
			entityRect.center = entity.coord;

			display.blit(entityDisplay, entityRect.topleft)

		return display