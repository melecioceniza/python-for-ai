#booleans
# Booleans represent truth values: True and False
# They are often used in conditional statements and logical operations. 
# Here are some examples of boolean values in Python:
is_python_fun = True
is_sky_green = False

print(f"Is Python fun? {is_python_fun}")
print(f"Is the sky green? {is_sky_green}")

# You can also use boolean values in conditional statements:
if is_python_fun:
    print("Python is indeed fun!")
if not is_sky_green:
    print("The sky is not green, it's usually blue!")

# Booleans can also be the result of comparisons:
a = 10
b = 20
print(f"Is a less than b? {a < b}")
print(f"Is a greater than b? {a > b}")
