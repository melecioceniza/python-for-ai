# Conditional statements in Python allow you to execute certain blocks of code based on specific conditions. The most common conditional statement is the "if" statement, which evaluates a condition and executes a block of code if the condition is true. Here's an example of how to use an "if" statement in Python:
age = 18
if age >= 18:
    print("You are an adult.")
# In this example, the program checks if the age is greater than or equal to 18. If the condition is true, it prints "You are an adult." If the condition is false, it does nothing. You can also add an "else" statement to execute a block of code when the condition is false. Here's an example:
age = 16
if age >= 18:
    print("You are an adult.")
else:
    print("You are not an adult.")
# In this example, if the age is less than 18, it will print "You are not an adult." You can also use "elif" (short for "else if") to check multiple conditions. Here's an example:
age = 65    
if age < 18:
    print("You are a minor.")
elif age >= 18 and age < 65:
    print("You are an adult.")
else:
    print("You are a senior citizen.")
# In this example, the program checks if the age is less than 18, between 18 and 65, or greater than or equal to 65, and prints the appropriate message based on the condition that is true. Conditional statements are essential for controlling the flow of your program and making decisions based on certain conditions. By using "if", "elif", and "else" statements effectively, you can create more complex and dynamic programs in Python.
# Note: When using conditional statements, always consider the data types of the values being compared and ensure that you are comparing values of the same type or converting them to a common type before comparison to avoid errors. Additionally, be mindful of operator precedence when combining multiple conditions in an "if" statement, and consider using parentheses to ensure that your expressions are evaluated in the intended order. Always test your code to ensure that it behaves as expected when using conditional statements.
# In conclusion, conditional statements in Python are a powerful tool for controlling the flow of your program and making decisions based on certain conditions. By using "if", "elif", and "else" statements effectively, you can create more complex and dynamic programs in Python. Always consider the data types of the values being compared and be mindful of operator precedence when using conditional statements to ensure that your code behaves as expected.

# Selection constructs
# Python provides the following three keywords to implement conditional branching:
# - if
# - elif
# - else

x = -6
if x > 0:
    print("positive number")
elif x == 0:
    print("zero")
else:
    print("negative number")
