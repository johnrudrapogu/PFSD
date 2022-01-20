class Employee(object):
	def __init__(self, first, last, sal):
		self.first = first
		self.last = last
		self.sal = sal
	@property
	def email(self):
		return '{}.{}@email.com'.format(self.first, self.last)
	def fullname(self):
		return '{}{}'.format(self.first, self.last)
	@property
	def fullname(self):
		return '{}{}'.format(self.first, self.last)
	@fullname.setter
	def fullname(self, name):
		first, last = name.split(' ')
		self.first = first
		self.last = last
	@fullname.deleter
	def fullname(self):
		self.first = None
		self.last = None	
		print('Property Deleted')
	def__repr__(self):
	return 'Employee {}'.format(self.first)
	def		
	
		
