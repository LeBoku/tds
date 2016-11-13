from base.displayHandler import DisplayHandler

class Controller:
	def __init__(self):
		self.displayHandler = DisplayHandler(self)
		self.registerEvents()
		return super().__init__()

	def display(self):
		return self.displayHandler.display()

	def registerEvents(self):
		pass