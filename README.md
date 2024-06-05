# Library-Management-System

'''Features ?
-> Issue a book
-> Return a book
-> Display all books
-> Add a book
-> Delete a book
'''
#====================== Asking for login ========================


def login():
  User_Name = input('Enter the User Name : ').upper()
  password = input('Enter the Password : ')
  if User_Name == "KartikeyGupta" and password == "@123*99&123$...":
    return True
  else:
    print('Your User Name OR Password is wrong please try again')


login()

#======================= Checking security ======================


def security_check():
  if not login():
    return


security_check()

books = "hello byebye".split()

issued_books = []


#==================== display all books ============================
def display(books):
  count = 1
  for book in books:
    print(f'{count}. {book}')
    count += 1


#======================== Add new books =============================


def addBook():
  n = int(input('How many do you want to add : '))
  for number in range(1, n + 1):

    book_name = input("Enter the name of the book ")
    books.append(book_name)
  print("The book has been added to the Library Sucessfully!")


#======================= Delete a book ===============================


def deleteBook():
  display(books)
  n = int(input('Enter the id of the book '))
  books.pop(n - 1)
  print('Book has been deleted successfully')


# ========================== issue book =============================


def issueBook():
  display(books)
  book_id = int(input('Enter the id of the book '))
  issued_books.append(books[book_id - 1])
  books.pop(book_id - 1)
  print('The book has been issued successfully!')


# =========================== return the book =======================


def returnBook():
  if (len(issued_books) == 0):
    print('There is no book issued')
    return
  else:
    display(issued_books)
    book_id = int(input('enter the id of book '))
    books.append(issued_books[book_id - 1])
    issued_books.pop(book_id - 1)
    print("The book is returned successfully!")


# ====== Main Program =======
while 1:
  print('1. Display Books')
  print('2. Add a Book')
  print('3. Delete a Book')
  print('4. Issue a Book')
  print('5. Return a Book')
  print('6. Exit')

  user = int(input('Enter the choice : '))
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
    print("Invalid Entry")

  print()
  print("= " * 20, "RESTART", " =" * 20)
  print()
