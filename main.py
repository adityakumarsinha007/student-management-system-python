print("="*100)

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
        with open("students.txt", "r") as file:
                for line in file:
                    if not line.strip():
                        continue
                    data = line.strip().split(",")
                    if len(data) ==4 and data[1].strip().upper() == roll_number:
                        print("Student Record already Exists.")
                        return
        with open ("students.txt", "a") as file:
            file.write(name + "," + roll_number + "," + branch + "," + str(marks) + "\n")
        print("Student Details Added Successfully")    
#-------------------------------------------------viewing the list of students-----------------------------------------------        
def view_student():
        print("="*100)
        print("                              STUDENT DETAILS")
        print("="*100)
        found = False
        with open("students.txt", "r") as file:
            for line in file:
                data = line.strip().split(",")
                if len(data) == 4:
                    found = True
                    print(f"Name: {data[0]}")
                    print(f"Roll Number: {data[1]}")
                    print(f"Branch: {data[2]}")
                    print(f"Marks: {data[3]}")
                    print('-'*100)
            if not found:
                print("No Rcords Found")
#------------------------------------------------searching the student in the record-----------------------------------------
def search_student():
    num =input("Enter the Roll number: ").upper()
    found = False
    with open("students.txt", "r") as file:
            for line in file:
                data = line.strip().split(",")
                if data[1] == num:
                    found = True
                    print("-"*100)
                    print(" STUDENT FOUND ")
                    print(f"Name : {data[0]}")
                    print(f"Roll number : {data[1]}")
                    print(f"Branch : {data[2]}")
                    print(f"Marks : {data[3]}")
                    print("-"*100)
                    break
            if not found:
                print("No student found in the record.")    
#---------------------------------------------------updating the record of the student----------------------------------------------
def update_student():
        roll = input("Enter the Roll number of the student: ").upper()
        found = False
        with open("students.txt", "r") as file:
            lines = file.readlines()
            for i in range(len(lines)):
                data = lines[i].strip().split(",")
                if data[1] == roll:
                    found = True
                    print("  STUDENT FOUND!  ")
                    print(f"Name : {data[0]}")
                    print(f"Roll number : {data[1]}")
                    print(f"Branch : {data[2]}")
                    print(f"Marks : {data[3]}")
                    print("-"*100)
                    print("Which field you want to update: ")
                    print("1. Name")
                    print("2. Branch")
                    print("3. Marks")
                    print("4. Cancel")
                    option = int(input("Enter Your Choice: "))
                    if option == 1:
                        new_name = input("Enter the updated name: ")
                        data[0] = new_name
                        lines[i] = ",".join(data) + "\n"
                        print("Student Information Updated Successfully.")
                        break
                    elif option == 2:
                        new_branch = input("Enter the updated branch: ").upper()
                        if new_branch not in  ["ECE", "CSE", "ME", "EE", "CE"]:
                            print("Invalid Branch")
                        else:
                            data[2]= new_branch 
                            lines[i] = ",".join(data) + "\n"   
                            print("Student Information Updated Successfully.")  
                            break
                    elif option == 3:
                        new_marks = int(input("Enter the updated Marks: "))
                        if new_marks <0 or new_marks >100:
                            print("Invalid Marks")
                        else:
                            data[3]= str(new_marks)
                            lines[i] = ",".join(data) + "\n" 
                            print("Student Information Updated Successfully.")
                            break
                    elif option == 4:
                        return   
                    else:
                        print("Invalid Choice")
            if found:
                with open("students.txt","w") as file:
                    file.writelines(lines)    
        if not found:
            print("No student found.")
# --------------------------------------------deleting the record of the student---------------------------            
def delete_student():
        roll_number = input("Enter the Roll Number of the student: ").upper()
        found = False
        with open("students.txt", "r") as file:
            lines = file.readlines()
            for i in range(len(lines)):
                if not lines[i].strip():
                        continue
                data = lines[i].strip().split(",")
                if len(data) == 4 and data[1].strip().upper() == roll_number:
                    print("Which field you want to choose? ")
                    print("1. Delete")
                    print("2. Cancel")
                    option = int(input("Enter Your Choice: "))
                    found = True
                    print(f"Name : {data[0]}")
                    print(f"Roll number : {data[1]}")
                    print(f"Branch : {data[2]}")
                    print(f"Marks : {data[3]}")
                    print("-"*100)
                    if option == 1:
                        lines.pop(i)
                        print("Student Information Deleted Successfully")
                        break
                    elif option == 2:
                        return
                    else:
                        print("Invalid Choice")
                        return
            if found:
                with open("students.txt","w") as file:
                    file.writelines(lines)         
        if not found:
            print("No student found.")
#---------------------------------------------------------main menu--------------------------------------------------------------------
def main_menu():
    while True:
        print("-"*100)
        print("1. Add Student")
        print("2. View Student")
        print("3. Search Student")
        print("4. Update Student")
        print("5. Delete Student")
        print("6. Exit")
        try:
            choice = int(input("Enter your choice: "))
            print("-"*100)
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
                print("-"*100)
                break
            else:
                print("Please enter a number between 1 and 6.")
        except ValueError:
            print("Invalid Choice")
            continue
#------------------------------------------------------------------------------------------------------------------------------------------------------



















































































































































































































