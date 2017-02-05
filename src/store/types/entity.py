from pygame.math import Vector2

from .offset import Offset


class Entity:
	def __init__(self, startVector=Vector2(0, 0), startAngle=0):
		self.frames = [Offset(Vector2(startVector), startAngle)]
		self.defaultOffset = Offset()

	def getOffsetForFrame(self, frameNr):
		if len(self.frames) > frameNr: 
			return self.frames[frameNr]
		else:
			return self.defaultOffset

	def repeatFrame(self, count=1, vector=None, angle=None):
		lastOffset = self.frames[-1]

		vector = vector if vector is not None else lastOffset.vector
		angle = angle if angle is not None else lastOffset.angle

		for i in range(count):
			self.frames.append(Offset(vector, angle))

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
			fromAngle = fromFrame.angle + 360
			toAngle = toFrame.angle + 360

			if fromAngle > toAngle:
				stepAngle = ~int(fromAngle - (toAngle + 360))
			else:
				stepAngle = fromAngle - toAngle

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
