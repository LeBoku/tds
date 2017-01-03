class Collison:
	def __init__(self, initatior, target, initatiorPolygon, targetPolygon, intersection):
		self.intersection = intersection
		self.initatior = initatior
		self.target = target
		self.initatiorPolygon = initatiorPolygon
		self.targetPolygon = targetPolygon

	@property
	def direction(self):
		pass