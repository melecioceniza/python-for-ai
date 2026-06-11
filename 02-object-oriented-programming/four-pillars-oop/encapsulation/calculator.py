# Protected Properties
# Python also has a convention for protected properties using a single underscore _ prefix
# Example
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self._salary = salary


employee = Employee("Mel", 100000)
print(employee.name)
print(employee._salary)  # Can access, but shouldn't
# Note : A single underscore _ is just a convention. It tells other programmers that the property is intended for internal use, but Python doesn't enforce this restriction


# Private Methods
# You can also make methods private using the double underscore prefix.
# Example
class Calculator:
    def __init__(self):
        self.result = 0

    def __validate(self, num):
        if not isinstance(num, (int, float)):
            return False
        return True

    def add(self, num):
        if self.__validate(num):
            self.result += num
        else:
            print("Invalide number")


calc = Calculator()
calc.add(10)
calc.add(5)
print(calc.result)
# calc.__validate(5) # This would cause and error

# Note Just like private properties with double underscores, private methods cannot be called directly from outside the class. The __validate method can only be used by other methods inside the class.


# Name Mangling
# Name mangling is how Python implement private properties and methods
# When you double underscores __ Python automatically renames it internally by adding _ClassName in front.
# For example __age becomes _Person__age
# Example
class Person:
    def __init__(self, name, age):
        self.name = name
        self.__age = age

    # add a getter
    def get_age(self):
        return self.__age


person = Person("Mel", 30)

# This is how Python mangles the name:
print(
    person._Person__age
)  # Not recommended! you can get the properties wihtout adding a getter method
print(person.get_age())  # recommended , but you need the add getter method.
