import pygame
import pygame.image


def rotateFast(img, angle):
    """
    rotate an image while keeping its center and size using just rotate witch is slightly 
    faster than rotozoom but also less accurate

    params:
        img -- the image to be rotated
        angle -- the counterclockwise angle for the rotation
    """
    rotImage = pygame.transform.rotate(img, angle)
    rotRect = img.get_rect()

    rotRect.center = rotImage.get_rect().center
    try:
        rotCutImage = rotImage.subsurface(rotRect)
    except ValueError:
        rotCutImage = rotImage

    return rotCutImage


def rotate(img, angle):
    """
    rotate an image while keeping its center and size

    params:
        img -- the image to be rotated
        angle -- the counterclockwise angle for the rotation
    """
    rotImage = pygame.transform.rotozoom(img, angle, 1)
    rotRect = img.get_rect()

    rotRect.center = rotImage.get_rect().center
    try:
        rotCutImage = rotImage.subsurface(rotRect)
    except ValueError:
        rotCutImage = rotImage

    return rotCutImage


def loadImage(path, isTransparent=True):
	img = pygame.image.load(path)
	if isTransparent:
		img = img.convert_alpha()
	else:
		img = img.convert()
	return img