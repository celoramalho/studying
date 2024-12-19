"""
Demonstration of Multiple Inheritance, Good Head Concept, and Method Resolution Order (MRO).
This example shows how Python resolves method calls in a multiple inheritance scenario.

Args:
    employee (obj): An object that implements a specific method.
    name (str): Name of the employee.
    salary (int): Salary value for an employee.

Returns:
    Depends on the method being called (e.g., string, integer, etc.).
"""

# Base class: Employee
class Employee:
    """
    Base class representing a generic employee.
    """
    def __init__(self, name, salary):
        self._name = name
        self._salary = salary
    
    @property
    def name(self):
        return self._name
    
    def role(self):
        # Default behavior for an Employee
        print(f'{self._name} is working...')


# Derived class: Programmer inherits from Employee
class Programmer(Employee):
    """
    Programmer class inherits from Employee.
    """
    def __init__(self, name, salary):
        super().__init__(name, salary)

    def role(self):
        # Overrides the role method from Employee
        print(f'{self._name} is writing code')

    def show_language(self):
        # Method specific to Programmer
        print(f'{self._name} writes code in Python')


# Derived class: Manager inherits from Employee
class Manager(Employee):
    """
    Manager class inherits from Employee and adds managerial behavior.
    """
    def __init__(self, name, salary):
        super().__init__(name, salary)
        self.__team_size = 20  # Private attribute

    def role(self):
        # Overrides the role method from Employee
        print(f'{self._name} manages the department')

    def management_philosophy(self):
        print(f'{self._name} focuses on people, transparency, and honesty')

    @property
    def team_size(self):
        # Encapsulation: Access to private attribute
        return self.__team_size

class TechGuy:
    def __str__(self):
        return f'Tech Guy, {self._name}'

# Multiple Inheritance: TechLead inherits from Programmer and Manager
class TechLead(Programmer, Manager, TechGuy):
    """
    TechLead inherits from Programmer and Manager.
    The 'Good Head' concept ensures that methods in Programmer are prioritized over Manager.
    """

    # This class does not define any new methods, so the behavior depends on the Method Resolution Order (MRO).
    # MRO: TechLead -> Programmer -> Employee -> Manager -> Employee -> object

    pass

# Creating an instance of TechLead
john_doe = TechLead('John Doe', 15000)

# MRO resolves methods based on the order of inheritance: Programmer > Manager.
john_doe.role()  # Output: John Doe is writing code  (Programmer's role method takes precedence)
john_doe.show_language()  # Output: John Doe writes code in Python
john_doe.management_philosophy()  # Output: John Doe focuses on people, transparency, and honesty
print(f'{john_doe.name} manages a team of {john_doe.team_size} people')
print(TechLead.__mro__) # Show the Method Resolution Order

print(john_doe) # Call a TechGuy method
"""
Explanation of Key Concepts (within the code):

1. **Multiple Inheritance**:
   - TechLead inherits from both Programmer and Manager.
   - Python allows this flexibility, but the order of inheritance matters.

2. **Good Head Concept**:
   - The first class listed in the inheritance chain (Programmer) takes priority.
   - If `role()` exists in both Programmer and Manager, the one in Programmer is used.

3. **Method Resolution Order (MRO)**:
   - Python resolves the order of method calls based on the MRO.
   - Use `ClassName.__mro__` to see the order of classes.
     Example:
     ```python
     print(TechLead.__mro__)
     # Output:
     # (<class '__main__.TechLead'>, <class '__main__.Programmer'>, 
     #  <class '__main__.Manager'>, <class '__main__.Employee'>, <class 'object'>)
     ```

4. **Encapsulation**:
   - The `team_size` attribute in Manager is private (`__team_size`) and accessed via a property.

5. **Overriding**:
   - Both Programmer and Manager override the `role()` method from Employee.

6. **Mixing**:
    - A Mixin is a class that provides specific functionality to other classes through inheritance, but it is not meant to stand alone. Mixins are used to "mix in" additional behavior into existing classes without deeply modifying their hierarchy.
    Mixins follow a composition-like design and allow code reusability while maintaining flexibility.
"""

#Herança múltipla
#Resolução da ordem de chamada de métodos
#Mixins