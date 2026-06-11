# Python Inheritance
# it allows us to define a class that inherits all the methods and properties from another class.
# Parent class is the class being inherited fromm, also called base class.
# Child class is the class that inherits from the parent class or another class. it also called a derive class


# Example
# create a class named Person with firstname and lastname properties and a printname method
class Person:
    def __init__(self, fname, lname):
        self.first_name = fname
        self.last_name = lname

    def print_name(self):
        print(self.first_name, self.last_name)


# Use the Person class to create an object, and then execute the printname method:
x = Person("Mel", "Ceniza")
x.print_name()

# Now create a child class
# To create a class that inherits the functionality from the another class, send the parent class as a parameter when creating the child class


# Example
# Create a class name Student, which will inherit the properties and methods from the Person class
class Student(Person):
    pass


# Note : Use the pass keyword when you do  no want to add any other properties or methods to the class
# Now the student class has the same properties and methods as the Person class.

# Example
# Use the Student class to create an object, and then execute the printname method

x = Student("Jesus", "Christ")
x.print_name()

# Add the __init__() Function
# So far we have created a child class that inherits the properties and the methods from its parent
# Add the __init__() function to the child class (instead of the pass keyword)
# Note : The __init__() function is called automatically every time


# Example
# Add the __init__() function to the Student class:
# When adding the __init__() function, the child class will no longer inherits the parent's __init__() function.
# Note : The child __ini__() function overide the inheritance of the parent's __init__() function
# To keep the inheritance of the parent's __init__() function, add a call to the parent's __init__() function:


class Student(Person):
    def __init__(self, fname, lname):
        # add properties
        Person.__init__(self, fname, lname)


# super() Function
# Python also has a super() function that will make the child class inherit all the methods and properties from its parent:
# Example
class Student(Person):
    def __init__(self, fname, lname):
        super().__init__(fname, lname)


# using the super() function, you do not have to use the name of the parent element, it will automatically inherit the methods and properties from its parent.


# Example
# add a property called graduationyear to the Student class:
class Student(Person):
    def __init__(self, fname, lname, year):
        super().__init__(fname, lname)
        self.graduationyear = year


x = Student("Mel", "Ceniza", 2027)
print(f"{x.first_name} {x.last_name} {x.graduationyear}")


# Add method example
class Student(Person):
    def __init__(self, fname, lname, year):
        super().__init__(fname, lname)
        self.graduationyear = year

    def welcome(self):
        print(
            f"Welcome, {self.first_name} {self.last_name} to the class of {self.graduationyear}"
        )


x = Student("Mel", "Ceniza", 2027)
print(x.welcome())
