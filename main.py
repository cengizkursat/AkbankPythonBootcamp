from pathlib import Path

cli_row="*"*13


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



    def addBookAlternative(self):
        
        newBook={"Title": None, "Author": None, "Release Year": None, "No of Pages": None}
        helper_string_list=["book title", "author", "release year", "number of pages"]
        j=0
        
        for i in newBook.keys():
            newBook[i]=input(f"Enter the {helper_string_list[j]}: ")
            j+=1
        
    

        
    
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
        lib.addBook()
    elif choice=="3":
        pass
    elif choice=="q" or choice =="Q":
        del lib
        break

    else:
        print("Invalid input, please choose a valid menu item")
        continue



print("Exited successfully")
