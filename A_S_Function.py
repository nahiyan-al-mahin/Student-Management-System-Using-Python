#This function is to add students info

def add_student(file):
    filename = file

    # Load existing student student IDs
    existing_ids = set()
    try:
        with open(filename, "r") as students:
            for line in students:
                if line.startswith("Student ID:"):
                    existing_ids.add(line.split("Student ID:")[1].strip())
    except FileNotFoundError:
        print("\nStudent file not found.\n")

    # Input of student Name
    while True:
        New_student_name = input("Enter Student Name: ")
        if New_student_name.isdigit():
            print("\nStudent name must contain only letters.\n")
        elif New_student_name.isalpha():
            break
        else:
            print("\nStudent name must contain only letters and cannot be blank.\n")
            continue
    # Input of student ID (needs to be unique)
    while True:
        New_student_ID = input("Enter Student ID: ")

        if not New_student_ID.isdigit():
            print("\nStudent ID must contain only digits.\n")
            continue

        if New_student_ID in existing_ids:
            print("\nStudent ID already exists! Try another.\n")
            continue

        print("Student ID is available.")
        break
    #extra information
    Student_email = input("Enter Student Email: ")
    Student_Phone = input("Enter Student Phone: ")
    Student_Dept = input("Enter Student Department: ")
    Student_Batch = input("Enter Student Batch: ")

    #This part is to write student info in txt file
    with open(filename, "a") as Student_Info:
        Student_Info.write(
            "==============================\n"
            f"Student ID: {New_student_ID}\n"
            f"Student Name: {New_student_name}\n"
            f"Student Email: {Student_email}\n"
            f"Student Phone: {Student_Phone}\n"
            f"Student Department: {Student_Dept}\n"
            f"Student Batch: {Student_Batch}\n"
            "==============================\n"
        )

    print("\nStudent Info saved successfully!!!\n")




