def search_student(students):
    
    while True:
        try:
            student_id = int(input("Enter Student ID: "))
            break
        except:
            print("Invalid ID")

    while True:

        found = False
        
        for student in students:
            if student["ID"] == student_id:
                found = True
                break
    
        if found == True:
            print(student)
            break
        else:
            print("Student Not Found")
            break