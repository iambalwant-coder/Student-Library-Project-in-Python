class library:
    def __init__(self, list_of_books):
        self.list_of_books = list_of_books
    
    def display_available_books(self):
        print("Books present in library are :- ")
        
        for books in self.list_of_books:
            print(" * " + books)

    def borrow_book(self , book_name):
        if book_name in self.list_of_books:
            print(f"You have been issue {book_name}, Please keep it safe and return it within 30 days.")
            self.list_of_books.remove(book_name)
            return True
        else:
            print("Sorry this book is either not available or has already been issued to someone else. Please wait until book available.")

    def return_book(self, book_name):
        self.list_of_books.append(book_name.capitalize())
        print("Thanks for returning this book ! i hope you enjoyed reading it. Have a great day head!")


class student:
    def reqest_book(self):
        self.book = input("Enter the name of the book you want to borrow: ")
        return self.book

    def return_book(self):
        self.book = input("Enter the name of the book you want to return: ")
        return self.book


if __name__=="__main__":
    central_library = library(["Algoritham","Django","Python","JAVA","CPP"])

    stud = student()
    # central_library.display_available_books()
    
    while True:
        welcomeMsg = '''\n ====== Welcome to Central Library ======
        Please choose an option:
        1. List all the books
        2. Request a book
        3. Add/Return a book
        4. Exit the Library
        '''
        print(welcomeMsg)
        a = int(input("Enter a choice: "))
        if a == 1:
            central_library.display_available_books()

        elif a == 2:
            central_library.borrow_book(stud.reqest_book())

        elif a == 3:
            central_library.return_book(stud.return_book())
            
        elif a == 4:
            print("Thanks for choosing Central Library. Have a great day ahead!")
            exit()
        else:
            print("Invalid Choice!")