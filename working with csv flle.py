# Working with csv
import csv
# User Registration with csv
#password = "go"

def RegisterUser():
    with open("Users.csv",mode = "a",newline= "") as file:
        writer = csv.writer(file, delimiter = ",")
        print("Enter your Info to register: ")
        Email = input("Email: ")
        password = input("Enter your password: ")
        password2 = input("pls confirm password: ")
        if password == password2:
            writer.writerow([Email,password])
            print("Your Registration is Successful")
        else:
            print("Something went wrong,pls try again")

#User Login function
def UserLogin():
    print("To login,pls enter your info")
    Email = input("Email: ")
    password = input("Enter password: ")
    with open("Users.csv","r") as file:
        reader = csv.reader(file, delimiter = ",")
        for row in reader:
            if row == [Email,password]:
                print("Your login is successful")
                return True
            
    print("No such email exit")
    return False

#def ChangePassword():
   

active = True
logged_in = False
# Main loop
while active:
    if logged_in:
        print("1.Logout\n2. change password\n3. Quit")
    else:
        print("1.Login\n2. Register\n3. Quit")

    choice = input("What will you like to do: ").lower()
    if choice == "register" and logged_in == False:
        RegisterUser()
    elif choice == "login" and logged_in == False:
        logged_in = UserLogin()
    #elif choice == "change password" and logged_in ==True:
     #  ChangePassword()
    elif choice == "quit":
        active = False
        print("Thanks For Your Time With Us")
    elif choice == "logout" and logged_in == True:
        logged_in = False
        print("Logout Successful.")
    else:
        print("Sorry,pls try again.")
        
        
                      
    
