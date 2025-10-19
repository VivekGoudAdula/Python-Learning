# CLASSES AND OBJECTS
# Python is an object oriented programming language

# ---------------------------------------------------------

# CREATING CLASS
# To create a class in python we use class keyword
class car:
    brand = "Tata"

# ---------------------------------------------------------

# CREATING AN OBJECT
# Now we can use car class to create objects

safari = car()
print(safari.brand)

# ---------------------------------------------------------

# __init__() method
# All classes have method called __init__(), which is always executed when the class is initiated
# Use __init__() method to assign values to object properities

class person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
person1 = person("Vivek", 19)
person2 = person("Vibha", 20)
print(person1.name)
print(person2.age)

# ---------------------------------------------------------

# __str__() method
class boy:
    def __init__(self,age):
        self.age = age
    def __str__(self):
        return f"{self.age}"
a1 = boy(19)
print(a1)

# ---------------------------------------------------------

# CREATE OWN METHODS
# You can create your own methods inside objects. Methods in objects are functions that belong to the object.

class locality:
    def __init__(self,place,pincode):
        self.place=place
        self.pincode=pincode
    def func(self):
        print(f"I stay at {self.place}, {self.pincode}")
area = locality("Hyderabad",500062)
area.func()

# ---------------------------------------------------------

# SELF PARAMETER
# The self parameter is a reference to the current instance of the class, and is used to access variables that belong to the class
# It does not have to be named self, you can call it whatever you like, but it has to be the first parameter of any function in the class

class cat:
    def __init__(kitty,breed,age):
        kitty.breed=breed
        kitty.age=age
c1 = cat("Persian Cat",7)
print(c1.breed)
print(f"Initial Age: {c1.age}")

# ---------------------------------------------------------

# MODIFY OBJECT PROPERTIES
c1.age = 6
print(c1.age)
print(f"Modified Age: {c1.age}")

# ---------------------------------------------------------

# DELETE OBJECT PROPERTIES

del c1.age
# print(c1.age) # OUTPUT: AttributeError: 'cat' object has no attribute 'age'

# ---------------------------------------------------------

# DELETE OBJECT 

del c1
# print(c1) # OUTPUT: NameError: name 'c1' is not defined

# ---------------------------------------------------------

# PASS STATEMENT
# Once a class is created, you can use the pass statement to avoid getting an error
class man:
    pass

# ---------------------------------------------------------