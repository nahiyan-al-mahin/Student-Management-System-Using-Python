#This function is to show Students info

def show_student(file):
    #reads the whole txt file
    print("\n=========== Student List Starts Here ===========\n")
    Students_file=open(file,"r")
    Student_Info = Students_file.read()
    print(Student_Info)
    Students_file.close()
    print("\n=========== Student List Ends Here =============\n")

