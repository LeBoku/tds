from store.enums import DefaultMilestones


class Move:
	def __init__(self, entities):
		self.entities = entities

		self.loop = False

		self.moveLength = 0
		self.initMoveLength()

		self.activeFrameNr = None
		self.activeFrameListeners = {}
		self.initActiveFrameData()

		self.mileStones = {
			DefaultMilestones.end: self.moveLength + 1 # #not called by its frame Number
		}

	def initMoveLength(self):
		for key, entity in self.entities.items():
			length = len(entity.frames)
			if length > self.moveLength:
				self.moveLength = length

	def initActiveFrameData(self):
		self.activeFrameNr = None
		self.loop = False
		self.activeFrameListeners = {}

	@property
	def isActive(self):
		return self.activeFrameNr is not None

	@property
	def framesLeft(self):
		if self.isActive:
			return self.moveLength - self.activeFrameNr

	def start(self):
		if not self.isActive:
			self._start()
			self.loop = False

		return self

	def startLoop(self):
		if not self.isActive:
			self._start()
			self.loop = True

		return self

	def stop(self, callEndListeners=False):
		listeners = []
		if callEndListeners and DefaultMilestones.end in self.activeFrameListeners:
			listeners = self.activeFrameListeners[DefaultMilestones.end].copy()

		self.initActiveFrameData()
	
		for listener in listeners:
			listener()
	
		return self

	def hasPassedMileStone(self, mileStone):
		return self.mileStones[mileStone] < self.activeFrameNr

	def listenForMilestone(self, mileStone, listener):
		if mileStone not in self.activeFrameListeners:
			self.activeFrameListeners[mileStone] = []

		self.activeFrameListeners[mileStone].append(listener)

	def listenForEnd(self, listener):
		self.listenForMilestone(DefaultMilestones.end, listener)

	def moveOn(self):
		if self.isActive:
			if self.activeFrameNr < self.moveLength:
				self.activeFrameNr += 1
			else:
				if self.loop:
					self.activeFrameNr = 0
				else:
					self.stop(True)
		
			self._dealWithListeners()
			
	def getOffsetForEntity(self, entity):
		if self.isActive:
			if entity in self.entities:
				return self.entities[entity].getOffsetForFrame(self.activeFrameNr)

	def _dealWithListeners(self):
		for key, mileStone in self.mileStones.items():
			if mileStone == self.activeFrameNr:
				self._callListeners(key)

	def _callListeners(self, mileStone):
		if mileStone in self.activeFrameListeners:
			for listener in self.activeFrameListeners[mileStone]:
				listener()

	def _start(self):
		self.initActiveFrameData()
		self.activeFrameNr = -1