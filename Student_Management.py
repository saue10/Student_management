students = []

print("Welcome to Students Info Section :")

print("Press 1 to fetch the menu list")
var =  int(input())

if var ==1:
    print("Welcome to the Menu list :")
    print("Press 2 to add new student info.")
    print("Press 3 to get  all students info.")
    print("Press 4 to search a student info. by his name or Roll no.")
    print("Press 5 to update existing student info.")
    print("Press 6 to remove any student info.")
    print("Press any integer to get exit from the Library")


def add_new_Student(Id,Name,Age,Course,marks):
    students.append({"Id" : Id, "Name" : Name, "Age":Age, "Course":Course, "Marks": marks})
    print("Details Updated")

def all_students_info ():
    print(students)

def search_student(Id, Name):
    matched_student=[]
    for student in students:
        if student["Id"]==Id or student["Name"]==Name:
            matched_student.append(student)
            
            break
        
    if matched_student:
        print(matched_student)

    else:
        print("No details found. Please enter correct details")    
    

def update_existing(student):
    print("Press A to update his Name \n Press B to update his Age \n Press C to update his Course \n Press D to update his Marks")
    
    
    update = input("Enter your Choice:")
    if update == "A":
        updated_name = input("enter the Updated Name of the student:")
        student["Name"] = updated_name

    elif update == "B":
        updated_Age = int(input("Enter the updated age:"))
        student["Age"]=updated_Age
    elif update == "C":
        updated_course = input("Enter the updated course value you want to replace with the existing one:")
        student["Course"] = updated_course
    elif update == "D":
        updated_marks = int(input("Enter the updated marks:"))
        student["Marks"] = updated_marks
    else:
        print("No other Section Available")        



while 1:
    user_input = int(input())
    if user_input==2:
        print("Enter Students details")
        Id = int(input("Enter Student Id:"))
        Name= input("Enter student name:")
        Age = int(input("Enter Valid Age:"))
        Course = input("Enter Course Name:")
        Marks = int(input("Enter Marks Obtained in that course:"))

        add_new_Student(Id,Name,Age,Course,Marks)

    elif user_input == 3:
        all_students_info()

    elif user_input == 4:
        print("Search by your choice 1 for Id and 2 for Name")
        search = int(input("Enter Your Choice"))
        if search == 1:
            Id = int(input("enter the Id of the student whose details you want to see")) 
        elif search==2:
            Name = input("enter the name of the student about which you want the info.")
        search_student(Id,Name)

    elif user_input == 5:
        exsiting_student_id = int(input("enter the Id of the student whose details you want to update"))
        found = False
        for student in students:
            if student["Id"] == exsiting_student_id:
                found = True
                update_existing(student)
                print("Vlaue Updated")
                break
        if not found:    
            print("Student with this id is not available")    
 
    elif user_input ==6:
        removed_student_id = int(input("Enter the id of the student whose details you want to remove:"))
        found =False
        for student in students:
            if student["Id"] == removed_student_id:
                found=True
                students.remove(student)
                print("Details Removed")
                break
        if not found:    
            print("student details not available") 
                   


    else:
        break

print("Hope you completed your query")        





