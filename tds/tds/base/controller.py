from base.displayHandler import DisplayHandler

class Controller:
	def __init__(self):
		self.displayHandler = DisplayHandler()
		self.registerEvents()
		return super().__init__()

	def display(self, display):
		return self.displayHandler.display(display)

	def registerEvents(self):
		pass