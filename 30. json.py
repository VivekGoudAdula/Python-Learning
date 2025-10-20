# JSON
# JavaScript Object Notation
# JSON, is used to store and exchange data, it is text written with Javascript object notation 

# ---------------------------------------------------------

# IMPORTING JSON MODULE
# Python has a built-in package called JSON by using which we can work with JSON data
import json

# PARSING JSON
# Parsing JSON means converting JSON data into a Python object

# json.loads() FUNCTION

x = '{"name":"Vivek","age":21,"city":"Hyderabad"}' # JSON data
y = json.loads(x) # PARSE JSON data into a Python dictionary
print(y["city"]) # Accessing the value of the "city" key
print(type(y)) # Checking the type of the parsed data # OUTPUT: <class 'dict'>

# ---------------------------------------------------------

# CONVERTING PYTHON OBJECTS INTO JSON

# json.dumps() FUNCTION

cat = {
	"name": "Kitty",
	"age":5,
	"breed":"Persian cat"
}
c = json.dumps(cat)
print(c)

# ----------------------------------------------------------

# Convert a Python object containing all the legal data types

data = {
    "name":"Ahmed",
    "age": 19,
    "single":True,
    "married":False,
    "education":None,
    "parents":("Ali","Aisha"),
    "siblings":["Omar","Fatima"],
    "address":{
        "street":"123 Main St",
        "city":"Cairo",
        "country":"Egypt"
    },
    "skills":[{
        "python": "advanced"
    },
    {
        "C": "beginner"
    }
    ]
}
info = json.dumps(data)
print(info)

# ----------------------------------------------------------

# FORMATTING THE JSON OUTPUT

# indent PARAMETER 
g = json.dumps(data, indent = 4)
print(g)

# separators PARAMETER
h = json.dumps(data, indent = 4, separators=(". ", " = "))
print(h)

# sort_keys PARAMETER
i = json.dumps(data, indent = 4, sort_keys = True)
print(i)

# ----------------------------------------------------------