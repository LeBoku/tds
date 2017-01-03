from map.base.displayHandler import DisplayHandler


class Controller:
	def __init__(self):
		self.displayHandler = None
		self.registerEvents()
		self.setUpDisplayHandler()
		return super().__init__()

	def setUpDisplayHandler(self):
		self.displayHandler = DisplayHandler(self)

	def setBaseImage(self, baseImage):
		self.displayHandler.baseImage = baseImage

	def display(self):
		return self.displayHandler.display()

	def registerEvents(self):
		pass
