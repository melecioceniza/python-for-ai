# Code Challenge : Inheritance
# Test your understanding of python inheritance by completing coding challenge
# Instructions
# Create a parent class Animal with an __init__() that takes name
# Add a method speak that prints the name
# Create a child class Dog that inherits from Animal
# Create an object d1 = Dog("Rex")
# Call d1.speak()


# Create the Animal class
class Animal:
    def __init__(self, name):  # Add __init__() with name parameter
        self.name = name

    def speak(self):  # Add method speak that print name
        print(self.name)


# Create the Dog class (inherits from Animal)
class Dog(Animal):  # Dog class that inheriting from Animal class
    def __init__(self, name):
        super().__init__(name)
        # self.name = name


# Create an object
d1 = Dog("Rex")  # instantiate an object name "Rex"

# Call the speak method
d1.speak()  # Call and display or print the method speak
