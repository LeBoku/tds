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
			if(self.activeFrameNr < self.moveLength):
				self.activeFrameNr += 1
			else:
				self.activeFrameNr = None

			
	def getOffsetForEntity(self, entity):
		if self.isActive:
			if(entity in self.entities):
				return self.entities[entity].getOffsetForFrame(self.activeFrameNr)
