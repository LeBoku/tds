from base.controller import Controller
from config import mapBounds

from map.mapDisplay import MapDisplay
from mapEntity.player.playerController import PlayerController

from mapEntity.weapon.weaponController import WeaponController
from store.images import weapons 

class MapController(Controller):
	def __init__(self):
		super().__init__()
		self.player = None
		self.entities = []

		self.bounds = mapBounds

		self.setUpEntities()

	def setUpDisplayHandler(self):
		self.displayHandler = MapDisplay(self)

	def addEntity(self, entity):
		self.entities.append(entity)
		return entity

	def removeEntity(self, entity):
		self.entities.remove(entity)
	
	def setUpEntities(self):	
		self.player = self.addEntity(PlayerController(self))
		self.player.coord = [500, 400]
		
		spear = WeaponController(self)
		spear.setBaseImage(weapons.spear())
		self.player.weapon = spear

	def display(self):
		display = self.displayHandler.display()

		for entity in self.entities:
			entityDisplay = entity.display()
			entityRect = entityDisplay.get_rect()
			entityRect.center = entity.coord;

			display.blit(entityDisplay, entityRect.topleft)

		return display