# Code Challenge : Polymorphism
# Instruction
# Create a class Cat with a method sound that prints "Meow"
# Create a class Fox with a method sound that prints "Wa-pa-pa"
# Create object c1 = Cat() and f1 = Fox()
# Call sound() on both objects


# Start here
class Animal:
    def __init__(self):
        pass


# Create the Cat class
class Cat(Animal):
    def sound(self):
        print("Meow")


# Create the Fox class
class Fox(Animal):
    def sound(self):
        print("Wa-pa-pa")


# Create objects
c1 = Cat()
f1 = Fox()

# Call the method
# print(c1.sound())
# print(f1.sound())

# Using for loop
for x in (c1, f1):
    x.sound()
