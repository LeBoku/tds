class Move:
	def __init__(self, **entities):
		self.entities = entities
		self.activeFrameNr = None
		self.moveLength = 0
		
		for key, entity in self.entities.items():
			lenght = len(entity.frames)
			self.moveLength = lenght if lenght > self.moveLength else self.moveLength

	@property
	def isActive(self):
		return self.activeFrameNr is not None

	def start(self):
		self.activeFrameNr = -1

	def moveOn(self):
		if self.isActive:
			self.activeFrameNr += 1
			
	def getOffsetForEntity(self, entity):
		if self.isActive:
			return self.entities[entity].getOffsetForFrame(self.activeFrameNr)
