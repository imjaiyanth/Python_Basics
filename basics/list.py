# Creating a list
fruits = ["apple", "banana", "cherry", "date"]

# Accessing elements in a list
print("Fruits:", fruits)
print("First fruit:", fruits[0])
print("Second fruit:", fruits[1])

# Modifying elements in a list
fruits[1] = "orange"
print("Updated list:", fruits)

# Adding elements to a list
fruits.append("grape")
print("List after adding 'grape':", fruits)

# Removing elements from a list
removed_fruit = fruits.pop(0)
print("List after removing", removed_fruit + ":", fruits)

# Iterating through a list
print("Iterating through the list:")
for fruit in fruits:
    print(fruit)

# Checking if an element is in the list
if "apple" in fruits:
    print("Yes, 'apple' is in the list.")
else:
    print("No, 'apple' is not in the list.")

# Getting the length of a list
print("Number of fruits in the list:", len(fruits))
