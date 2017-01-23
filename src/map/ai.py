
class Ai:
	def __init__(self, character):
		self.character = character

	def loopCall(self):
		pass

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