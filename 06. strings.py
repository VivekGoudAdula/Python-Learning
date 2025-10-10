# STRINGS
# Strings are sequences of characters, enclosed in single or double quotes.

# Creating strings
firstName = "Vivek" # Double quotes
LastName = 'Goud' # Single quotes

# Multiline strings
address = """
Hyderabad,
Telangana,
India
"""

# Accessing characters in a string
print(firstName[1])

# Length of a string
print(len(address))

# Checking substring
print("Hyderabad" in address) # Checks if hydebaad is in address and returns True
print("India" not in address) # Checks if India is not in address and returns False

# --------------------------------

# SLICING
# Slicing allows you to extract a part of a string

sentence = "I am learning Python programming"
print(sentence[0:20]) # From index 0 to 19

print(sentence[:20]) # From start to index 19
print(sentence[5:]) # From index 5 to end

print(sentence[-11:-1]) # From index -11 to -2

# --------------------------------

# MODIFYING STRINGS

firstName.upper() # Converts to uppercase
firstName.lower() # Converts to lowercase
address.strip() # Removes whitespace from start and end
LastName.replace("u", "o") # Replaces 'u' with 'o'
address.split(",") # Splits string into a list at each comma

# --------------------------------

# CONCATENATION
fullName = firstName + " " + LastName

# --------------------------------

# FORMATTING
age = 19
print(f"My name is {fullName} and I am {age} years old.") # f-string formatting

# MODIFIERS
price = 49.95467
print(f"Price is {price:.2f}") # Limits to 2 decimal places

# ---------------------------------