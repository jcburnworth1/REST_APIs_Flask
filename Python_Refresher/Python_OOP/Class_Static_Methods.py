##### Basics of class & static methods #####
## ClassTest
class ClassTest:
    ## Most of the time, will use instance and class methods, static methods are more rare
    def instance_method(self): ## Used for most items
        ## Produce an action that uses or modifies the instance data
        print(f"Called instance_method of class, {self}")

    @classmethod ## Denotes a class method where you no longer need an instance of the class to run
    def class_method(cls):
        ## Often used as factories - See example below
        print(f"Called class_method of {cls}")

    @staticmethod
    def static_method(): ## Don't get any parameters when called
        ## Place a method inside a class
        print(f"Called static_method.")

## Instance Method
test = ClassTest()
test.instance_method() ## Requires an instance to run this method

## Class Method
ClassTest.class_method() ## No instance required to run

## Static Method
ClassTest.static_method() ## No instance required to run

##### Class Method Factory Example #####
class Book:
    TYPES = ("hardcover", 'paperback') ## Used to

    def __init__(self, name: str, book_type: str, weight: float):
        self.name = name
        self.book_type = book_type
        self.weight = weight

    def __repr__(self):
        return f"<Book {self.name}, {self.book_type}, weighing {self.weight}g>"

    @classmethod
    def hardcover(cls, name, page_weight): ## Hardcover book factory
        return Book(name, cls.TYPES[0], page_weight + 100)

    @classmethod
    def paperback(cls, name, page_weight): ## Hardcover book factory
        return Book(name, cls.TYPES[1], page_weight)

## Manually create hardcover book
book = Book("Harry Potter", "hardcover", 1500)
print(book.name)
print(book)

## Use class method Book.hardcover()
book1 = Book.hardcover('Harry Potter 2', 1500)
print(book1)

## Use class method Book.paperback()
book2 = Book.hardcover('Harry Potter 3', 1500)
print(book2)