def delete_student(students):
    while True:
        try:
            student_id = int(input("Enter Student ID: "))
            selected_student = None
            break
        except ValueError:
            print("Invalid Student ID")

    while True:
        found = False

        for student in students:
            if student["ID"] == student_id:
                selected_student = student
                found = True
                break

        if found == False:
            print("Student ID Not Found")
            return students
        else:
            while True:
                confirmation = input(f"Are you sure you want to delete the record of {student_id}.\nThe following items will be deleted permanently {selected_student}.\nEnter y to delete otherwise enter anyother thing to not delete : ").lower().strip()

                if confirmation == 'y':
                    students.remove(selected_student)
                    print("Student Record Deleted")
                    return students
                else:
                    print("Nothing Deleted")
                    return students

                break
                