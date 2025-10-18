# GENERATORS
# Generators are the functions which can resume and pause thier execution
# When a generator function is called, it returns a generator object which is an iterator
# The code inside the function will only be compiled, it wont be executed, it will be executed only when it we iterate over the generator

# YIELD KEYWORD
# The yield keyword is what makes a function a generator.
# Instead of using return we use yield in generator.


def generators():
    yield 1
    yield 2
    yield 3
for generator in generators():
    print(generator)


# next() function 
# We can manually iterate through the generator using next() function
def greet():
    yield "Hello"
    yield "Good Morning"
    yield "Good Afternoon"
greeting = greet()
print(next(greeting))
print(next(greeting))
