# VARIABLES
# Variables are containers for storing data values.
name = "Vivek Goud Adula"  # String variable stored in ""
place = 'Hyderabad'      # String variable stored in ''
print(name)

age = 19 # Integer variable
print(age)

# --------------------------------

# CASTING
# You can specify the data type of a variable by casting.

a = str(5) # a wil be a string : '5'
b = float(10) # b will be a float : 10.0
c = int(15) # c will be an integer : 15

# --------------------------------

# TYPE FUNCTION
# To get the type of a variable we use type() function
print(type(a)) # Output: <class 'str'>
print(type(b)) # Output: <class 'float'>
print(type(c)) # Output: <class 'int'>

# --------------------------------

# CASE SENSITIVE
# Variable names are case-sensitive.
d = 10
D = "Vivek"
print(d) # Output: 10
print(D) # Output: Vivek
# D and d are different, D will not overwrite d

# --------------------------------

# VARIABLE NAMES
# A variable name must start with a letter or the underscore character
myname = "Vivek"
my_name = "Vivek"
_my_name = "Vivek"
_myname = "Vivek"
myname1 = "Vivek"
MYNAME = "Vivek"

# A variable name cannot start with a number
'''
1myname = "Vivek"
my-name = "Vivek"
my name = "Vivek"
'''
# These will give syntax errors


# ---------------------------------

# MULTIPLE ASSIGNMENTS
# You can assign values to multiple variables in one line
x,y,z = "Apple,""Ball","Cat"

# ONE VALUE TO MULTIPLE VARIABLES
g = h = i = "Dog"
