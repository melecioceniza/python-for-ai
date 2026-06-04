#dictionary is a collection of key-value pairs. It is unordered, mutable, and indexed.
#Dictionaries are defined using curly braces {} and key-value pairs are separated by a colon :. Here are some examples of dictionaries in Python:
# Creating a dictionary with string keys and integer values

my_dict = {"name": "Alice", "age": 30, "city": "New York"}
print(my_dict)  # Output: {'name': 'Alice', 'age': 30, 'city': 'New York'}
# Creating a dictionary with integer keys and string values
my_dict2 = {1: "one", 2: "two", 3: "three"}
print(my_dict2)  # Output: {1: 'one', 2: 'two', 3: 'three'}
# Creating a dictionary with mixed keys and values
my_dict3 = {"name": "Bob", 1: [1, 2, 3], "is_student": True}
print(my_dict3)  # Output: {'name': 'Bob', 1: [1, 2, 3], 'is_student': True}
#You can access values in a dictionary using their keys. Here are some examples:
print(my_dict["name"])  # Output: Alice
print(my_dict2[2])  # Output: two
print(my_dict3[1])  # Output: [1, 2, 3]
#You can also add new key-value pairs to a dictionary or modify existing ones. Here are some examples:

# Adding a new key-value pair
my_dict["country"] = "USA"
print(my_dict)  # Output: {'name': 'Alice', 'age': 30, 'city': 'New York', 'country': 'USA'}
# Modifying an existing key-value pair
my_dict["age"] = 31
print(my_dict)  # Output: {'name': 'Alice', 'age': 31, 'city': 'New York', 'country': 'USA'}
#You can also remove key-value pairs from a dictionary using the del keyword or the pop() method. Here are some examples:
# Removing a key-value pair using del
del my_dict["city"]
print(my_dict)  # Output: {'name': 'Alice', 'age': 31, 'country': 'USA'}
# Removing a key-value pair using pop()
age = my_dict.pop("age")
print(age)  # Output: 31
print(my_dict)  # Output: {'name': 'Alice', 'country': 'USA'}

