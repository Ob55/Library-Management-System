class Book:
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.checked_out = False

    def __str__(self):
        availability = "Available" if not self.checked_out else "Checked out"
        return f"{self.title} by {self.author} (ISBN: {self.isbn}) - {availability}"


class Patron:
    def __init__(self, name):
        self.name = name
        self.books_checked_out = []

    def checkout_book(self, book):
        if not book.checked_out:
            self.books_checked_out.append(book)
            book.checked_out = True
            return True
        return False

    def return_book(self, book):
        if book in self.books_checked_out:
            self.books_checked_out.remove(book)
            book.checked_out = False
            return True
        return False

    def __str__(self):
        return f"{self.name} - Books Checked Out: {len(self.books_checked_out)}"


class Library:
    def __init__(self):
        self.books = []
        self.patrons = []

    def add_book(self, title, author, isbn):
        book = Book(title, author, isbn)
        self.books.append(book)

    def add_patron(self, name):
        patron = Patron(name)
        self.patrons.append(patron)

    def lend_book(self, patron_name, isbn):
        # Check if the patron is already registered
        patron_exists = False
        for patron in self.patrons:
            if patron.name == patron_name:
                patron_exists = True
                break

        # If the patron is not registered, add them to the system
        if not patron_exists:
            self.add_patron(patron_name)

        # Check out the book for the patron
        for patron in self.patrons:
            if patron.name == patron_name:
                for book in self.books:
                    if book.isbn == isbn and not book.checked_out:
                        return patron.checkout_book(book)

        return False

    def return_book(self, patron_name, isbn):
        for patron in self.patrons:
            if patron.name == patron_name:
                for book in patron.books_checked_out:
                    if book.isbn == isbn:
                        return patron.return_book(book)
        return False

    def display_books(self):
        print("Books in the Library:")
        for book in self.books:
            print(book)

    def display_patrons(self):
        print("Library Patrons:")
        for patron in self.patrons:
            print(patron)

    def display_available_books(self):
        print("Available Books:")
        for book in self.books:
            if not book.checked_out:
                print(book)

    def display_books_checked_out_by_patron(self, patron_name):
        for patron in self.patrons:
            if patron.name == patron_name:
                print(f"Books checked out by {patron.name}:")
                for book in patron.books_checked_out:
                    print(book)
                return
        print("Patron not found.")
