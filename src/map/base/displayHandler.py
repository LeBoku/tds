class DisplayHandler:
	def __init__(self, controller):
		self.controller = controller
		self.baseImage = None

		self.setUpBaseImage()

	@property
	def dimensions(self):
		return self.baseImage.get_size()

	def setUpBaseImage(self):
		pass

	def display(self):
		if self.baseImage is not None:
			return self.baseImage.copy()