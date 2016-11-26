from pygame.math import Vector2

from .offset import Offset

class Entity:
	def __init__(self, startVector):
		self.frames = [Offset(Vector2(startVector))]
		self.defaultOffset = Offset()

	def getOffsetForFrame(self, frameNr):
		if len(self.frames) > frameNr: 
			return self.frames[frameNr]
		else:
			return self.defaultOffset

	def repeatFrame(self, count=1):
		for i in range(count):
			self.frames.append(self.frames[-1].copy())

	def animateTo(self, toVector, frameCount=1):
		toFrame = Offset(Vector2(toVector))
		fromFrame = self.frames[-1]
		frames = []

		distanceVector = toFrame.vector - fromFrame.vector
		distanceVector.scale_to_length(distanceVector.length() / frameCount)

		lastFrame = fromFrame

		for frameNumber in range(frameCount):
			angle = 0
			offset = lastFrame.vector + distanceVector

			lastFrame = Offset(offset, angle)
			frames.append(lastFrame)
		
		self.frames.extend(frames)
			