class Employee:
    # name = "Ram"
    language = "python"         # Class Attributes
    salary = 120000


# salary and language are class attributes as they directly belongs to the class


ram = Employee()
print(ram.language , ram.salary)


arnav = Employee()
arnav.name = "Arnav"    # Object Attributes / Instance Attributes
print(arnav.name, arnav.language , arnav.salary)


# Here name is object attributes / instance attributes

