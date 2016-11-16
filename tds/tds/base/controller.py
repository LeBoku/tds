from base.displayHandler import DisplayHandler

class Controller:
	def __init__(self):
		self.displayHandler = DisplayHandler(self)
		self.registerEvents()
		return super().__init__()

	def setBaseImage(self, baseImage):
		self.displayHandler.baseImage = baseImage

	def display(self):
		return self.displayHandler.display()

	def registerEvents(self):
		pass