# Sequence Operations in Python
# Sequence operations are a fundamental part of Python programming and are used to manipulate and work with sequences such as lists, tuples, strings, and more. These operations allow you to perform various tasks such as indexing, slicing, concatenation, repetition, and more. In this section, we will explore some of the common sequence operations in Python and how to use them effectively in your code.

# 1. Indexing: You can access individual elements of a sequence using indexing. The index starts at 0 for the first element, 1 for the second element, and so on. You can also use negative indexing to access elements from the end of the sequence.
my_list = [1, 2, 3, "Hello", True]
print(my_list[0])  # Output: 1
print(my_list[-1])  # Output: True

# 2. Slicing: You can extract a portion of a sequence using slicing. The syntax for slicing is [start:stop:step], where start is the index to start from, stop is the index to end at (exclusive), and step is the interval between indices.
my_string = "Hello, World!"
print(my_string[0:5])  # Output: Hello
print(my_string[7:12])  # Output: World 
print(my_string[::2])  # Output: Hlo ol!

# 3. Concatenation: You can combine two or more sequences using the concatenation operator (+). This creates a new sequence that contains the elements of the original sequences.
list1 = [1, 2, 3]
list2 = [4, 5, 6]
combined_list = list1 + list2
print(combined_list)  # Output: [1, 2, 3, 4, 5, 6]
string1 = "Hello"
string2 = "World"
combined_string = string1 + " " + string2
print(combined_string)  # Output: Hello World

# 4. Repetition: You can repeat a sequence a specified number of times using the repetition operator (*). This creates a new sequence that contains the original sequence repeated the specified number of times.
my_list = [1, 2, 3]
repeated_list = my_list * 3
print(repeated_list)  # Output: [1, 2, 3, 1, 2, 3, 1, 2, 3]
my_string = "Hello"
repeated_string = my_string * 3
print(repeated_string)  # Output: HelloHelloHello

# Sequence operations are essential for working with data in Python and are widely used in various programming scenarios. By understanding how to use these operations effectively, you can manipulate and work with sequences in a powerful and efficient way in your Python code. Always consider the context of your code and the specific use case when using sequence operations to ensure that you are using them correctly and effectively.  
# Note: When using sequence operations, be mindful of the data types of the sequences you are working with and ensure that you are using the appropriate operations for those data types to avoid errors. Additionally, be aware of the behavior of sequence operations with different data types, such as how concatenation works with strings versus lists, and how repetition behaves with different types of sequences. Always test your code to ensure that it behaves as expected when using sequence operations. 
