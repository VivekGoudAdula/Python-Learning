# DICTIONARIES
# A dictionary is a collection which is unordered, changeable and indexed. No duplicate members.

phonebook = {
    "Vivek": 9932762098,
    "Bob": 1234567890,
    "Alice": 9876543210
}

print(phonebook) # Print the whole dictionary
print(type(phonebook)) # Type of the variable
print(len(phonebook)) # Length of the dictionary

# ---------------------------------

# ACCESSING ITEMS

print(phonebook["Vivek"]) # Accessing value by key

print(phonebook.get("Alice")) # Accessing value by key using get()

print(phonebook.keys()) # Returns all keys
print(phonebook.values()) # Returns all values
print(phonebook.items()) # Returns all key-value pairs

# ---------------------------------

# MODIFYING ITEMS
phonebook["Vivek"] = 9999999999 # Changing value of existing key

phonebook.update({"Bob": 1111111111}) # Changing value using update()

# ---------------------------------

# ADDING ITEMS
phonebook["Charlie"] = 2222222222 # Adding new key-value pair
phonebook.update({"David": 3333333333}) # Adding new key-value pair using update()

# ---------------------------------

# REMOVING ITEMS
phonebook.pop("Alice") # Removes item with specified key
phonebook.popitem() # Removes last inserted item
del phonebook["Bob"] # Deletes item with specified key
phonebook.clear() # Clears the entire dictionary

# ---------------------------------

# LOOPING THROUGH A DICTIONARY
for i in phonebook:
    print(i) # Prints keys

for i in phonebook.keys():
    print(i) # Prints keys
for i in phonebook.values():
    print(i) # Prints values
for i in phonebook.items(): 
    print(i) # Prints key-value pairs

# ---------------------------------

# COPYING A DICTIONARY
phone = phonebook.copy() # Using copy() method
newPhone = dict(phonebook) # Using dict() function

# ---------------------------------

# NESTED DICTIONARIES
data = {
    "person1": {
        "name": "Vivek",
        "age": 19,
        "city": "Hyderabad"
    },
    "person2": {
        "name": "Alice",
        "age": 20,
        "city": "New York"
    }
}

print(data["person1"]["name"]) # Accessing nested dictionary item