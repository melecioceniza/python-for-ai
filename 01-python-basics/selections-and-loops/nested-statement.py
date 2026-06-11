# A nested statement in Python means one statement is placed inside another statement.
# The most common example is a nested if statement:
age = 20
has_id = True

if age >= 18:
    if has_id:
        print("Entry allowed")

# How it works
# Python checks age >= 18.
# If it's True, Python enters the first if block.
# Then it checks has_id.
# If that is also True, it prints:

# Here is another example
age = 16
has_id = True

if age >= 18:
    if has_id:
        print("Entry allowed")
    else:
        print("Bring your ID")
else:
    print("Too young")  # output - Too young


# Nested loops
# You can also nest loops
for i in range(3):
    for j in range(2):
        print(i,j)
# Output
# 0 0
# 0 1
# 1 0
# 1 1
# 2 0
# 2 1     

# Identation is important
# Python uses indentation to define nesting:
if True:
    print("Inside")
    if True:
        print("Nested inside")

# Output
# Inside
# Nested inside