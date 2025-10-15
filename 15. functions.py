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