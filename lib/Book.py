class Book:
    def __init__(self, title, author, isbn):
         # Initialize Book attributes
        self.title = title
        self.author = author
        self.isbn = isbn
        self.checked_out = False
        self.borrower = None

    def check_out(self, patron_name):
        # Check out the Book to a patron
        if not self.checked_out:
            self.checked_out = True
            self.borrower = patron_name
            return True
        else:
            return False

    def return_book(self):
        if self.checked_out:
            self.checked_out = False
            self.borrower = None
            return True
        else:
            return False

    def __str__(self):
        availability = "Available" if not self.checked_out else "Checked out by " + self.borrower
        return f"{self.title} by {self.author} (ISBN: {self.isbn}) - {availability}"
