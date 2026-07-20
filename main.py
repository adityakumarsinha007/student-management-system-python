print("="*50)
print("            STUDENT MANAGEMENT SYSTEM")
print("="*50)
students = []
#-----------------------------------------------adding the students details in the record-----------------------------------

def add_student():
        name = input("Enter the name of the student: ")
        roll_number = input("Enter the roll number of the student: ").upper()
        branch = input("Enter the branch of the student: ").upper()
        alloted_branch = ["ECE", "CSE", "ME", "EE", "CE"]
        if branch not in alloted_branch:
            print("Invalid Branch")
            print("Branch should be ECE, CSE, ME, EE, CE")
            return
        marks = int(input("Enter the marks of the student: "))
        if marks < 0 or marks > 100:
            print("Marks must be between 0 and 100.")
            return    
        student = {
                "name" : name,
                "roll_number" : roll_number,
                "branch" : branch,
                "marks" : marks
                }
        for record in students:
            if record["roll_number"] == roll_number:
                print("Student Record already Exists.")
                return
        students.append(student)
        print("Student Details Added Successfully")    
#-------------------------------------------------viewing the list of students-----------------------------------------------        
def view_student():
        if len(students)==0:
            print("No students records found.")
            return  
        else:
            print("="*50)
            print("         STUDENT DETAILS")
            print("="*50)
            for student in students:
                print(f"Name : {student['name']}")
                print(f"Roll number : {student['roll_number']}")
                print(f"Branch : {student['branch']}")
                print(f"Marks : {student['marks']}")
                print("-"*50)
#------------------------------------------------searching the student in the record-----------------------------------------
def search_student():
        if len(students)==0:
            print("No Records Found")
            return
        num =input("Enter the Roll number: ").upper()
        found = False
        for student in students:
            if student["roll_number"] == num:
                found = True
                print("-"*50)
                print("STUDENT FOUND")
                print(f"Name : {student['name']}")
                print(f"Roll number : {student['roll_number']}")
                print(f"Branch : {student['branch']}")
                print(f"Marks : {student['marks']}")
                break
        if not found:
                print("No student found in the record.")    
#---------------------------------------------------updating the record of the student----------------------------------------------
def update_student():
        roll = input("Enter the Roll number of the student: ").upper()
        found = False
        for student in students:
            if student["roll_number"] == roll:
                found = True
                print("STUDENT FOUND!")
                print(f"Name : {student['name']}")
                print(f"Roll number : {student['roll_number']}")
                print(f"Branch : {student['branch']}")
                print(f"Marks : {student['marks']}")
                print("-"*50)
                print("Which field you want to update: ")
                print("1. Name")
                print("2. Branch")
                print("3. Marks")
                print("4. Cancel")
                option = int(input("Enter Your Choice: "))
                if option == 1:
                    student['name'] = input("Enter the updated name: ")
                    print("Student Information Updated Successfully.")
                    break
                elif option == 2:
                    new_branch = input("Enter the updated branch: ").upper()
                    if new_branch not in  ["ECE", "CSE", "ME", "EE", "CE"]:
                        print("Invalid Branch")
                    else:
                        student["branch"]= new_branch    
                        print("Student Information Updated Successfully.")  
                        break
                elif option == 3:
                    new_marks = int(input("Enter the updated Marks: "))
                    if new_marks <0 or new_marks >100:
                        print("Invalid Marks")
                    else:
                        student['marks']= new_marks    
                        print("Student Information Updated Successfully.")
                        break
                elif option == 4:
                    return   
                else:
                    print("Invalid Choice")
        if not found:
            print("No student found.")
# --------------------------------------------deleting the record of the student---------------------------            
def delete_student():
        if len(students)==0:
            print("No Records Found")
            return
        roll = input("Enter the Roll Number of the student: ").upper()
        found = False
        for student in students:
            if student['roll_number'] == roll:
                found = True
                print("STUDENT FOUND!")
                print(f"Name : {student['name']}")
                print(f"Roll number : {student['roll_number']}")
                print(f"Branch : {student['branch']}")
                print(f"Marks : {student['marks']}")
                print("-"*50)
                print("Which field you want to choose? ")
                print("1. Delete")
                print("2. Cancel")
                option = int(input("Enter Your Choice: "))
                if option == 1:
                    students.remove(student)
                    print("Student Information Deleted Successfully")
                    break
                elif option == 2:
                    return
                else:
                    print("Invalid Choice")
        if not found:
            print("No student found.")

while True:
    print("-"*50)
    print("1. Add Student")
    print("2. View Student")
    print("3. Search Student")
    print("4. Update Student")
    print("5. Delete Student")
    print("6. Exit")
    try:
        choice = int(input("Enter your choice: "))
        print("-"*50)
        if choice == 1:
            print("Add Student Selected")
            add_student()
        elif choice == 2:
            print("View Student Selected")
            view_student()
        elif choice == 3:
            print("Search Student Selected")
            search_student()
        elif choice == 4:
            print("Update Student Selected")
            update_student()
        elif choice == 5:
            print("Delete Student Selected")
            delete_student()
        elif choice == 6:
            print("Exiting the program....")
            break
        else:
            print("Please enter a number between 1 and 6.")
    except ValueError:
        print("Invalid Choice")
        continue
#------------------------------------------------------------------------------------------------------------------------------------------------------



















































































































































































































