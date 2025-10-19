# INHERITANCE
# Inheritance allows us to define a class that acquires properties and methods of another class

# PARENT CLASS
class parent:
    def __init__(self,fName, lName):
        self.fName = fName
        self.lName = lName
    def printName(self):
        print(f"Your Name is: {self.fName} {self.lName}")
# OBJECT
p1 = parent("Vivek","Goud")
p1.printName()

# CHILD CLASS 
class child(parent):
    pass

c1 = child("Vibha","Goud")
c1.printName()


# ---------------------------------------------------------

# USING __init__() function in CHILD CLASS
# When you add the __init__() function, the child class will no longer inherit the parent's __init__() function.
# Note: The child's __init__() function overrides the inheritance of the parent's __init__() function.

class kid(parent):
    def __init__( child, fname,lname):
        parent.__init__(child,fname,lname)
k1 = kid("Akira","Goud")
k1.printName()

# super() function
class daughter(parent):
    def __init(girl,fname,lname):
        super().__init__(girl,fname,lname) # Using super() function need not mention parent class name it will automatically inherit properties and methods of parent class
d1 = daughter("Amala","Goud")
d1.printName()


# ---------------------------------------------------------

# ADD PROPERTIES

class son(parent):
    def __init__(self,fname,lname,age):
        super().__init__(fname,lname)
        self.age = age
s1 = son("Arjun","Goud",19)
print(s1.age)

# ---------------------------------------------------------

# ADD METHODS

class grandson(parent):
    def __init__(self,fname,lname,age):
        super().__init__(fname,lname)
        self.age = age
    def birthday(self):
        print(f"Happy {self.age}th Birthday {self.fName}")
g1 = grandson("Aarav","Goud",5)
g1.birthday()