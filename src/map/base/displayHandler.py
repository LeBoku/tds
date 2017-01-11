class DisplayHandler:
	def __init__(self, controller):
		self.controller = controller
		self.baseImage = None
		self.needsCopy = True
		self.setUpBaseImage()

	@property
	def dimensions(self):
		return self.baseImage.get_size()

	def setUpBaseImage(self):
		pass

	def display(self):
		if self.baseImage is not None:
			if self.needsCopy:
				image = self.baseImage.copy()
			else:
				image = self.baseImage

			return image
