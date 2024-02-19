import os

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
        
        for item in book_list:
            temp_list=item.split(",")
            print(f"Book: {temp_list[0]}, Author: {temp_list[1]}")  

    def addBook(self):

        helper_string_list=["book title", "author", "release year", "number of pages"]
        book_string=""

        for i in range (len(helper_string_list)):
            book_string+=input(f"Enter the {helper_string_list[i]}: ")
            book_string+=", "
        
        self.txt_file.write("\n"+book_string)
        
    def removeBook(self):
        
        book_string=""
        book_list=[]

        to_be_removed=input("Enter the title of the book to be removed: ")
    
        for line in self.txt_file:
            book_string+=line 
        
        book_list=book_string.splitlines()
        loop_counter=0

        for item in book_list:
            temp_list=item.split(",")
            del temp_list[-1]
            
            if temp_list[0]==to_be_removed:
                break
    
            loop_counter+=1
        
        del book_list[loop_counter]
        self.txt_file.close()
        new_file=open("books.txt", "w+")

        for item in book_list:
            new_file.write(item+"\n")
        
        new_file.close()

lib=Library("books.txt")
cli_row="*"*13

while True:
    print(cli_row)
    print("MODEST LIBRARY DATABASE ver. 1.0")
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
        lib.addBook()
    elif choice=="3":
        lib.removeBook()
        del lib
        lib=Library("books.txt")
    elif choice=="q" or choice =="Q":
        del lib
        break

    else:
        print("Invalid input, please choose a valid menu item")
        continue



print("Exited successfully")
