# -*- coding: utf-8 -*-
"""Library Management System.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1hyTHm8nlqzDHCleEooXogwE4fQlOuEiI
"""

class Library:
    def __init__(self):
        self.file_name = "books.txt"
        self.file = open(self.file_name, "a+")

    def __del__(self):
        self.file.close()

    def list_books(self):
        self.file.seek(0)
        books = self.file.readlines()
        if books:
            print("*** List of Books ***")
            for book in books:
                book_info = book.strip().split(",")
                print(f"Title: {book_info[0]}, Author: {book_info[1]}")
        else:
            print("No books available.")

    def add_book(self):
        title = input("Enter book title: ")
        author = input("Enter book author: ")
        release_year = input("Enter release year: ")
        num_pages = input("Enter number of pages: ")
        book_info = f"{title},{author},{release_year},{num_pages}\n"
        self.file.write(book_info)
        print(f"Book '{title}' added successfully.")

    def remove_book(self):
        title = input("Enter the title of the book to remove: ")
        self.file.seek(0)
        books = self.file.readlines()
        updated_books = []
        removed = False
        for book in books:
            book_info = book.strip().split(",")
            if book_info[0] == title:
                removed = True
            else:
                updated_books.append(book)
        if removed:
            self.file.seek(0)
            self.file.truncate()
            for book in updated_books:
                self.file.write(book)
            print(f"Book '{title}' removed successfully.")
        else:
            print(f"Book '{title}' not found.")

# Create an object named “lib” with “Library” class.
lib = Library()

# Create a menu to interact with the “lib” object.
while True:
    print("*** MENU ***")
    print("1) List Books")
    print("2) Add Book")
    print("3) Remove Book")
    print("Q) Quit")

    choice = input("Enter your choice: ")

    if choice == "1":
        lib.list_books()
    elif choice == "2":
        lib.add_book()
    elif choice == "3":
        lib.remove_book()
    elif choice == "Q":
        print("Exiting...")
        break
    else:
        print("Invalid choice. Please enter a valid option.")