# 21/02/25
# file handling and exception handling
from pathlib   import  Path
import os
def create_folder():
    try:
        name = input(" name of your folder? :-")
        p= Path(name) # aur ye current location dega file create karwane ke liye .
        p.mkdir()  # ye folder create karwata hai 
    except Exception as err:
        print("Error occured")   
create_folder()
#rglob files read karne ke loye use hota hai 
def read_folder():
    p=Path("")
    items = list(p.rglob("*")) 
    for i,v in enumerate(items):
        print(f"{i+1} : {v}")
    # for i in range(len(items)) :
    #     print(f"{i+1} : {items[i]}")   
read_folder()
def update_folder():
    try:
        old_name = input("old name of file")
        p=Path(old_name)
        if p.exists():  # usko direct change nhi kar 
            new_name = input("Enter new name of folder")
            newp = Path(new_name)
            p.rename(newp)
            print(f"{old_name} renamed to {new_name}")
    except Exception as err:
        print("Error occured")        
update_folder() 
def delete_folder():
    try:
        read_folder()
        nmae = input("Enter folder nmae to be deleted:")
        p= Path(nmae)
        if p.exsists():
            p.rmdir()
            print("Malik folder hat gaya")       
    except Exception as error:
        print("error occured")
#with open use karene pe file ka naam aur operation  dono dena padega 
def create_file():
    read_folder()
    folder_name= input("Enter folder name:")





def read_file():
    read_folder()
    nmae=input("enter folder nmae :")
                         



    print("press 1 for create folder")
    print("press 2 for read folder")
    print("press 3 for update folder")
    print("press 4 for delete folder")
    print("press 5 for creating file")
    print("press 6 for reading the file")
check = input("give you response:-")
if check ==1:
    create_folder()

elif check == "2":
    read_folder()

elif check == "3":
    update_folder()

elif check == "4":
    delete_folder()

elif check == "5":
    create_file()

elif check == "6":
    read_file()

elif check == "8":
    delete_folder()

elif check == "7":
    update_folder()

