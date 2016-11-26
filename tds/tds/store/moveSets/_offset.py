from pygame.math import Vector2

class Offset:
	def __init__(self, vector=Vector2(0,0), angle=0):
		self.vector = vector
		self.angle = angle

	def copy(self):
		return Offset(self.vector, self.angle)