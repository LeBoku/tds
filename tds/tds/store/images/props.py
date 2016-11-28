from store.images import util

def crate():
	img = util.createAlphaSurface((15, 15))
	img.fill((0,0,0))
	
	return img