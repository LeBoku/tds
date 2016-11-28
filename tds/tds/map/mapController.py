from pygame.math import Vector2

from base.controller import Controller
from config import mapBounds

from map.mapDisplay import MapDisplay
from mapEntity.MapEntityController import MapEntityController
from mapEntity.player.playerController import PlayerController

from mapEntity.subEntity.subEntity import SubEntity
from store import images
from store import moveSets

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
		self.box = self.addEntity(MapEntityController(self))
		self.box.setBaseImage(images.props.crate())
		self.box.coord = Vector2(400, 400)

		self.setUpPlayer()

	def setUpPlayer(self):
		self.player = self.addEntity(PlayerController(self))
		self.player.coord = Vector2(500, 400)
		
		self.player.moveSetController.registerMove("attack_forward", moveSets.spear.forwardAttack())
		self.player.moveSetController.registerMove("move", moveSets.character.move())
		
		self.createSubEntity("leftHand", images.character.hand(), Vector2(-5, 0))
		rightHand = self.createSubEntity("rightHand", images.character.hand(), Vector2(5, 0))

		self.createSubEntity("weapon", images.weapons.spear(), parent=rightHand)

	def createSubEntity(self, name, image, offset=Vector2(0,0), parent=None):
		if (parent is None):
			parent = self.player

		e = SubEntity(self)
		e.offsetVector = offset
		e.setBaseImage(image)

		parent.addSubEntity(name, e)

		return e

	def display(self):
		display = self.displayHandler.display()

		for entity in self.entities:
			coord = entity.coord
			if entity.offset is not None:
				coord += entity.offset.vector

			entityDisplay = entity.display()
			entityRect = entityDisplay.get_rect()
			entityRect.center = coord

			display.blit(entityDisplay, entityRect.topleft)

		return display