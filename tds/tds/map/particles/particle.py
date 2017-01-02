from map.mapEntityController import MapEntityController

from .particleDisplay import ParticleDisplay

class Particle(MapEntityController):
	def __init__(self, map):
		super().__init__(map)
		
	def setDimensions(self):
		pass

	def setUpDisplayHandler(self):
		self.displayHandler = ParticleDisplay()