from store.images import util


def player():
	img = util.createAlphaSurface((5, 2))
	img.fill((0,0,0))
	
	return img


def hand():
	img = util.createAlphaSurface((2, 2))
	img.fill((0,0,0))

	return img