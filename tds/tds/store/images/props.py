from store.images import util

def crate():
	img = util.createAlphaSurface((20, 20))
	img.fill((0,255,0))
	
	return img