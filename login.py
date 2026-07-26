print('='*100)
print("*"*100)
print("                                  STUDENT MANAGEMENT SYSTEM")
print("*"*100)
#--------------------------------------------------Register new user---------------------------------------------
def register():
    while True:
        Create_Username = input("Enter Username for Register: ")
        Create_Password = input("Enter the Password: ")
        Confirm_Password = input("Re-enter the Password for Confirmation:  ")
        if Create_Password == Confirm_Password:
            with open("users.txt", "a") as file:
                file.write(Create_Username + "," + Create_Password + "\n")
            print("Account Created Successfully!")
            return
        else:
            print("Password doesn't match.")
            print("-"*100)
#--------------------------------------------------login function------------------------------------------------
def login(): 
    import main 
    while True:
        found = False
        entered_username = input("Enter Username: ")
        entered_password = input("Enter Password: ")
        with open("users.txt", "r") as file:
            for line in file:
                line = line.strip()
                data = line.split(",")    
                if data[0] == entered_username and data[1] == entered_password:
                    found = True
                    break 
            if found: 
                print("Login Successfully")
                main.main_menu()
                return    
            if not found:
                print("Invalid Username and Password. Please try again.")          
#--------------------------------------------------Exit User-----------------------------------------------------
def exit():
    print("------------------------------------EXIT-------------------------------------")
    print("  Thank You!  ")
while True:
    print("1. Register")
    print("2. Login")
    print("3. Exit")
    print('='*100)
    print("Choose your options")
    
    try:
        choice = int(input("Enter Your Choice: "))
        if choice == 1:
            register()
        elif choice == 2:
            login()    
        elif choice == 3:
            exit()
            break
        else:
            print("Please enter a number between 1 and 3.")
            print("-"*100)
    except ValueError:
        print("Invalid Choice")
        print("-"*100)
        continue










































