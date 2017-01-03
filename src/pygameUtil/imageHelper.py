from pygame import gfxdraw, Rect, image, Surface

def loadImage(path, isTransparent=True):
	img = image.load(path)
	if isTransparent:
		img = img.convert_alpha()
	else:
		img = img.convert()
	return img

def drawShapelyPolygon(onto, polygon, color):
	polygonPoints = []

	for x,y in polygon.exterior.coords:
		polygonPoints.append((int(x), int(y)))

	gfxdraw.filled_polygon(onto, polygonPoints, color)