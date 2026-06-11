# Python Inner Classes
# an inner class is a class defined inside another class. The inner class can access the properties and methods of the other class.
# Inner classes are useful for grouping classes that are only used in one place, making your code more organized.


# Example
# Create an inner class
class Outer:
    def __init__(self):
        self.name = "Outer Class"

    class Inner:
        def __init__(self):
            self.name = "Inner Class"

    def display(self):
        print("This is the inner class")


outer = Outer()
print(outer.name)

# Access Inner Class from the outside
# To access the inner class, create an object of the outer class, and then create an object of the inner class


class Outer_Access_Inner:
    def __init__(self):
        self.name = "Outer"

    class Inner_Access:
        def __init__(self):
            self.name = "Inner"

        def display_from_inner(self):
            print("Hello I am coming from inner class")


# create object of the outer class
outer = Outer_Access_Inner()
inner = outer.Inner_Access()
inner.display_from_inner()

# Accessing Outer class from Inner Class
# Inner classes in Python do not automatically have access to the outer class instance
# if you want the inner class to access the outer class, you need to pass the outer class instance as a parameter.


# Example
# Pass the outer class instance to the inner class.
class Outer_Access_Outer:
    def __init__(self):
        self.name = "Outer Class"

    class Inner_Class:
        def __init__(self, outer):
            self.outer = outer

        def display(self):
            print(f"Oouter class name : {self.outer.name}")


outer1 = Outer_Access_Outer()
inner1 = outer1.Inner_Class(outer1)
inner1.display()
