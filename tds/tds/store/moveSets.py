from collections import namedtuple
from copy import deepcopy

from pygame.math import Vector2

def spear():
	move = getMoveBase()
	move["frames"].extend(animate({
			"weapon": Vector2(0, 0)
		}, {
			"weapon": Vector2(0, 15)
		}, 3))
	move["frames"].extend(animate({
			"weapon": Vector2(0, 15)
		}, {
			"weapon": Vector2(0, -30)
		}, 3))

	move["frames"].extend(animate({
			"weapon": Vector2(0, -30)
		}, {
			"weapon": Vector2(0, 0)
		}, 3))

	return move

def getMoveBase():
	move = {"frames": []}
	return move

def animate(fromState: Vector2, toState: Vector2, frameCount):
	keys = fromState.keys()
	frames = [fromState]
	framesInfo = {}

	for key in keys:
		fromVector = fromState[key]
		toVector = toState[key]
		info = {}

		difference = toVector - fromVector

		info["direction"] = difference.normalize()
		info["distance"] = fromVector.distance_to(toVector) / frameCount
		
		framesInfo[key] = info
		

	for frameNumber in range(1, frameCount + 1):
		frameData = {}

		for key in keys:
			info = framesInfo[key]
			
			movement = Vector2(info["direction"].x, info["direction"].y)
			movement.scale_to_length(frameNumber * info["distance"])
			frameData[key] = movement + fromVector

		frames.append(frameData)

	return frames