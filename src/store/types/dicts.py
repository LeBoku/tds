class DotDict:
	def __init__(self, **kwargs):
		for key, value in kwargs.items():
			setattr(self, key, value)


class DodgeData:
	def __init__(self, vector, frameCount):
		self.vector = vector,
		self.frameCount = frameCount
		self.framesLeft = frameCount

	@property
	def isOngoing(self):
		return self.framesLeft > 0


class Particle:
	def __init__(self, polygon, color):
		self.polygon = polygon
		self.color = color
