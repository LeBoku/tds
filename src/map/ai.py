from store.perception.eye import Eye


class Ai:
	def __init__(self, character, map):
		self.character = character
		self.map = map

		self.percivers = []
		self.setUpPercivers()

		self.perceptionListeners = []
		self.setUpPerceptionListeners()

	def setUpPercivers(self):
		self.percivers.append(Eye(self.character, self.map))

	def setUpPerceptionListeners(self):
		pass

	def loopCall(self):
		for perception in self.percive():
			for listener in self.perceptionListeners:
				if listener.applies(perception):
					listener.call(perception)

	def percive(self):
		percivedThings = []

		for perciver in self.percivers:
			percivedThings.extend(perciver.percive())

		return percivedThings

	def lookTowardsEntity(self, entity):
		distance_vector = self.getDistanceVectorToMapEntity(entity)
		self.character.angle = distance_vector.angle_to((0, -1))

	def getDistanceVectorToMapEntity(self, entity):
		distance_vector = entity.coord - self.character.coord

		return distance_vector

	def moveTowardsMapEntity(self, entity, threshold, leeway = 5):
		distance_vector = self.getDistanceVectorToMapEntity(entity)
		distance = distance_vector.length()

		if threshold + leeway > distance > threshold - leeway:
			self.character.setDestination(None)

		elif distance < threshold:
			distance_vector.rotate(180)
			distance_vector.scale_to_length(threshold - distance)
			self.character.setDestination(distance_vector)

		elif distance > threshold:
			distance_vector.scale_to_length(distance - threshold)
			self.character.setDestination(self.character.coord + distance_vector)