import datetime
from database import initialize_database, add_initial_books, list_books, rent_book, return_book, search_books

def rent_a_book():
    book_id = int(input("Enter book ID to rent: "))
    renter_name = input("Enter your name: ")

    try:
        days_to_rent = int(input("Enter the number of days to rent the book: "))
    except ValueError:
        print("Invalid input for days to rent. Please enter a valid number.")
        return

    rent_book(book_id, renter_name, days_to_rent)

def return_a_book():
    rent_id = int(input("Enter rent ID to return: "))
    return_book(rent_id)

def search_for_book():
    query = input("Enter book title or author to search: ")
    search_books(query)

def main():
    # Initialize the database and add initial books if needed
    initialize_database()
    add_initial_books()

    while True:
        print("\n*** Virtual Library Management System ***")
        print("1. List Books")
        print("2. Rent a Book")
        print("3. Return a Book")
        print("4. Search for a Book")
        print("5. Quit")

        choice = input("Enter your choice: ")

        if choice == "1":
            list_books()

        elif choice == "2":
            rent_a_book()

        elif choice == "3":
            return_a_book()

        elif choice == "4":
            search_for_book()

        elif choice == "5":
            print("Have a nice day!")
            break

if __name__ == "__main__":
    main()
