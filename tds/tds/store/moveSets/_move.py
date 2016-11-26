class Move:
	def __init__(self, **entities):
		self.entities = entities
		self.activeFrameNr = None
		self.moveLength = 0
		self.loop = False
		self.mayRestart = False
		
		for key, entity in self.entities.items():
			lenght = len(entity.frames)
			self.moveLength = lenght if lenght > self.moveLength else self.moveLength

	@property
	def isActive(self):
		return self.activeFrameNr is not None

	def start(self):
		if not self.isActive or self.mayRestart:
			self.activeFrameNr = -1
			self.loop = False

	def startLoop(self):
		if not self.isActive or self.mayRestart:
			self.activeFrameNr = -1
			self.loop = True

	def stop(self):
		self.activeFrameNr = None

	def moveOn(self):
		if self.isActive:
			if(self.activeFrameNr < self.moveLength):
				self.activeFrameNr += 1
			elif self.loop:
				self.activeFrameNr = 0
			else:
				self.stop()
			
	def getOffsetForEntity(self, entity):
		if self.isActive:
			if(entity in self.entities):
				return self.entities[entity].getOffsetForFrame(self.activeFrameNr)
