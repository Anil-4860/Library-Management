# Write a Library class with no_of_books and books as two instance variables.
#  Write a program to create a library from this Library class and show 
# how you can print all books, add a book and get the number of books using different methods. 
# Show that your program doesnt persist the books after the program is stopped!

class library:
  def __init__(self):

    self.books=[]
    self.no_of_Books=0
  def addBook(self,book):
    self.books.append(book)
    self.no_of_books=len(self.books)

  def showInfo(self):
    print(f"library has {self.no_of_books} books")
a=library()
a.addBook(input("enter book to add:"))
a.showInfo()
