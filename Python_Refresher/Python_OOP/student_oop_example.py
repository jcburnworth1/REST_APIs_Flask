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
