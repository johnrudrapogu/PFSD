class Product:
	def __init__(self, quantity, key, price):
		self.quantity = quantity
		self.key = key
		self.price = price

	def display():
		print(f"self.this is {self.quantity}")
		print(f"self.this is {self.key}")
		print(f"self.this is {self.price}")

p1 = Product("4", "88999", "599")

print(p1)
p1.display()


