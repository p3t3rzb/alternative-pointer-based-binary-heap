class heap:
	class __node__:
		def __init__(self,key,l,r,p,bfr,afr):
			self.key = key
			self.l = l
			self.r = r
			self.p = p
			self.bfr = bfr
			self.afr = afr
	def __init__(self):
		self.n = 0
		self.root = None
		self.last = None
		self.lastparent = None
	def push(self,key):
		if self.n == 0:
			self.root = [self.__node__(key,None,None,None,None,None)]
			self.last = self.root
			self.lastparent = self.root
		else:
			v = [self.__node__(key,None,None,None,self.last,None)]
			self.last[0].afr = v
			self.last = v
			if self.lastparent[0].r:
				self.lastparent = self.lastparent[0].afr
				self.lastparent[0].l = v
			elif self.lastparent[0].l:
				self.lastparent[0].r = v
			else:
				self.lastparent[0].l = v
			v[0].p = self.lastparent
			while v[0].p:
				if v[0].key < v[0].p[0].key:
					t = v[0].key
					v[0].key = v[0].p[0].key
					v[0].p[0].key = t
				else:
					break
				v = v[0].p
		self.n += 1
	def pop(self):
		if self.n == 1:
			self.root = None
			self.last = None
			self.lastparent = None
			self.n -= 1
		elif self.n:
			temp = self.last
			if self.lastparent[0].r:
				self.lastparent[0].r = None
			else:
				self.lastparent[0].l = None
				if self.n > 3:
					self.lastparent = self.lastparent[0].bfr
			self.root[0].key = temp[0].key
			self.last = self.last[0].bfr
			self.last[0].afr = None
			del temp
			temp = self.root
			while temp[0].l:
				s = temp[0].l
				if temp[0].r:
					if temp[0].r[0].key < s[0].key:
						s = temp[0].r
				if s[0].key < temp[0].key:
					t = s[0].key
					s[0].key = temp[0].key
					temp[0].key = t
				else:
					break
				temp = s
			self.n -= 1
	def top(self):
		return self.root[0].key
	def size(self):
		return self.n
	def empty(self):
		return self.n==0
	def __free__(self,v):
		if v:
			self.__free__(v[0].l)
			self.__free__(v[0].r)
			del v
	def __del__(self):
		self.__free__(self.root)
