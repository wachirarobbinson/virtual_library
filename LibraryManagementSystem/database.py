import sqlite3
import datetime

def initialize_database():
    connection = sqlite3.connect("books.db")
    cursor = connection.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS books (
            id INTEGER PRIMARY KEY,
            title TEXT,
            author TEXT
        )
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS rented_books (
            id INTEGER PRIMARY KEY,
            book_id INTEGER,
            renter_name TEXT,
            rent_date DATE,
            return_date DATE,
            location TEXT,
            returned INTEGER DEFAULT 0,
            FOREIGN KEY (book_id) REFERENCES books (id)
        )
    ''')

    connection.commit()
    connection.close()

def add_initial_books():
    connection = sqlite3.connect("books.db")
    cursor = connection.cursor()

    books = [
        ("Petals of Blood", "Ngũgĩ wa Thiong’o"),
        ("Thursdays", "Jackson Biko"),
        ("The Havoc of Choice", "Wanjiru Koinange"),
        ("A Kenyan Christmas", "John Kimani"),
        ("A Mama for Owen", "Jane Oliech"),
        ("For You Are a Kenyan Child", "Brian Chege"),
    ]

    for book in books:
        cursor.execute("INSERT INTO books (title, author) VALUES (?, ?)", book)

    connection.commit()
    connection.close()

def list_books():
    connection = sqlite3.connect("books.db")
    cursor = connection.cursor()

    cursor.execute("SELECT * FROM books")
    books = cursor.fetchall()

    for book in books:
        print(f"ID: {book[0]}, Title: {book[1]}, Author: {book[2]}")

    connection.close()

def rent_book(book_id, renter_name, days_to_rent):
    connection = sqlite3.connect("books.db")
    cursor = connection.cursor()

    rent_date = datetime.date.today()
    return_date = rent_date + datetime.timedelta(days=days_to_rent)

    cursor.execute("INSERT INTO rented_books (book_id, renter_name, rent_date, return_date) VALUES (?, ?, ?, ?)",
                   (book_id, renter_name, rent_date, return_date))

    connection.commit()
    connection.close()

def return_book(rent_id):
    connection = sqlite3.connect("books.db")
    cursor = connection.cursor()

    cursor.execute("UPDATE rented_books SET returned = 1 WHERE id = ?", (rent_id,))

    connection.commit()
    connection.close()

def search_books(query):
    connection = sqlite3.connect("books.db")
    cursor = connection.cursor()

    cursor.execute("SELECT * FROM books WHERE title LIKE ? OR author LIKE ?", ('%' + query + '%', '%' + query + '%'))
    books = cursor.fetchall()

    if not books:
        print("No matching books found.")
    else:
        print("Matching books:")
        for book in books:
            print(f"ID: {book[0]}, Title: {book[1]}, Author: {book[2]}")

    connection.close()
