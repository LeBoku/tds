from store.images import util


def crate():
	img = util.createAlphaSurface((40, 40))
	img.fill((0,255,0))
	
	return img


def boundry(rect, color):
	return util.createSurface(rect.size, color)

