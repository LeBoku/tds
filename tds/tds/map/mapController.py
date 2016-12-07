from pygame.math import Vector2
from pygame import gfxdraw, Surface

from base.controller import Controller
from base.types.dicts import DotDict
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

		self.showCollisions = True
		self.collisionColor = (255,0,0)

	def setUpDisplayHandler(self):
		self.displayHandler = MapDisplay(self)

	def addEntity(self, entity):
		self.entities.append(entity)
		return entity

	def addCollisionEntity(self, entity, collisionPoints):
		entity.collisionPoints = collisionPoints
		self.collisionEntities.append(entity)

	def isCollidingWithSomeThing(self, initiator):
		collisionResult = DotDict(isColliding = False, 
			collisions=[])

		for entity in self.collisionEntities:
			if entity is not None:
				collision = entity.isCollidingWith(initiator)
				if collision is not None:
					collisionResult.isColliding = True
					collisionResult.collisions.append(collision)
					

		return collisionResult

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
		self.player.setUpSubEntities()

	def display(self):
		display = self.displayHandler.display()

		for entity in self.entities:
			entity.loopCall()
			coord = entity.coord
			if entity.offset is not None:
				coord += entity.offset.vector

			entityDisplay = entity.display()
			entityRect = entityDisplay.get_rect()
			entityRect.center = coord

			display.blit(entityDisplay, entityRect.topleft)

		if self.showCollisions:
			entities = self.collisionEntities.copy()
			entities.append(self.player.weapon)

			for entity in entities:
				polygonPoints = []
				polygon =  entity.collisionPolygon
				for x,y in polygon.exterior.coords:
					polygonPoints.append((int(x), int(y)))

				gfxdraw.filled_polygon(display, polygonPoints, self.collisionColor)

		return display