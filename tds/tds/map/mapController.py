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
		self.collisionEntities = []

		self.bounds = mapBounds

		self.setUpEntities()

	def setUpDisplayHandler(self):
		self.displayHandler = MapDisplay(self)

	def addEntity(self, entity):
		self.entities.append(entity)
		return entity

	def addCollisionEntity(self, entity, collisionPoints):
		entity.collisionPoints = collisionPoints
		self.collisionEntities.append(entity)

	def isCollidingWithSomeThing(self, collisionPolygon):
		isCollididing = False
		for entity in self.collisionEntities:
			if entity is not None:
				isCollididing = entity.isCollidingWith(collisionPolygon)
				if isCollididing:
					break

		return isCollididing

	def removeEntity(self, entity):
		self.entities.remove(entity)
	
	def setUpEntities(self):
		box = self.addEntity(MapEntityController(self))
		box.setBaseImage(images.props.crate())
		box.coord = Vector2(400, 400)
		self.addCollisionEntity(box, [(-10, -10),
			(10, -10),
			(10, 10),
			(-10, 10)])

		self.setUpPlayer()

	def setUpPlayer(self):
		self.player = self.addEntity(PlayerController(self))
		self.player.setBaseImage(images.character.player())
		
		self.player.collisionPoints = [(-3, -1.5),
			(3, -1.5),
			(3, 1.5),
			(-3, 1.5),]

		self.player.coord = Vector2(500, 400)
		
		self.player.moveSetController.registerMove("attack_forward", moveSets.spear.forwardAttack())
		self.player.moveSetController.registerMove("move", moveSets.character.move())
		
		self._createSubEntity("leftHand", images.character.hand(), Vector2(-5, 0))
		rightHand = self._createSubEntity("rightHand", images.character.hand(), Vector2(5, 0))

		self._createSubEntity("weapon", images.weapons.spear(), parent=rightHand)

	def _createSubEntity(self, name, image, offset=Vector2(0,0), parent=None):
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