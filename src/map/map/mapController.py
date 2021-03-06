from pygame import Rect
from pygame.math import Vector2

import config
from config import mapBounds
from map.base.controller import Controller
from map.characters.enemy.enemyController import EnemyController
from map.characters.player.playerController import PlayerController
from map.map.mapDisplay import MapDisplay
from map.mapEntityController import MapEntityController
from map.props.boundry import Boundry
from pygameUtil import imageHelper
from store import images
from store.types.dicts import Particle, DotDict


class MapController(Controller):
	def __init__(self):
		super().__init__()
		self.player = None
		self.entities = []
		self.collisionEntities = []
		self.particles = []

		self.bounds = mapBounds

		self.setUpEntities()

		self.collisionColor = (255, 0, 0)

	def setUpDisplayHandler(self):
		self.displayHandler = MapDisplay(self)

	def addEntity(self, entity):
		self.entities.append(entity)
		return entity

	def addParticle(self, particle):
		self.particles.append(particle)

	def addCollisionEntity(self, entity):
		self.collisionEntities.append(entity)

	def isCollidingWithSomeThing(self, initiator):
		collisionResult = DotDict(isColliding=False, collisions=[])

		for entity in self.collisionEntities:
			if entity is not None:
				collision = entity.isCollidingWith(initiator)
				if collision is not None:
					collisionResult.isColliding = True
					collisionResult.collisions.append(collision)

		return collisionResult

	def getEntitesInsideShape(self, shape):
		entities = []
		for entity in self.entities:
			poly = entity.collisionPolygon
			if poly is not None and poly.intersects(shape):
				entities.append(entity)

		return entities

	def removeEntity(self, entity):
		self.entities.remove(entity)
	
	def setUpEntities(self):
		box = self.addEntity(MapEntityController(self))
		box.setBaseImage(images.props.crate())
		box.coord = Vector2(400, 400)
		box.collisionPoints = [
			(-20, -20),
			(20, -20),
			(20, 20),
			(-20, 20)
		]

		self.addCollisionEntity(box)

		self.player = self.addEntity(PlayerController(self))
		self.player.coord = Vector2(500, 400)

		enemy = self.addEntity(EnemyController(self))
		enemy.coord = Vector2(500, 300)

		self.setUpBoundry()

	def setUpBoundry(self):
		boundryWidth = 15

		boundryRects = [
			Rect((0, 0), (config.mapBounds[0], boundryWidth)),
			Rect((0, 0), (boundryWidth, config.mapBounds[1])),
			Rect((config.mapBounds[0] - boundryWidth, 0), (boundryWidth, 2000)),
			Rect((0, config.mapBounds[1]-boundryWidth), (config.mapBounds[0], boundryWidth))
		]

		color = (0, 0, 0)
		boundries = []

		for boundry in boundryRects:
			boundries.append(Boundry(self, boundry, color))

		for boundry in boundries:
			self.addEntity(boundry)

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

		if config.debug:
			if self.player.isAttacking:
				self.particles.append(Particle(self.player.weapon.collisionPolygon, self.collisionColor))

			for entity in self.collisionEntities:
				self.particles.append(Particle(entity.collisionPolygon, self.collisionColor))

		for particle in self.particles:
			imageHelper.drawShapelyPolygon(display, particle.polygon, particle.color)

		self.particles = []

		return display
