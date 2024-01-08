class library:
    def __init__(self,listofBooks) :
        self.book_list=listofBooks
        self.issued_books={}
    
    def available_books(self) :
        print("books present in library :")
        for book in self.book_list:
            print(book)
    
    def borrow_book(self,name,bookname) :
        if bookname in self.book_list :
            self.issued_books[bookname]=name
            self.book_list.remove(bookname)
            print(f"--> {bookname} is borrowed by {name}\n")
        else :
            print(f"--> sorry {bookname} is not present in the library\n")

    def return_book(self,bookname) :
        if bookname in self.issued_books :
            name=self.issued_books.pop(bookname)
            self.book_list.append(bookname)
            print(f"--> {bookname} returned by {name}\n")
        else :
            print(f"this {bookname} was not issued by library\n")
    
    def donate_book(self,bookname) :
        name= input("enter your name")
        self.book_list.append(bookname)
        print(f"--> thank you {name} for donating {bookname} to the library \n")

    def issued_booklist(self) :
        for bookname,name in self.issued_books.items() :
            print(f"--> {bookname} is issued by {name}")



class Student:
    def request_book(self) :
        self.name= input("enter your name : ")
        self.bookname=input("enter the name of the book to be borrowed : ")
        return self.name,self.bookname

    def return_book(self) :
        self.name= input("enter your name : ")
        self.bookname=input("enter the bookname u want to return ")
        return self.name,self.bookname
    
    def donate_book(self) :
        self.bookname=input("enter the name of the book to be donated : ")
        return self.bookname


book_list=['book1','book2','book3','book4','book5']
IIITlibrary = library(book_list)
student = Student()

while True :
    print("\n---> 1. for display of available books : ")
    print("---> 2. for borrowing a book : ")
    print("---> 3. for returning a book :  ")
    print("---> 4. for donating a book : ")
    print("---> 5. for display issued books : ")
    print("---> 6. to exit from the program : ")

    choice = int(input("enter your choice : "))
    if choice==1 :
        IIITlibrary.available_books()
    elif choice==2 :
        name,bookname=student.request_book()
        IIITlibrary.borrow_book(name,bookname)
    elif choice==3 :
        name,bookname=student.return_book()
        IIITlibrary.return_book(bookname)
    elif choice==4 :
        bookname=student.donate_book()
        IIITlibrary.donate_book(bookname)
    elif choice==5 :
        IIITlibrary.issued_booklist()
    elif choice==6 :
        print("------>program exited----////")
        break
    else :
        print("--- INVALID CHOICE -----")