def update_details(students):

    while True:
        try:
            student_id = int(input("Enter ID of the student whose details needs to be updated: "))
        except ValueError:
            print("Invalid Student ID")
            continue

        found = False

        selected_student = None

        for student in students:
            if student["ID"] == student_id:
                selected_student = student
                found = True
                break

        if found == False:
            print("Student Not Available")
        else:
            break
            
                

    while True:

        print()
        print("Enter 1 to Update Student ID")
        print("Enter 2 to Update Student Name")
        print("Enter 3 to Update Student Class")
        print("Enter 4 to Update Student Section")
        print("Enter 0 to Exit")
        print()

        while True:
            try:
                choice = int(input("Enter your choice: "))
                print()
                break
            except ValueError:
                print("Invalid Choice")

        if choice == 0:
            break

        elif choice == 1:

            while True:

                while True:
                    try:
                        new_student_id = int(input("Enter new student ID: "))
                        print()
                        break
                    except ValueError:
                        print("Invalid Student ID")

                duplicate = False

                for student in students:
                    if student is not selected_student and student["ID"] == new_student_id:
                        duplicate = True
                        break

                if duplicate == True:
                    print("Student ID Already Taken")
                    print()
                    continue
                else:
                    selected_student["ID"] = new_student_id
                    print("Student ID Selected Successfully.\n")
                    break
        
        elif choice == 2:
            
            while True:
                new_name = input("Enter New Name: ").strip()

                if new_name == '':
                    print("Name connot be empty.")
                else:
                    break
                
            selected_student["Name"] = new_name
            print("Student Name Updated Successfully.\n")
        
        elif choice == 3:

            while True:
                new_class = input("Enter New Class: ").strip()
                
                if new_class == '':
                    print("Class cannot be empty.")
                else:
                    break

            selected_student["Class"] = new_class
            print("Student Class Updated Successfully.\n")

        elif choice == 4:

            while True:
                new_section = input("Enter New Section: ").strip()

                if new_section == '':
                    print("Section cannot be empty.")
                else:
                    break

            selected_student["Section"] = new_section
            print("Student Section Updated Successfully.")
