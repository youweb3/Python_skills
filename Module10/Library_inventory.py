# Create a Book class for information such as title, author, and availability.
class Book:
    def __init__(self, title, author, available =True):
        self.title = title
        self.author = author
        self.available = available


# ===============================
# Library class to manage for all the books such as search, add, update
# ======

class Library:
    def __init__(self):
     self.all_books = [] # List to store all Book objects

     # Add Book function
    def adding_book(self, one_book):
        self.all_books.append(one_book) #add books and store in "all_books []" array

    
    # search book by title using lambda and filter
    def search_by_title(self, title):
       #lambda function to check if book title matches input
       search_title = lambda book: book.title.lower() == title.lower()
       #filter returns all books that satisfy the lambda condition
       return list(filter(search_title, self.all_books))
    
    
    # Search books by author using lambda and filter
    def search_by_author (self, author):
       # Lambda function to check if book author matches input
       search_author = lambda booking : booking.author.lower() == author.lower()
       return list(filter(search_author, self.all_books))
    
    # Update book availability
    def update_availability(self, title, available):
       # Lambda function updates availability if title matches
       update_book = lambda book: setattr(book, 'available', available) if book.title.lower() == title.lower() else None
       # Map applies the lambda to all books
       list(map(update_book, self.all_books))

#=====================================================================

# ===============================
# Sample Book instances
# ======
b1 = Book("1984", "George Orwell")
b2 = Book("Hamlet", "Shakespeare")
b3 = Book ("IT", "Yousef")


# ===============================
# Create Library instance
# =====

my_library = Library()

#==Add books to library
my_library.adding_book(b1)
my_library.adding_book(b2)
my_library.adding_book(b3)

# ===============================
# Display all books in library
# =======

print("\nAll books in library:")
for add_book in my_library.all_books:
   print(add_book.title, "-", add_book.author)

print("--------------")

# ===============================
# Search for books by title
# =====

print("\n----- Search by title -----")
found_books = my_library.search_by_title("Hamlet")
for book in found_books:
   print("Found:", book.title, "-", book.author)


# Search for books by author
# =====
print("\nBooks by author 'Yousef':")
for book in my_library.search_by_author("Yousef"):
    print(f"- {book.title} by {book.author}")#Using f-string to format output nicely

print("=======================")
#=============================
# Check availability before
print("Check availability books:")
for b in my_library.all_books:
   print(b.title, "-", "Available" if b.available else "Not Available")

# Updatebook availability
my_library.update_availability("1984", False)

# Check availability after
print("\nAvailability or Not:")
for b in my_library.all_books:
    print(b.title, "-", "Available" if b.available else "Not Available")
    print(f"-{b.title} is {'available' if b.available else 'not available'}")





#//////////////////////////////////////////////////

#     # Searching books by title with for loop
# def search_by_title(self, title):
#         results = []
#         for one_book in self.all_books:
#           if one_book.title.lower() == title.lower():
#              results.append(one_book)
#              return results

# #===Search by title
# found_books = my_library.search_by_title("1984")
# for book in found_books:
#     print("Found:", book.title, "-", book.author)