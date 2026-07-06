# print('👇')

# print("--------------------STUDENT MANAGEMENT SYSTEM--------------------")
# print()
# print("Options 👇")
# print("Enter 1 to \"Add a Student\"")
# print("Enter 2 to \"View all Students\"")
# print("Enter 3 to \"Search a Student\"")
# print("Enter 4 \"Update Student Details\"")
# print("Enter 5 \"Delete a Student\"")

#   for stud in students:
#         if student["ID"] == stud["ID"]:
#             non_duplicate == True
#         else:
#             non_duplicate == False

        
#         if non_duplicate == False:
#             students.append(student)
#             return students
#         else:
#             student["ID"] = int(input("Student ID Already Available Please Create a New One: "))

# while True:

#     try:
#         student_id = int(input("Enter Student ID: "))
#         break
#     except ValueError:
#         print("Please Enter Integer Value Only.")











# def update_details(students):

#     while True:
#         try:
#             student_id = int(input("Enter Student ID: "))
#             break
#         except ValueError:
#             print("Invalid Student ID")
    
#     while True:

#         found = False

#         for student in students:
#             if student["ID"] == student_id:
#                 found = True

#                 print("Enter 1 to Update Student ID")
#                 print("Enter 2 to Update Student Name")
#                 print("Enter 3 to Update Student Class")
#                 print("Enter 4 to Update Student Section")
#                 print("Enter 0 t0 Exit")
#                 print()

#                 while True:
#                     try:
#                         choice = int(input("Enter Your Choice: "))
#                         break
#                     except ValueError:
#                         print("Invalid Choice")
                
#                 if choice == 0:
#                     print("Exit Successfull")
#                 elif choice == 1:

#                     while True:
        
#                         while True:
#                             try:
#                                 new_student_id = int(input("Enter Student ID: "))
#                                 break
#                             except ValueError:
#                                 print("Please Enter Integer Value Only.")

#                         duplicate = False

#                         for student in students:
#                             if student["ID"] == new_student_id:
#                                 duplicate = True
#                                 idx = students.index(student)
#                                 break

#                         if duplicate == True:
#                             print("Student ID Already Taken")
#                             break
#                         else:
#                             students[idx]["ID"] = new_student_id
#                             break






# lst = [1,2,3,4,5]

# print(lst)

# for i in lst:
#     if i==2:
#         idx = lst.index(i)
#         break

# lst.remove(idx)

# print(lst)