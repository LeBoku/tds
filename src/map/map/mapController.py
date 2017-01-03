from pygame.math import Vector2
from pygame import gfxdraw, Surface

from map.base.controller import Controller
from config import mapBounds

from pygameUtil import imageHelper

from map.map.mapDisplay import MapDisplay
from map.mapEntityController import MapEntityController
from map.characters.playerController import PlayerController
from map.subEntity import SubEntity

from store import images
from store import moveSets
from store.types.dicts import Particle


from store.types.dicts import DotDict

class MapController(Controller):
	def __init__(self):
		super().__init__()
		self.player = None
		self.entities = []
		self.collisionEntities = []
		self.particles = []

		self.bounds = mapBounds

		self.setUpEntities()

		self.showCollisions = False
		self.collisionColor = (255, 0, 0)

	def setUpDisplayHandler(self):
		self.displayHandler = MapDisplay(self)

	def addEntity(self, entity):
		self.entities.append(entity)
		return entity

	def addParticle(self, particle):
		self.particles.append(particle)

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
			if entityDisplay is not None:
				entityRect = entityDisplay.get_rect()
				entityRect.center = coord

				display.blit(entityDisplay, entityRect.topleft)

		if self.showCollisions:
			self.particles.append(Particle(self.player.weapon.collisionPolygon, self.collisionColor))

			for entity in self.collisionEntities:
				self.particles.append(Particle(entity.collisionPolygon, self.collisionColor))

		for particle in self.particles:
			imageHelper.drawShapelyPolygon(display, particle.polygon, particle.color)

		self.particles = []

		return display