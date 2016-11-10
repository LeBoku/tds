from base.controller import Controller

from map.mapDisplay import MapDisplay

class MapCtrl(Controller):
	def __init__(self):
		super().__init__()
		self.displayHandler = MapDisplay()

	def display(self, display):
		return super().display(display)