# Student Management System

import json
from Add_a_Student import add_student
from tabulate import tabulate
from Search_a_Student import search_student
from Update_Student_Details import update_details
from Delete_a_Student import delete_student

FILE_NAME = 'students.json'

def load_data():
    try:
        with open(FILE_NAME,'r') as file:
            return json.load(file)
    except(FileNotFoundError,):
        return []

def save_data(students):
    with open(FILE_NAME,'w') as file:
        json.dump(students,file,indent=4)


students = load_data()

while True:
    
    # Menu
    print("-----------------------STUDENT MANAGEMENT SYSTEM-----------------------")
    print()
    print("Options 👇")
    print()
    print("Enter 1 to \"Add a Student\"")
    print("Enter 2 to \"View all Students\"")
    print("Enter 3 to \"Search a Student\"")
    print("Enter 4 to \"Update Student Details\"")
    print("Enter 5 to \"Delete a Student\"")
    print("Enter 0 to \"Exit\"")
    print()

    while True:
        try:
            user_choice = int(input("Enter your choice (0-5): "))
            break
        except ValueError:
            print("Invalid Choice")

    if user_choice not in [0,1,2,3,4,5]:
        print("Invalid Choice")
        continue
    elif user_choice == 1:
        students = add_student(students)
        save_data(students)
        print("Student Added Successfully")
    elif user_choice == 2:
        print(tabulate(students, headers="keys", tablefmt="grid"))
    elif user_choice == 3:
        search_student(students)
    elif user_choice == 4:
        update_details(students)
        save_data(students)
        print("Student Details Updated Successfully")
    elif user_choice == 5:
        students = delete_student(students)
        save_data(students)        
    elif user_choice == 0:
        print("--------------------Program Successfully Terminated--------------------")
        break

