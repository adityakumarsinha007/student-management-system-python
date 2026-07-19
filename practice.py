'''students = []
name = input("Enter the name of the student: ")
roll_number = input("Enter the roll number of the student: ")
branch = input("Enter the branch of the student: ")
marks = int(input("Enter the marks of the student: "))
student1 = {
    "name" : name,
    "roll_number" : roll_number,
    "branch" : branch,
    "marks" : marks
}
name = input("Enter the name of the student: ")
roll_number = input("Enter the roll number of the student: ")
branch = input("Enter the branch of the student: ")
marks = int(input("Enter the marks of the student: "))
student2 = {
    "name" : name,
    "roll_number" : roll_number,
    "branch" : branch,
    "marks" : marks
}
students.append(student1)
students.append(student2)
print(students)
for student in students:
    print("-"*50)
    print(f"Name : {student["name"]}")
    print(f"Roll number : {student["roll_number"]}")
    print(f"Branch : {student["branch"]}")
    print(f"Marks : {student["marks"]}")   
    print("-"*50)
'''
name = input("Enter the name: ")
branch = input("Enter the branch: ")
marks = input("Enter the marks: ")
'''def greet(name):
    print(f"Hello {name}")
def college():
    print("GEC West Champaran")
def branch():
    print("ECE") 
def student_name(name):
    print(f"Student Name: {name}")       
greet(name)
student_name(name)
'''
def student_details(name,branch,marks):
    print(f"Student Name: {name}")
    print(f"Student branch: {branch}")
    print(f"Student marks: {marks}")
student_details(name,branch,marks)





