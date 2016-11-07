import math

def invertAngle(angle):
	return (angle + 180) % 360

def calcAngleBetweenPositions(pos1, pos2):
	bPos = (pos1[0] - pos2[0], pos1[1] - pos2[1])

	a = math.sqrt(bPos[0] ** 2 + bPos[1] ** 2)
	aPos = (0, a)
	c = math.sqrt(bPos[0] ** 2 + (aPos[1] + bPos[1]) ** 2)

	if a == 0:
		a = 1
	if c == 0:
		c = 1

	alpha = math.acos((a ** 2 - a ** 2 - c ** 2) / (-2 * a * c))
	alpha = math.degrees(alpha)

	angle = 180 - (2 * alpha)
	if bPos[0] > 0:
		angle = 360 - angle

	return (angle + 180) % 360

def calcNewPosByAngleAndDistance(pos, angle, distance):
	angle %= 360

	shortMoveAngle = angle % 90
	shortMoveAngle = math.radians(shortMoveAngle) 

	cos = math.cos(shortMoveAngle)

	c = distance
	b = c * cos
	a = math.sqrt(c ** 2 - b ** 2)

	moveDirection = angle // 90

	if moveDirection == 0:
		x = pos[0] - a
		y = pos[1] - b

	if moveDirection == 1:
		x = pos[0] - b
		y = pos[1] + a

	if moveDirection == 2:
		x = pos[0] + a
		y = pos[1] + b

	if moveDirection == 3:
		x = pos[0] + b
		y = pos[1] - a

	return int(x), int(y)

def calcDistanceBetweenPoses(pos1, pos2):
	a = abs(pos1[0] - pos2[0])
	b = abs(pos1[1] - pos2[1])

	c = math.sqrt(a * a + b * b)
	return c

def getDifferenceBetweenAngles(angle, checkAngle):
	angle %= 360
	checkAngle %= 360
	
	angleDiff = (angle - checkAngle + 180 + 360) % 360 - 180
	return angleDiff