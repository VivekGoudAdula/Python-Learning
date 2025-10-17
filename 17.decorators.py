# DECORATORS
# Decorators are used to add extra behaviour to a function, without changing function code
# It takes a function as an input and returns new function

# BASIC DECORATOR
def name(func):
    def inner():
        return func().upper()
    return inner
@name
def fname():
    return "Hello WOrld"
print(fname())

# -----------------------------------------

# MULTIPLE DECORATOR CALLS
# def changecase(fun):
#     def upp():
#         return fun().upper()
#     return upp()
# @changecase
# def my_func():
#     return "Vivek goud"
# print(my_func())

# @changecase
# def fun():
#     return "Adula"
# print(fun())

# -----------------------------------------

# ARGUMENTS IN THE DECORATED FUNCTION
# def case(func):
#     def new(x):
#         return func(x).upper()
#     return new
# @case
# def myfunction(name):
#     return "Hello" + name
# print(myfunction(" Viv"))

# *args AND **kwargs
# def changecase(fun):
#     def inner_fun(*args,**kwargs):
#         return fun(*args,**kwargs).upper()
#     return inner_fun
# @changecase
# def new(age):
#     return "You are " + age + " old"
# print(new("nineteen"))

# -----------------------------------------

# DECORATORS WITH ARGUMENTS
# Decorators can accept their own arguments by adding another wrapper level.

def changecase(n):
    def inner(func):
        def new():
            if n==1:
                a=func().lower()
            else:
                a=func().upper()
            return a
        return new
    return inner
@changecase(0)
def info():
    return "Hello Max"
print(info()) 


# -----------------------------------------

# MULTIPLE ARGUMENTS
def cooking(func):
    def curry():
        return func()+"\nFood Prepared!"
    return curry
def cook(func):
    def rice():
        return func() + "\nDish ready"
    return rice
@cooking
@cook
def food():
    return "Curry prepared successfully"
print(food())


# -----------------------------------------

# PRESERVING FUNCTION METADATA
def hello():
    return "Hello"
print(hello.__name__)