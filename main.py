from pathlib import Path

cli_row="*"*13

class Book:

    def __init__(self):
        pass



class Library:


    def __init__(self, txt_file):
        self.txt_file=open(txt_file, "a+")
        self.txt_file.seek(0)

    def __del__(self):
        self.txt_file.close()

               
    def listBooks(self):
        book_list=[]
        book_string=""
        for line in self.txt_file:
            book_string+=line 
        book_list=book_string.splitlines()
        print(book_list)

        

    def addBook(self, book_obj):
        pass
    
    def removeBook(self):
        pass 


lib=Library("books.txt")

while True:
    print(cli_row)
    print("1) List Books")
    print("2) Add Book")
    print("3) Remove Book")
    print("Q) Quit")
    print(cli_row+"\n")
    
    choice=input("Choose menu item: ")

    if choice=="1":
        lib.listBooks()
    elif choice=="2":
        pass
    elif choice=="3":
        pass
    elif choice=="q" or choice =="Q":
        del lib
        break

    else:
        print("Invalid input, please choose a valid menu item")
        continue



print("Exited successfully")
