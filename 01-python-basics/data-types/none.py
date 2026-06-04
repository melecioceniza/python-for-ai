# None
my_var = None
print(my_var)  # Output: None
# None is often used to represent the absence of a value or a null value. It is commonly used in situations where you want to indicate that a variable has no value or that a function does not return anything.
# You can also check if a variable is None using the is keyword.
if my_var is None:
    print("my_var is None")
# None is a singleton in Python, which means there is only one instance of None in the entire program. This is why you can use the is keyword to check for None, as it checks for identity rather than equality.
another_var = None
print(my_var is another_var)  # Output: True
