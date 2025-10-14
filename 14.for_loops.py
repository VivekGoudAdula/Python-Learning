# FOR LOOPS
# For loop is used to iterate over a sequence


fruits = ["Apple","Banana","Grapes"]
for fruit in fruits:
    print(fruit)

# LOOPING THROUGH A STRING

for x in "Vivek Goud Adula":
    print(x)

# BREAK 
 
for fruit in fruits:
    print(fruit)
    if fruit == "Banana":
        break

# PASS

for i in [1,2,3]:
    pass

# RANGE () FUNCTION

for i in range(len(fruits)):
    print(fruits[i])

# NESTED LOOPS
vegetables = ["Tomato", "Brinjal", "Mirchi"]
groceries = ["Bread", "Cheese", "Butter"]
for vegetable in vegetables:
    for grocery in groceries:
        print(vegetable,grocery)