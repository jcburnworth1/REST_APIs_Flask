##### Class Composition #####
class BookShelf:
    def __init__(self, *books):
        self.books = books

    def __str__(self):
        return f"Bookshelf with {len(self.books)} books."

class Book: ## Doesn't make sense to inherit BookShelf
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f"Book: {self.name}"

## Create two instances of the Book class
book1 = Book("Book1")
book2 = Book("Book2")

## Create a BookShelf class with our two books above
shelf = BookShelf(book1, book2)

print(shelf)