from library import Library, Book, Patron

def main():
    library = Library()

    # Adding initial books and patrons
    library.add_book("book: The Great Gatsby", "F. Scott Fitzgerald", "01")
    library.add_book("book: To Kill a Mockingbird", "Harper Lee", "02")
    library.add_book("book: Pride and Prejudice", "Jane Austen", "03")
    library.add_book("book: 1984", "George Orwell", "04")
    library.add_book("book: The Catcher in the Rye", "J.D. Salinger", "05")
    library.add_book("book: Harry Potter and the Philosopher's Stone", "J.K. Rowling", "06")
    library.add_book("book: The Hobbit", "J.R.R. Tolkien", "07")
    library.add_book("book: The Lord of the Rings", "J.R.R. Tolkien", "08")
    library.add_book("book: The Chronicles of Narnia", "C.S. Lewis", "09")

    while True:
        print("\n1. Display Available Books")
        print("2. Check Out a Book")
        print("3. Return a Book")
        print("4. Add a Book")
        print("5. Quit")

        choice = input("Enter your choice: ")

        if choice == "1":
            library.display_available_books()
        elif choice == "2":
            patron_name = input("Enter your name: ")
            library.display_available_books()
            isbn = input("Enter the ISBN of the book you want to check out: ")
            if library.lend_book(patron_name, isbn):
                print("Book checked out successfully.")
            else:
                print("Book not available or patron not found.")
        elif choice == "3":
            patron_name = input("Enter your name: ")
            library.display_books_checked_out_by_patron(patron_name)
            isbn = input("Enter the ISBN of the book you want to return: ")
            if library.return_book(patron_name, isbn):
                print("Book returned successfully.")
            else:
                print("Book not found or not checked out by the patron.")
        elif choice == "4":
            title = input("Enter the title of the book: ")
            author = input("Enter the author of the book: ")
            isbn = input("Enter the ISBN of the book: ")
            library.add_book(title, author, isbn)
            print("Book added successfully.")
        elif choice == "5":
            print("Thank you for using the library management system. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a valid option.")

if __name__ == "__main__":
    main()

