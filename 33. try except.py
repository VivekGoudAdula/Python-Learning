# TRY EXCEPT
# The try block lets you test a block of code for errors.
# The except block lets you handle the error.
# The else block lets you execute code when there is no error.
# The finally block lets you execute code, regardless of the result of the try- and except blocks.

# ---------------------------------------------------------

# TRY AND EXCEPT BLOCK

# When an error / exception occurs python normally stops and generate an error message
# So these exceptions can be handled using try and except block


try:
    add = a+b
except:
    print("a and b are not defined")

# We can define as many as except blocks as we want, for specific exceptions

try:
    print(9/0)
except ValueError:
    print("Value Error occurred")
except ZeroDivisionError:
    print("You cannot divide a number by zero") # THIS WILL BE THE OUTPUT 
except NameError:
    print("Variable is not defined")

# ---------------------------------------------------------

# ELSE BLOCK
# We can use else block to execute a block of code is no exception raised

try:
    print("Hello World")
except ValueError:
    print("Something went wrong")
else:
    print("Nothing went wrong") # THIS WILL BE THE OUTPUT

# ---------------------------------------------------------

# FINALLY BLOCK
# It will be excecuted no matter if an exception is raised or not
try:
    print(10/0)
except ZeroDivisionError:
    print("You cannot divide a number by zero")
finally:
    print("The try except block is finished") # THIS WILL BE THE OUTPUT

try:
    print("Hello") 
except:
    print("Unknown Error")
else:
    print("No Error occurred") # THIS WILL BE THE OUTPUT
finally:
    print("The try except block is finished") # THIS WILL BE THE OUTPUT

# ---------------------------------------------------------

# RAISE AN EXCEPTION
# We can choose to raise an exception manually
x = 0
if x<=0:
    raise Exception ("Number must be greater than 0")

# We can even define what kind of exception to raise
y = "Hello"
if type(y) is str:
    raise TypeError("Only integers are allowed")

# ---------------------------------------------------------