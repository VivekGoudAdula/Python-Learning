# SCOPE
# A variable is only available from inside the region it is created. This is called scope.

# ------------------------------------------

# LOCAL SCOPE
# A variable created inside a function belongs to the local scope of that function, and can only be used inside that function.
def func():
    x=4
    print(x)
# print(x) # GIVES AN ERROR
func()


# Function inside the function
# The variable x is not available outside the function, but it is available for any function inside the function
def funct():
    x=500
    def fun():
        print(x)
    fun()
funct()

# ------------------------------------------

# GLOBAL SCOPE
# A variable created in the main body of the Python code is a global variable and belongs to the global scope.
# Global variables are available from within any scope, global and local.
a = 100
def num():
    print(a)
num()
print(a)

# NAMING VARIABLES
a = 100
def num():
    a=10
    print(a)
num()
print(a)


# GLOBAL KEYWORD
def nums():
    global y
    y=9
nums()
print(y)

# LEGB RULE
# Python follows the LEGB rule when looking up variable names, and searches for them in this order:
        # Local - Inside the current function
        # Enclosing - Inside enclosing functions (from inner to outer)
        # Global - At the top level of the module
        # Built-in - In Python's built-in namespace
x = "global"

def outer():
  x = "enclosing"
  def inner():
    x = "local"
    print("Inner:", x)
  inner()
  print("Outer:", x)

outer()
print("Global:", x)