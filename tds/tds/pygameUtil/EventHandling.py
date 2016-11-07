import traceback

import pygame.event
import pygame.locals

class EventListener:
	def __init__(self, type, **conditions):
		super().__init__()
		self.conditions = conditions
		self.type = type
		self.eventHandler = EventHandler.get()

	def __call__(self, f):
		def func(ev):
			if self.checkConditions(ev):
				return f(ev)
		
		self.eventHandler.addEventListener(self.type, func)
		self.func = func
		return func

	def destroy(self):
		self.eventHandler.removeEventListener(self.type, self.func)

	def checkConditions(self, ev):
		isValid = True

		for arg in self.conditions:
			if arg in ev.dict or arg == "type":
				isValid = (getattr(ev, arg) == self.conditions[arg]) or (hasattr(self.conditions[arg], "__contains__") and getattr(ev, arg) in self.conditions[arg])

			elif arg=="checkFuncs":
				funcs = []
				funcs.append(self.conditions[arg])
				tmp = []
				tmp.extend(funcs)

				for f in tmp:
					isValid = f(ev)
					if not isValid: 
						break

			else:
				isValid = False
				
			if not isValid:
				break

		return isValid

class EventHandler:
	_instance = None

	@staticmethod
	def get():
		if not EventHandler._instance:
			EventHandler._instance = EventHandler()
		return EventHandler._instance

	def __init__(self):
		self.eventListener = {}
		self.pressedMouseButtons = {}
		self.pressedKeys = {}

	def postCustomEvents(self):
		self.postMouseButtonIsDownEvents()
		self.postKeyIsDownEvents()

	def postMouseButtonIsDownEvents(self):
		for button in self.pressedMouseButtons:
			self.pressedMouseButtons[button] += 1
			self.postCustomEvent(subType="MOUSE_BUTTON_IS_DOWN", button=button, pos=pygame.mouse.get_pos(), downForLoops=self.pressedMouseButtons[button])

	def postKeyIsDownEvents(self):
		for key in self.pressedKeys:
			self.pressedKeys[key] += 1
			self.postCustomEvent(subType="KEY_IS_DOWN", key=key, downForLoops=self.pressedKeys[key])

	def postCustomEvent(self, **attrs):
		ev = pygame.event.Event(pygame.locals.USEREVENT, attrs) 
		pygame.event.post(ev)
		
	def getMouseButtonIsDown(self, button):
		return button in self.pressedMouseButtons

	def isKeyDown(self, key):
		return key in self.pressedKeys

	def isAnyKeyDown(self, keys=None):
		areDown = False

		if keys is not None:
			for key in keys:
				areDown = key in self.pressedKeys
				if areDown:
					break 
		else:
			areDown = len(self.pressedKeys) >= 0

		return areDown

	def orderKeysByLoopsDown(self, keys=None):
		keysToTest = {}

		if keys is not None:
			for key in keys:
				if key in self.pressedKeys:
					keysToTest[key] = self.pressedKeys[key]
		else:
			keysToTest = self.pressedKeys

		return sorted(keysToTest, key=keysToTest.get)

	def addEventListener(self, type, listener):
		try:
			self.eventListener[type].append(listener)
		except KeyError:
			self.eventListener[type] = [listener]

	def removeEventListener(self, type, listener):
		self.eventListener[type].remove(listener) 
		   
		if len(self.eventListener[type]) <= 0:
			del self.eventListener[type]

	def handleCurrentEvent(self, ev):
		if ev.type == pygame.MOUSEBUTTONDOWN:
			self.pressedMouseButtons[ev.button] = 0

		elif ev.type == pygame.MOUSEBUTTONUP:
			del self.pressedMouseButtons[ev.button]

		elif ev.type == pygame.KEYDOWN:
			self.pressedKeys[ev.key] = 0

		elif ev.type == pygame.KEYUP:
			del self.pressedKeys[ev.key]

	def handleEvents(self):
		for ev in pygame.event.get():
			self.handleCurrentEvent(ev)
			type = ev.type if ev.type != pygame.locals.USEREVENT else ev.subType
			if type in self.eventListener:
				for listener in self.eventListener[type]:
					flag = listener(ev)

					if flag is not None and flag == False:
						break

