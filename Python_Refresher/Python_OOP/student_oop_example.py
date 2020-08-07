##### Basic OOP Example #####
## Setup Student Class ##
class Student:
    def __init__(self, name: str, year: int, grades: list): ## This is a method
        self.name = name
        self.year = year
        self.grades = grades
        self.student_average = sum(self.grades) / len(self.grades)

    # def student_average(self): ## Utilize this method to calculate average
    #     return sum(self.grades) / len(self.grades)


## Create an instance of the class Student
student = Student('J.C.', 7, [70,75,80,89,95])

#### __str__ & __repr__ #####
## Person Class
class Person:

    def __init__(self, name, age):
        """
        Initialize Peron with the following parameters
        :param name: Name of the individual
        :param age: Age of the individual
        """
        self.name = name
        self.age = age

    def __str__(self): ## This will print to console when print(Person) called for readability
        """
        String representation of a Person object
        :return: Person <name>, <age> years old.
        """
        return f"Person {self.name}, {self.age} years old."

    def __repr__(self):
        """
        :return: <Person <name>, <age> years old.>
        """
        return f"<Person {self.name}, {self.age} years old.>"

## Bob Object
bob = Person('Bob', 35)

print(bob) ## Prints the default <__main__.Person object at 0x10dc8d850>