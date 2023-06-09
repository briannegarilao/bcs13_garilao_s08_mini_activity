# author: briannegarilao

class Book:
    def __init__(self, title, author, publication_year):
        self.title = title
        self.author = author
        self.publication_year = publication_year
        self.is_available = True

    def get_title(self):
        return self.title

    def get_author(self):
        return self.author

    def get_publication_year(self):
        return self.publication_year

    def is_book_available(self):
        return self.is_available

    def borrow_book(self):
        if self.is_available:
            self.is_available = False
            return True
        else:
            return False

    def return_book(self):
        if not self.is_available:
            self.is_available = True
            return True
        else:
            return False


library = []

while True:
    print("Add a new book to the library:")
    title = input("Enter the title: ")
    author = input("Enter the author: ")
    publication_year = input("Enter the publication year: ")

    book = Book(title, author, publication_year)
    library.append(book)

    choice = input("Do you want to add another book? (Y/N): ")
    if choice.lower() != 'y':
        break

print("\nAvailable books in the library:")
for index, book in enumerate(library):
    if book.is_book_available():
        print(f"{index + 1}. {book.get_title()} by {book.get_author()} ({book.get_publication_year()})")

if len(library) > 0:
    book_index = int(input("\nEnter the index of the book you want to borrow: ")) - 1
    if 0 <= book_index < len(library):
        book = library[book_index]
        if book.borrow_book():
            print(f"\nSuccessfully borrowed the book: {book.get_title()}")
        else:
            print("\nThe chosen book is not available for borrowing.")
    else:
        print("\nInvalid book index.")

    print("\nAvailable books in the library:")
    for index, book in enumerate(library):
        if book.is_book_available():
            print(f"{index + 1}. {book.get_title()} by {book.get_author()} ({book.get_publication_year()})")

    if len(library) > 0:
        book_index = int(input("\nEnter the index of the book you want to return: ")) - 1
        if 0 <= book_index < len(library):
            book = library[book_index]
            if book.return_book():
                print(f"\nSuccessfully returned the book: {book.get_title()}")
            else:
                print("\nThe chosen book is already available.")
        else:
            print("\nInvalid book index.")

    print("\nAvailable books in the library:")
    for index, book in enumerate(library):
        if book.is_book_available():
            print(f"{index + 1}. {book.get_title()} by {book.get_author()} ({book.get_publication_year()})")
else:
    print("\nThe library is empty.")
