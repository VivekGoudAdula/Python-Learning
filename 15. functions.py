# FUNCTIONS
# A function is a block of code it runs only when it is called
# A function returns data as a result
# A function helps avoiding repetetion of code

# FUNCTION TO PRINT HELLO WORLD
def hello_world():
    print("Hello World")

# CALLING A FUNCTION
hello_world()

# RETURNING A VALUE
def hello():
    return "Vivek Goud Adula"
message = hello()
print(message)


# -------------------------------

# ARGUMENTS
def name(f_name):
    print("Hello" + " " + f_name)
name("Vivekkkk")


# PARAMETERS vs ARGUMENTS

# def name(f_name):                          # --> PARAMETER
#     print("Hello" + " " + f_name)
# name("Vivekkkk")                           # --> ARGUMENT

# DEFAULT PARAMETERS

def func(age=19):
    print(age)
func(18)
func() # DEFAULT WE WILL GET 19 IF NO ARGUMENT IS GIVEN

# KEYWORD ARGUMENTS

def names(fname,lname):
    print(fname,lname)
names(fname="Vivek", lname="Goud")

# POSITIONAL ARGUMENTS

def details(num,aadhar):
    return num,aadhar
det1 = details(9999999999,6969696969696969)
det2 = details(8888888888,9090909090909090)
print(det1, det2)


# MIXING POSITIONAL AND KEYWORD ARGUMENTS

def animal(breed,name,age):
    print("I have a",age,"year old",breed,"his name is",name)
animal("Shihtzu","Max",age=9)


# POSITIONAL ONLY ARGUMENTS
def man(a,/):
    print(a)
man("ram")
# man(a="ram") # WILL GIVE AN ERROR


# KEYWORD ONLY ARGUMENTS
def woman(*,b):
    print(b)
woman(b="rani")
# woman("rani") # WILL GIVE AN ERROR


# COMBINING POSITTION-ONLY AND KEYWORD-ONLY ARGUMENTS
def func(w,x,/,*,y,z):
    return w+x+y+z
result = func(1,2,y=3,z=4)
print(result)


# -------------------------------

# *args, **kwargs

# ARBITRARY ARGUMENTS - *args
# The *args parameter allows a function to accept any number of positional arguments.
# Inside the function, args becomes a tuple containing all the passed arguments

def fruits(*args):
    print("Type:",type(args))
    print("All Arguments:",args)
    print("First fruit:",args[0])
    print("Second fruit:",args[1])
fruits("Apple","Mango","Grapes")


# ARBITRARY KEYWORD ARGUMENTS - **kwargs
# The **kwargs parameter allows a function to accept any number of keyword arguments.
# Inside the function, kwargs becomes a dictionary containing all the keyword arguments:

def details(**info):
    print("Type:",type(info))
    print("All Arguments:",info)
    print("First Name:",info["fName"])
    print("Last Name:",info["lName"])
details(lName="Goud",fName="Vivek", city="Hyderabad")

# -------------------------------

# COMBINING *args and **kwargs
# ORDER MUST BE
        # regular parameters
        # *args
        # **kwargs
def info(header,*args,**kwargs):
    print(header)
    print(args)
    print(kwargs)
info("MY INFORMATION","AIML", "III-A", age = "19", Area = "Sainikpuri")


# -------------------------------

# UNPACKING LISTS WITH *
def addition(a,b,c):
    return a+b+c
nums=[2,3,4]
result=addition(*nums)
print(result)

# UNPACKING DICTIONARIES WITH **
def person(fname,lname):
    print("Helloo",fname,lname)
information = {"lname":"Goud","fname":"Vivek"}
person(**information)