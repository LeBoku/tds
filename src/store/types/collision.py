class Collison:
	def __init__(self, initatior, target, initatiorPolygon, targetPolygon):
		self.initatior = initatior
		self.target = target
		self.initatiorPolygon = initatiorPolygon
		self.targetPolygon = targetPolygon

	@property
	def intersection(self):
		return self.targetPolygon.intersection(self.initiatorPolygon)

	@property
	def direction(self):
		pass