# database.py
import datetime
from sqlalchemy import create_engine, Column, Integer, String, Date, ForeignKey
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# Define the SQLAlchemy Base
Base = declarative_base()

class Book(Base):
    __tablename__ = 'books'

    id = Column(Integer, primary_key=True)
    title = Column(String)
    author = Column(String)

class RentedBook(Base):
    __tablename__ = 'rented_books'

    id = Column(Integer, primary_key=True)
    book_id = Column(Integer, ForeignKey('books.id'))
    renter_name = Column(String)
    rent_date = Column(Date)
    return_date = Column(Date)
    returned = Column(Integer, default=0)

class User(Base):
    __tablename__ = 'users'

    user_id = Column(Integer, primary_key=True)
    username = Column(String)

def initialize_database():
    # Create an SQLite database and tables using SQLAlchemy
    engine = create_engine('sqlite:///books.db')
    Base.metadata.create_all(engine)

def add_initial_books():
    # Create initial books using SQLAlchemy
    engine = create_engine('sqlite:///books.db')
    Session = sessionmaker(bind=engine)
    session = Session()

    books = [
        Book(title="Petals of Blood", author="Ngũgĩ wa Thiong’o"),
        Book(title="Thursdays", author="Jackson Biko"),
        Book(title="The Havoc of Choice", author="Wanjiru Koinange"),
        Book(title="A Kenyan Christmas", author="John Kimani"),
        Book(title="A Mama for Owen", author="Jane Oliech"),
        Book(title="For You Are a Kenyan Child", author="Brian Chege"),
    ]

    session.add_all(books)
    session.commit()
    session.close()

def list_books():
    engine = create_engine('sqlite:///books.db')
    Session = sessionmaker(bind=engine)
    session = Session()

    books = session.query(Book).all()

    for book in books:
        print(f"ID: {book.id}, Title: {book.title}, Author: {book.author}")

    session.close()

def rent_book(book_id, renter_name, days_to_rent):
    engine = create_engine('sqlite:///books.db')
    Session = sessionmaker(bind=engine)
    session = Session()

    rent_date = datetime.date.today()
    return_date = rent_date + datetime.timedelta(days=days_to_rent)

    rented_book = RentedBook(book_id=book_id, renter_name=renter_name, rent_date=rent_date, return_date=return_date)
    session.add(rented_book)
    session.commit()
    session.close()

def return_book(rent_id):
    engine = create_engine('sqlite:///books.db')
    Session = sessionmaker(bind=engine)
    session = Session()

    rented_book = session.query(RentedBook).filter_by(id=rent_id).first()
    if rented_book:
        rented_book.returned = 1
        session.commit()
    else:
        print("Book with ID not found in rentals.")

    session.close()

def search_books(query):
    engine = create_engine('sqlite:///books.db')
    Session = sessionmaker(bind=engine)
    session = Session()

    books = session.query(Book).filter(
        (Book.title.like(f'%{query}%')) | (Book.author.like(f'%{query}%'))
    ).all()

    if not books:
        print("No matching books found.")
    else:
        print("Matching books:")
        for book in books:
            print(f"ID: {book.id}, Title: {book.title}, Author: {book.author}")

    session.close()
