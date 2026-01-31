#This function is to search students

def search_student(file):
    def searching(file,student_id):
        student_found=False

        #Checks the student id and see if it matches
        try:
            with open(file ,"r") as student_info:
                for line in student_info:
                    info=line.strip()
                    if "Student ID: " in info:
                        id = info.split("Student ID: ")[1].strip()
                        if student_found:
                            break
                        if id==student_id:
                            student_found=True
                            print("\n Student Found\n")
                    if student_found:
                        print(info.rstrip())


            if not student_found:
                print(F"\n Student ID {student_id} not found!!!\n")
        except FileNotFoundError:
            print(f"File {file} not found!!!\n")
    #Takes student input
    while True:
        student_id = input("Enter Student ID you want to search or Type ""E/e"" to exit: ")
        if student_id == "E" or student_id == "e":
            print("\n Thank You. Search Option exited!!!\n")
            break
        else:
            searching(file, student_id)
    return 0

