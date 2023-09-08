import datetime
from database import (
    initialize_database,
    list_books,
    rent_book,
    return_book,
    search_books,
)

def main():
    # Create a dictionary to store book locations
    book_locations = {}

    initialize_database()

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
            # Rent a book
            book_id = int(input("Enter book ID to rent: "))
            renter_name = input("Enter your name: ")

            days_to_rent = int(input("Enter the number of days to rent the book: "))

            # Check if the book exists
            if book_id in book_locations:
                location = book_locations[book_id]
                rent_book(book_id, renter_name, days_to_rent, location)
                return_date = datetime.date.today() + datetime.timedelta(days=days_to_rent)
                print(f"Book rented successfully! Return by {return_date}")
                print(f"Book location in the library: {location}")
            else:
                print("Book not found in the library.")

        elif choice == "3":
            # Return a book
            rent_id = int(input("Enter rent ID to return: "))
            return_book(rent_id)
            print("Book returned successfully!")

        elif choice == "4":
            # Search for a book
            query = input("Enter book title or author to search: ")
            search_books(query)

        elif choice == "5":
            print("Have a nice day!")
            break

if __name__ == "__main__":
    main()
