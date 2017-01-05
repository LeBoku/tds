from store.images import util


def player():
	img = util.createAlphaSurface((10, 4))
	img.fill((0,0,0))
	
	return img


def hand():
	img = util.createAlphaSurface((4, 4))
	img.fill((0,0,0))

	return img