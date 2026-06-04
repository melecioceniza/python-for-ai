#Strings are text - any characters inside quotes. Python doesn’t care if you use single or double quotes, just be consistent.
#You can use single quotes for a string that contains double quotes, and vice versa.
#Here are some examples of strings in Python:
# Using double quotes for a string that contains single quotes

string1 = "It's a nice day!"
print(string1)
# Using single quotes for a string that contains double quotes
string2 = 'She said, "Hello!"'
print(string2)
# Using double quotes for a string that contains both single and double quotes
string3 = "She said, \"It's a nice day!\""
print(string3)
#Using triple quotes for a string that spans multiple lines
string4 = """This is a string that spans multiple lines."""
print(string4)
#You can also use triple quotes for a string that contains both single and double quotes without needing to escape them.
string5 = '''She said, "It's a nice day!"'''
print(string5)

#lists are ordered collections of items, which can be of any data type. They are defined using square brackets [] and can contain duplicate items. Lists are mutable, meaning you can change their content after they have been created.
my_list = [1, 2, 3, "Hello", True]
print(my_list)
#You can access individual items in a list using their index, which starts at 0.
print(my_list[0])  # Output: 1
print(my_list[3])  # Output: "Hello"
print(my_list[4])  # Output: True
#You can also modify items in a list by assigning a new value to a specific index.
my_list[1] = "World"
print(my_list)  # Output: [1, "World", 3, "Hello", True]
#Lists also support various methods for adding, removing, and manipulating items. For example:
my_list.append("New Item")  # Adds an item to the end of the list
print(my_list)  # Output: [1, "World", 3, "Hello", True, "New Item"]
my_list.remove(3)  # Removes the first occurrence of the item with value 3
print(my_list)  # Output: [1, "World", "Hello", True, "New Item"]

#tuples are similar to lists, but they are immutable, meaning you cannot change their content after they have been created. They are defined using parentheses () and can contain duplicate items.
my_tuple = (1, 2, 3, "Hello", True)
print(my_tuple)
#You can access individual items in a tuple using their index, which starts at 0.
print(my_tuple[0])  # Output: 1
print(my_tuple[3])  # Output: "Hello"
print(my_tuple[4])  # Output: True
#Since tuples are immutable, you cannot modify their content. However, you can create a new tuple by concatenating existing tuples.
new_tuple = my_tuple + (4, 5)
print(new_tuple)  # Output: (1, 2, 3, "Hello", True, 4, 5)
#You can also use tuple unpacking to assign values from a tuple to individual variables.
a, b, c, d, e = my_tuple
print(a)  # Output: 1
print(b)  # Output: 2
print(c)  # Output: 3
print(d)  # Output: "Hello"
print(e)  # Output: True

#ranges are a sequence of numbers that are generated using the range() function. They are commonly used in loops and for creating sequences of numbers. The range() function can take one, two, or three arguments: start, stop, and step.
#Here are some examples of using the range() function:  
# Using range() with one argument (stop)
for i in range(5):
    print(i)  # Output: 0, 1, 2, 3, 4
# Using range() with two arguments (start, stop)
for i in range(1, 6):
    print(i)  # Output: 1, 2, 3, 4, 5
# Using range() with three arguments (start, stop, step)
for i in range(0, 10, 2):
    print(i)  # Output: 0, 2, 4, 6, 8
#You can also create a list from a range using the list() function.
my_range = range(1, 10, 2)
print(list(my_range))  # Output: [1, 3, 5, 7, 9]

#bytes are a sequence of bytes, which are used to represent binary data. They are defined using the bytes() function or by prefixing a string with b. Bytes are immutable, meaning you cannot change their content after they have been created.
#Here are some examples of bytes in Python:
# Using the bytes() function to create a bytes object
my_bytes = bytes([1, 2, 3, 4, 5])
print(my_bytes)  # Output: b'\x01\x02\x03\x04\x05'
# Using a bytes literal to create a bytes object
my_bytes_literal = b"Hello"
print(my_bytes_literal)  # Output: b'Hello'
#You can access individual bytes in a bytes object using their index, which starts at 0
print(my_bytes[0])  # Output: 1
print(my_bytes_literal[1])  # Output: 101 (ASCII value of 'e')
#Since bytes are immutable, you cannot modify their content. However, you can create a new bytes object by concatenating existing bytes objects.
new_bytes = my_bytes + b'\x06\x07'
print(new_bytes)  # Output: b'\x01\x02\x03\x04\x05\x06\x07'
#You can also convert a bytes object to a string using the decode() method.
my_string = my_bytes_literal.decode("utf-8")
print(my_string)  # Output: "Hello" 

#bytearray is a mutable sequence of bytes, which is used to represent binary data. It is defined using the bytearray() function. Bytearrays can be modified after they have been created, unlike bytes.
#Here are some examples of bytearrays in Python:
# Using the bytearray() function to create a bytearray object
my_bytearray = bytearray([1, 2, 3, 4, 5])
print(my_bytearray)  # Output: bytearray(b'\x01\x02\x03\x04\x05')
# Using a bytearray literal to create a bytearray object
my_bytearray_literal = bytearray(b"Hello")
print(my_bytearray_literal)  # Output: bytearray(b'Hello')
#You can access individual bytes in a bytearray object using their index, which starts at 0.
print(my_bytearray[0])  # Output: 1
print(my_bytearray_literal[1])  # Output: 101 (ASCII value of 'e')
#Since bytearrays are mutable, you can modify their content by assigning a new value to a specific index.
my_bytearray[1] = 10
print(my_bytearray)  # Output: bytearray(b'\x01\n\x03\x04\x05')
#You can also create a new bytearray object by concatenating existing bytearray objects.
new_bytearray = my_bytearray + bytearray(b'\x06\x07')
print(new_bytearray)  # Output: bytearray(b'\x01\n\x03\x04\x05\x06\x07')
#You can also convert a bytearray object to a string using the decode() method.
my_string = my_bytearray_literal.decode("utf-8")
print(my_string)  # Output: "Hello"

#MEMORY VIEW is a sequence of bytes that provides a view of the memory of another object. It is defined using the memoryview() function. Memory views are used to access the memory of an object without copying it, which can be more efficient for large data
#Here are some examples of memory views in Python:
# Using the memoryview() function to create a memory view object
my_bytes = bytes([1, 2, 3, 4, 5])
my_memory_view = memoryview(my_bytes)
print(my_memory_view)  # Output: <memory at 0x7f8b8c8c8c8>
# You can access individual bytes in a memory view object using their index, which starts at
print(my_memory_view[0])  # Output: 1
print(my_memory_view[1])  # Output: 2
# You can also create a new memory view object by slicing an existing memory view object.
new_memory_view = my_memory_view[1:4]
print(new_memory_view)  # Output: <memory at 0x7f8b8c8c8c8>
# You can also convert a memory view object to a bytes object using the tobytes() method.
my_bytes_from_memory_view = my_memory_view.tobytes()
print(my_bytes_from_memory_view)  # Output: b'\x01\x02\x03\x04\x05'
