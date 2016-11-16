class DisplayHandler:
	def __init__(self, controller):
		self.controller = controller
		self.baseImage = None

		self.setUpBaseImage()

	def setUpBaseImage(self):
		pass

	def display(self):
		return self.baseImage.copy()