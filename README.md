# Library Management System

The Library Management System is a Python-based command-line application that allows users to manage books and patrons in a library. It provides functionalities such as adding books, adding patrons, checking out and returning books, and displaying available books and patrons.

## Features

- **CRUD Operations**: Users can create, read, update, and delete books and patrons from the library database.
- **Book Checkout**: Patrons can check out books from the library, and the system tracks the availability of each book.
- **Book Return**: Patrons can return books to the library, updating their status to available.
- **Data Validation**: The system validates user inputs and provides informative error messages for data integrity.
- **CLI Interface**: The command-line interface provides a user-friendly way to interact with the library system.
- **SQLite Database**: The application uses SQLite as its database engine for data storage.

## Installation

1. Clone the repository:

    ```bash
    git clone git@github.com:Ob55/Library-Management-System.git
    ```

2. Navigate to the project directory:

    ```bash
    cd library-management-system
    ```

3. Install dependencies:

    ```bash
    pip install -r requirements.txt
    ```

## Usage

1. Run the main.py script to start the application:

    ```bash
    python main.py
    ```

2. Follow the on-screen instructions to navigate the application menu and perform desired operations.

## Project Structure

The project follows the following directory structure:

- **main.py**: The main entry point of the application.
- **library.py**: Contains the Library class for managing books and patrons.
- **patron.py**: Defines the Patron class for representing library patrons.
- **book.py**: Defines the Book class for representing library books.
- **database.py**: Manages the SQLite database connection and ORM functionality.
- **requirements.txt**: Contains the list of project dependencies.

## Contributing

Contributions are welcome! If you would like to contribute to this project, please fork the repository and submit a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
##Auther
brian m