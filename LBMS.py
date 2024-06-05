#LMS -> Library Management System

'''Features?
-> Display all books
-> Add a book
-> Delete a book
-> Issue a book
-> Return a book

'''

books = [
    "Twisted Love", "The Theory of Everything", "Harry Potter",
    "Bhagwat Geeta", "Ikigai", "The Ramayana", "The Love"
]

issued_books = []

#Display books


def display(books):
  count = 1

  for book in books:
    print(f"{count}. {book}")
    count += 1


# Add a book


def addBook():
  book = input("Enter the name of the book: ")
  books.append(book)
  print("The books has been added in the Library successfully!")


#Delete a book


def deleteBook():
  display(books)

  n = int(input("Enter the id of the book: "))
  books.pop(n - 1)
  print("The book has been deleted successfully!")


# Issue a book


def issueBook():
  display(books)

  book_id = int(input("Enter the id of the book: "))
  issued_books.append(books[book_id - 1])
  books.pop(book_id - 1)

  print("The book has been issued successfully!")


# Return a book


def returnBook():
  display(issued_books)

  book_id = int(input("Enter the id of the book: "))
  books.append(issued_books[book_id - 1])
  issued_books.pop(book_id - 1)

  print("The book has been returned successfully!")


# MAIN Program

while 1:
  print("1. Display all books")
  print("2. Add a book")
  print("3. Delete a book")
  print("4. Issue a book")
  print("5. Return a book")
  print("6. Exit")

  user = int(input("Enter your choice: "))
  print()

  if user == 1:
    display(books)

  elif user == 2:
    addBook()

  elif user == 3:
    deleteBook()

  elif user == 4:
    issueBook()

  elif user == 5:
    returnBook()

  elif user == 6:
    print("Thanks for using our software...")
    break

  else:
    print("Invalid Input. Please Try Again!")

  print("=" * 20 + " RESTART " + "=" * 20)
