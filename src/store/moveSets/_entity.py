from pygame.math import Vector2

from ._offset import Offset

class Entity:
	def __init__(self, startVector=Vector2(0,0)):
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

	def backToDefault(self, frameCount):
		self.animateTo(frameCount, self.defaultOffset.vector)

	def rotateAround(self, frameCount, byAngle, around=(0, 0)):
		fromAngle = self.frames[-1].angle
		rotationCenter = Vector2(around)

		stepAngle = byAngle/ frameCount

		frames = []
		lastFrame = self.frames[-1]
		for i in range(frameCount):
			differenceVector = rotationCenter - lastFrame.vector
			newAngle = (lastFrame.angle - stepAngle) % 360

			rotatedVector = differenceVector.rotate(stepAngle)
			newPos = rotationCenter - rotatedVector

			lastFrame = Offset(newPos, newAngle)
			frames.append(lastFrame)
	
		self.frames.extend(frames)	

	def animateTo(self, frameCount, toVector=(0,0), toAngle=0, clockwise=False):
		toFrame = Offset(Vector2(toVector), toAngle)
		fromFrame = self.frames[-1]
		frames = []
	
		if clockwise:
			stepAngle = (fromFrame.angle + 360) - (toFrame.angle + 360)
		else:
			stepAngle = (toFrame.angle + 360) - (fromFrame.angle + 360)

		if stepAngle != 0:
			stepAngle /= frameCount  

		stepVector = toFrame.vector - fromFrame.vector
		if stepVector.length() > 0:
			stepVector.scale_to_length(stepVector.length() / frameCount)

		lastFrame = fromFrame

		for frameNumber in range(frameCount):
			angle = (lastFrame.angle + stepAngle) % 360
			offset = lastFrame.vector + stepVector

			lastFrame = Offset(offset, angle)
			frames.append(lastFrame)
		
		self.frames.extend(frames)
			