# POLYMORPHISM
# Polymorphism = Many Forms
# Methods, functions, Operators with same name can be executed with different classes and objects

# -------------------------------------------------------------

# FUNCTION POLYMORPHISM
# len() function can be used on different objects
name = "Alice"
print(len(name)) # STRING
names = ["Wednesday","Steeve",]
print(len(names)) # LIST

# -------------------------------------------------------------

# CLASS POLYMORPHISM
# Multiple classes with same method name
# For Example, car and bike both have a method drive()

class car:
	def __init__(self,name,brand):
		self.name = name
		self.brand = brand
	def drive(self):
		print("Car Started")
class bike:
	def __init__(self,name,brand):
		self.name = name
		self.brand = brand
	def drive(self):
		print("Bike Started")
car1 = car("Mustang","Ford")
bike1 = bike("Ninja","Kawasaki")
for i in (car1,bike1):
	i.drive()
	
# -------------------------------------------------------------

# INHERITANCE CLASS POLYMORPHISM
# Classes with child classes with same name also have polymorphism

class person:
	def __init__(self,name,age):
		self.name = name
		self.age = age
	def eat(self):
		print(f"{self.name} is Eating")
class mom(person):
	pass
class dad(person):
	pass
m = mom("Amala",25)
d = dad("Raju",35)
for i in (m,d):
	print(i.name)
	print(i.age)
	i.eat()

# -------------------------------------------------------------