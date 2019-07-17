import pyservoce
import evalcache

class Unit:
	"""Базовый класс для использования в кинематических цепях и сборках

	Вычисляет свою текущую позицию исходя из дерева построения.
	Держит список наследников, позиция которых считается относительно него.    
	"""

	class ShapeView:
		def __init__(self, sctrl):
			self.sctrl = sctrl

		def set_location(self, trans):
			self.sctrl.set_location(trans)

		def hide(self, en):
			self.sctrl.hide(en)


	def __init__(self, 
				parent=None,
				shape=None,
				name=None, 
				location=pyservoce.libservoce.nulltrans()):    
		self.parent = parent
		self.shape = shape
		self.location = evalcache.unlazy_if_need(location)
		self.global_location = self.location
		self.name = name
		self.color = None

		self.views = set()
		self.childs = set()

		if parent is not None:
			parent.add_child(self)

	def add_child(self, child):
		child.parent = self
		self.childs.add(child)

	def link(self, child):
		self.add_child(child)

	def location_update(self):
		if self.parent is None:
			self.global_location = self.location

		else:
			self.global_location = self.parent.global_location * self.location

	def relocate(self, location, deep=False):
		self.location = evalcache.unlazy(location)
		if deep:
			self.location_update_deep()
		else:
			self.location_update()

	def location_update_deep(self):
		self.location_update()

		for c in self.childs:
			c.location_update_deep()

	def set_shape(self, shape):
		self.shape = shape

	def print_tree(self, tr=0):
		s = "\t" * tr + str(self) 
		print(s)
		
		for c in self.childs:
			c.print_tree(tr+1)

	def __str__(self):
		if self.name:
			n = self.name
		else:
			n = repr(self)

		if self.shape is None:
			h = "NullShape"
		else:
			h = self.shape.__lazyhexhash__[0:10]

		return str((n,h))

	def apply_view_location(self):
		for v in self.views:
			v.set_location(self.global_location)

	def bind_scene(self, scene, color=(1,1,1)):
		if self.shape is None:
			return

#		if color is None and self.color is None:
#			color = pyservoce.defs.DEFAULT_COLOR

#		if self.color is not None:
#			color = self.color

#		if not isinstance(color, pyservoce.libservoce.Color):
#			color = pyservoce.libservoce.Color(*color)

		shape_view = self.ShapeView(scene.add(
			evalcache.unlazy(self.shape), 
			color))
		scene.viewer.display(shape_view.sctrl)
		self.views.add(shape_view)

		self.apply_view_location()

	def bind_scene_deep(self, scene):
		self.bind_scene(scene)
		for c in self.childs:
			c.bind_scene_deep(scene)


	#ef update_global_location(self):
	#   if self.local_location is None:
	#       if self.parent is None:
	#           self.global_location = pyservoce.libservoce.nulltrans()
	#       else:
	#           self.global_location = self.parent.global_location
	#       return

	#   if self.parent is None:
	#       self.global_location = self.local_location
	#   else:
	#       self.global_location = self.parent.global_location * self.local_location

	#ef eval_location(self, location):
	#   trace("eval_location")
	#   if location is None:
	#       self.local_location = None
	#   else:
	#       self.local_location = (
	#           location.unlazy() if isinstance(location, LazyObject) else location
	#       )
	#   self.update_global_location()

	#ef set_location(self, location):
	#   trace("set_location")
	#   self.eval_location(location)
	#   self.apply_location()

	#ef apply_location(self):
	#   raise NotImplementedError()

class CynematicUnit(Unit):
	def __init__(self, **kwargs):
		super().__init__(**kwargs)
		self.output = Unit(parent=self)

	def link(self, arg):
		self.output.link(arg)

class RotateConnector(Unit):
	def __init__(self, **kwargs):
		super().__init__(**kwargs)