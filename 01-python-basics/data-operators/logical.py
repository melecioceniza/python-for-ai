#logical operators in Python
# Logical operators are used to combine multiple conditions and return a boolean result (True or False).    
# The three logical operators in Python are:
# and: Returns True if both conditions are true.
# or: Returns True if at least one of the conditions is true.
# not: Returns True if the condition is false, and False if the condition is true.
# Here are some examples of using logical operators in Python:
x = 5
y = 10
print(x < y and y < 20)  # Output: True (both conditions are true)
print(x < y or y > 20)    # Output: True (at least one condition is true)
print(not x < y)          # Output: False (x < y is true, so not x < y is false)

# You can also combine multiple logical operators to create more complex conditions. For example:
a = 15
b = 25
c = 35
print(a < b and b < c)  # Output: True (both conditions are true)
print(a < b or b > c)    # Output: True (at least one condition is true)
print(not a < b)          # Output: False (a < b is true, so not a < b is false)    

# Logical operators are commonly used in conditional statements (like if statements) to control the flow of the program based on certain conditions. Here is an example:
age = 18
if age >= 18 and age <= 65:
    print("You are eligible to work.")
else:
    print("You are not eligible to work.")

# In this example, the program checks if the age is between 18 and 65 (inclusive) and prints a message accordingly. Logical operators are essential for making decisions in your code and are widely used in various programming scenarios.
# Note: When using logical operators, be mindful of operator precedence. The not operator has the highest precedence, followed by and, and then or. You can use parentheses to control the order of evaluation in complex expressions. For example:
x = 5 
y = 10
z = 15
print(x < y and y < z or x > z)  # Output: True (x < y and y < z is true, so the whole expression is true)
print(x < y and (y < z or x > z))  # Output: True (y < z is true, so the expression inside the parentheses is true, and x < y is also true, so the whole expression is true)

# In conclusion, logical operators are a fundamental part of Python programming and are used to combine multiple conditions and return a boolean result. They are essential for controlling the flow of your program and making decisions based on certain conditions. Understanding how to use logical operators effectively is crucial for any Python programmer, as they are fundamental to many programming tasks and applications.
# Note: When using logical operators, always consider the operator precedence and use parentheses to ensure that your expressions are evaluated in the intended order. Additionally, be mindful of the data types of the values being compared, as this can affect the result of the logical operations. Always ensure that you are comparing values of the same type or converting them to a common type before comparison to avoid errors.
# Logical operators are a powerful tool in Python that allow you to combine multiple conditions and make decisions based on those conditions. They are essential for controlling the flow of your program and are widely used in various programming scenarios. By understanding how to use logical operators effectively, you can write more efficient and effective code in Python.
