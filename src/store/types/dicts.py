class DotDict:
	def __init__(self, **kwargs):
		for key, value in kwargs.items():
			setattr(self, key, value)


class Peception:
	def __init__(self, type, **data):
		self.type = type
		self.data = data


class Particle:
	def __init__(self, polygon, color):
		self.polygon = polygon
		self.color = color
