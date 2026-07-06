def add_student(students):
    
    while True:
        
        while True:
            try:
                student_id = int(input("Enter Student ID: "))
                break
            except ValueError:
                print("Please Enter Integer Value Only.")

        duplicate = False

        for student in students:
            if student["ID"] == student_id:
                duplicate = True
                print("Student ID Taken. Please Enter a New One.")
                break

        if not duplicate:
            break

    student_info = {
        "ID" : student_id,
        "Name" : input("Enter Student Name: "),
        "Class" : input("Enter Student Class (Roman Numbers): "),
        "Section" : input("Enter Student Section: ")
    }

    students.append(student_info)

    return students
    