# Sets in Python
# A set is an unordered collection of unique items. It is mutable, which means you can add or remove items from a set after it has been created. Sets are defined using curly braces {} or the
#set() function. Here are some examples of sets in Python:
# Creating a set with curly braces
my_set = {1, 2, 3, "Hello", True}
print(my_set)  # Output: {1, 2, 3, 'Hello', True}
# Creating a set with the set() function
my_set2 = set([4, 5, 6, "World", False])
print(my_set2)  # Output: {4, 5, 6, 'World', False}
# You can also create a set from a string, which will create a set of unique characters in the string.
my_string_set = set("Hello")
print(my_string_set)  # Output: {'H', 'e', 'l', 'o'}
# Since sets are unordered, you cannot access items in a set using an index. However, you can check if an item is in a set using the in keyword.
print(2 in my_set)  # Output: True
print("World" in my_set)  # Output: False
# You can add items to a set using the add() method and remove items using the remove() method. Here are some examples:
# Adding an item to a set
my_set.add(4)
print(my_set)  # Output: {1, 2, 3, 4, 'Hello', True}
# Removing an item from a set
my_set.remove("Hello")
print(my_set)  # Output: {1, 2, 3, 4, True}
# You can also perform set operations like union, intersection, and difference using the |, &, and - operators respectively. Here are some examples:
# Union of two sets
union_set = my_set | my_set2
print(union_set)  # Output: {1, 2, 3, 4, 5, 6, 'Hello', 'World', True, False}
# Intersection of two sets
intersection_set = my_set & my_set2
print(intersection_set)  # Output: {4}
# Difference of two sets
difference_set = my_set - my_set2
print(difference_set)  # Output: {1, 2, 3, True}
# You can also use the built-in functions len() to get the number of items in a set and clear() to remove all items from a set. Here are some examples:
# Getting the number of items in a set
print(len(my_set))  # Output: 5
# Clearing all items from a set
my_set.clear()
print(my_set)  # Output: set()

# Sets are a powerful data type in Python that can be used for various applications, such as removing duplicates from a list, performing mathematical set operations, and more.
# Note: Since sets are unordered, the output of the set may not be in the same order as the items were added.
# Also, since sets only contain unique items, if you try to add a duplicate item to a set, it will not be added again.
my_set.add(1)
my_set.add(1)
print(my_set)  # Output: {1}

#fronzen set is an immutable version of a set. It is defined using the frozenset() function. Once a frozenset is created, you cannot add or remove items from it. Here are some examples of frozensets in Python:
# Creating a frozenset
my_frozenset = frozenset([1, 2, 3, 4, 5])
print(my_frozenset)  # Output: frozenset({1, 2, 3, 4, 5})

# You can perform set operations on frozensets just like regular sets. Here are some examples:
# Union of two frozensets
frozenset2 = frozenset([4, 5, 6])   
union_frozenset = my_frozenset | frozenset2
print(union_frozenset)  # Output: frozenset({1, 2, 3, 4, 5, 6})

# Intersection of two frozensets
intersection_frozenset = my_frozenset & frozenset2
print(intersection_frozenset)  # Output: frozenset({4, 5})

# Difference of two frozensets
difference_frozenset = my_frozenset - frozenset2
print(difference_frozenset)  # Output: frozenset({1, 2, 3})

