from mapEntity.MapEntityController import MapEntityController

from character.characterDisplay import CharacterDisplay

class CharacterController(MapEntityController):
	def __init__(self, map):
		super().__init__(map)
		self.displayHandler = CharacterDisplay(self)