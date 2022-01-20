class Bank(object):
	minbal = 1000
	def __init__(self, accno, name, bal):
		self.accno = accno
		self.name = name
		self.bal = bal
		