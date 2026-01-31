#This is to remove student

def remove_student(file):

    #Takes input of the id that needs to be removed
    while True:
        remove_student_id = input("Enter Student ID you want to remove "
                                  "or enter E/e to exit: ")
        if remove_student_id == "E" or remove_student_id == "e":
            print("\nThank You. Remove student option exited!\n")
            break

        try:
            #stores txt file in one place
            with open(file, "r") as f:
                lines = f.readlines()

            delete = False
            student_found = False

            #finds the student id by checking between previous txt info
            with open(file, "w") as f:
                for line in lines:
                    info = line.strip()

                    # This is to detect Student ID
                    if info.startswith("Student ID:"):
                        current_id = info.split("Student ID:")[1].strip()

                        if current_id == remove_student_id:
                            delete = True
                            student_found = True
                            print("\nStudent Found & Removed\n")
                            continue

                    # This is to the end of a student block
                    if delete and info.startswith("="):
                        delete = False
                        continue

                    # This is to write only non-deleted content
                    if not delete:
                        f.write(line)

            if not student_found:
                print("\nStudent ID not found!\n")

        except FileNotFoundError:
            print(f"\nStudent file '{file}' not found\n")
