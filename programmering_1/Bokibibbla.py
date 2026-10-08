
class Book:
    def __init__(self, title, pages, author):
        self.title = title
        self.pages = pages
        self.author = author

    def show_info(self):
        print("Title:", self.title)
        print("Author", self.author)
        print("Pages", self.pages)

bok1 = Book("hobbit", "J.R.R. Tolkien", 310)
bok2 = Book("Harry Potter", "J.K. Rowling", 400)

bok2.show_info()

