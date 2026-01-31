from S_M_Function import show_menu
from A_S_Function import add_student
from R_S_Function import remove_student
from S_S_Function import search_student
from Sh_S_Function import show_student
from Designer import developer

file= "Information_Students.txt"
try:
    with open(file,'x') as student_file:
        student_file.write("==========Student Management System=========\n")
except FileExistsError:
    pass

print("\n----------Welcome to Student Database Management----------\n")
while True:
    show_menu()
    print("Enter your option(1-6):")
    choice=input()
    if not choice.isdigit():
        print("Please enter a valid option")
        continue
    elif choice.isdigit():
        choice=int(choice)
    if choice==0 or choice>6:
        print("Wrong Option")
    if choice==1:
        add_student(file)
    if choice==2:
        show_student(file)
    if choice==3:
        search_student(file)
    if choice==4:
        remove_student(file)
    if choice==5:
        developer()
    if choice==6:
        print("Thank you for using this program.Have a nice day!")
        quit()





