def clear():
	print("\033c\033[3J\033[2J\033[0m\033[H", end='')
class empty: pass
empty = empty()
class path:
	def __init__(self, chogame, func, parent=None, id=None, name=None):
		self.func = func
		self.parent = parent
		self.options = {}
		self.is_title = False
		self.chogame = chogame
		if id is not None:
			self.chogame.rooms[id] = [name, self]
		self.id = id
	def __call__(self, *args, **kwargs):
		clear()
		self.func(*args, **kwargs)
	def add_chogame_as_option(self, chogame, name=None, id=None, key=None):
		chogame.title_func.is_title = False
		chogame.title_func.parent = self
		self.option(name=name, id=id, key=key)(chogame.title_func)
	def option(self, name=None, id=None, key=None):
		if key is None:
			key = str(len(self.options)+1)
		if self.chogame.rooms.get(id) is not None:
			name, p = self.chogame.rooms.get(id)
			self.options[key] = [name, p]
			return
		def inner(func):
			if not (type(func)==path):
				p = path(self.chogame, func, self, id, name)
			else:
				p = func
			self.options[key] = [name, p]
			return p
		return inner
class context:
	def __init__(self, path_obj, parent=None, parent_ctx=None):
		self.path = path_obj
		if parent is None:
			self.parent = self.path.parent
		else:
			self.parent = parent
		if self.parent is None:
			self.ctx_chain = []
		else:
			self.ctx_chain = parent_ctx.ctx_chain
			self.ctx_chain.append(parent_ctx)
	def choice(self, back=empty):
		if self.path.is_title:
			back = empty
		if back is empty:
			back = self.parent is not None
		if back is True:
			back = 'Back'
		choicetext = '\n'.join([f'{key}: {cont[0]}' for key, cont in self.path.options.items()])
		if back:
			choicetext+='\nNothing: '+back
		choicetext+='\n> '
		while True:
			choice = input(choicetext)
			if choice=='' and back:
				self.back()
				return
			if self.path.options.get(choice):
				self.path.options[choice][1](context(self.path.options[choice][1], parent_ctx=self))
				return
	def back(self):
		self.parent(self.ctx_chain.pop(-1))
	def goto_room(self, room, *args):
		if type(room) == str:
			room = self.path.chogame.rooms[room][1]
		room(context(room, self.path, self), *args)
class CHOgame:
	def __init__(self):
		self.rooms = {}
	def title(self, func):
		self.title_func = path(self, func, None, 'title')
		self.title_func.is_title = True
		return self.title_func
	def __call__(self):
		return self.start()
	def room(self, name, id=None):
		if id is None:
			id = name
		def inner(func):
			p = path(self, func, None, id)
			self.rooms[id] = [name, p]
			return p
		return inner
	def start(self):
		self.title_func(context(self.title_func))