class Student:
	clg = "KLC"
	def __init__(self, id, name, course):
		self.id = id
		self.name = name
		self.course = course
	
	def display(self,):
		print(f"self.this is {self.id}")
		print(f"self.this is {self.name}")
		print(f"self.this is {self.course}")
		

s1 = Student("1234", "Robert", "PFSD")

print(s1)
s1.display()
print(Student.clg)