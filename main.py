# Task1     Use SQLite (Database Integration)
import sqlite3

# Connect to SQLite database
conn = sqlite3.connect('library.db')
cursor = conn.cursor()

# Create books table
cursor.execute('''
CREATE TABLE IF NOT EXISTS books (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    author TEXT NOT NULL,
    genre TEXT NOT NULL,
    availability_status TEXT NOT NULL
)
''')

conn.commit()


def create_book(title, author, genre, availability_status='Available'):
    cursor.execute('''
    INSERT INTO books (title, author, genre, availability_status)
    VALUES (?, ?, ?, ?)
    ''', (title, author, genre, availability_status))
    conn.commit()


def read_books():
    cursor.execute('SELECT * FROM books')
    return cursor.fetchall()


def update_book(book_id, title, author, genre, availability_status):
    cursor.execute('''
    UPDATE books
    SET title = ?, author = ?, genre = ?, availability_status = ?
    WHERE id = ?
    ''', (title, author, genre, availability_status, book_id))
    conn.commit()


def delete_book(book_id):
    cursor.execute('DELETE FROM books WHERE id = ?', (book_id,))
    conn.commit()


def search_books(field, value):
    query = f"SELECT * FROM books WHERE {field} LIKE ?"
    cursor.execute(query, ('%' + value + '%',))
    return cursor.fetchall()


def borrow_book(book_id):
    cursor.execute('''
    UPDATE books
    SET availability_status = 'Borrowed'
    WHERE id = ?
    ''', (book_id,))
    conn.commit()


def return_book(book_id):
    cursor.execute('''
    UPDATE books
    SET availability_status = 'Available'
    WHERE id = ?
    ''', (book_id,))
    conn.commit()


def sort_books(field, order='ASC'):
    query = f"SELECT * FROM books ORDER BY {field} {order}"
    cursor.execute(query)
    return cursor.fetchall()


def filter_books(field, value):
    query = f"SELECT * FROM books WHERE {field} = ?"
    cursor.execute(query, (value,))
    return cursor.fetchall()


def generate_report(report_type):
    if report_type == 'borrowed':
        cursor.execute("SELECT * FROM books WHERE availability_status = 'Borrowed'")
    elif report_type == 'overdue':
        cursor.execute("SELECT * FROM books WHERE availability_status = 'Overdue'")
    return cursor.fetchall()


def main():
    while True:
        print("\nLibrary Management System")
        print("1. Add a Book")
        print("2. View Books")
        print("3. Update a Book")
        print("4. Delete a Book")
        print("5. Search for Books")
        print("6. Borrow a Book")
        print("7. Return a Book")
        print("8. Exit")
        print("9. Sort Books")
        print("10. Filter Books")
        print("11. Generate Report")

# Task2     Functionality

        choice = input("Enter your choice: ")

        if choice == '1':
            title = input("Enter book title: ")
            author = input("Enter book author: ")
            genre = input("Enter book genre: ")
            create_book(title, author, genre)
            print("Book added successfully.")
        elif choice == '2':
            books = read_books()
            for book in books:
                print(book)
        elif choice == '3':
            book_id = input("Enter book ID to update: ")
            title = input("Enter new title: ")
            author = input("Enter new author: ")
            genre = input("Enter new genre: ")
            availability_status = input("Enter availability status: ")
            update_book(book_id, title, author, genre, availability_status)
            print("Book updated successfully.")
        elif choice == '4':
            book_id = input("Enter book ID to delete: ")
            delete_book(book_id)
            print("Book deleted successfully.")
        elif choice == '5':
            field = input("Search by (title/author/genre): ")
            value = input(f"Enter {field}: ")
            books = search_books(field, value)
            for book in books:
                print(book)
        elif choice == '6':
            book_id = input("Enter book ID to borrow: ")
            borrow_book(book_id)
            print("Book borrowed successfully.")
        elif choice == '7':
            book_id = input("Enter book ID to return: ")
            return_book(book_id)
            print("Book returned successfully.")

#       Task4  Advance Features

        elif choice == '8':
            print("Exiting...")
            break
        elif choice == '9':
            field = input("Sort by (title/author/genre/availability_status): ")
            order = input("Order (ASC/DESC): ")
            books = sort_books(field, order)
            for book in books:
                print(book)
        elif choice == '10':
            field = input("Filter by (genre/availability_status): ")
            value = input(f"Enter {field}: ")
            books = filter_books(field, value)
            for book in books:
                print(book)
        elif choice == '11':
            report_type = input("Generate report for (borrowed/overdue): ")
            books = generate_report(report_type)
            for book in books:
                print(book)
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()