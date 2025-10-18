# LAMBDA FUNCTIONS
# Lambda function is a small anonymous function
# It can take any number of arguments baut it has only a single expression
# SYNTAX: lambda arguments : expression

x = lambda a : a + 10
print(x(5)) 

# MULTIPLE ARGUMENTS

a = lambda x , y : x + y
print(a(2,7))

# LAMBDA FUNCTION
def func(n):
    return lambda a: a * n
double = func(2)
triple = func(3)
print(double(10))
print(triple(10))

# -----------------------------------------
 
# LAMBDA BUILT-IN FUNCTIONS
# map(), filter(), sorted()


# map()
# The map() function applies a function to every item in an iterable
nums = [5,4,3,2,1]
doubled = list(map(lambda a: a*2,nums))
print(doubled)

# filter()
# The filter() function creates a list of items for which a function returns True
odd_nos = list(filter(lambda a: a%2!=0, nums))
print(odd_nos)

# sorted()
# The sorted() function can use a lambda as a key for custom sorting
students = [ ("Akshay",20),("vivek", 19),("Vishnu",20)]
sorting = sorted(students, key=lambda a: a[1])
print(sorting)