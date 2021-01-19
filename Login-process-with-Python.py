#before you try the program you need to create an excel file
# and enter the path of the created excel file into the ''path'' variable
import xlrd
from xlutils.copy import copy

#enter the path of your created excel file in '''here''' (its going to be used as your local database)
#instead of '\' use '\\' in the path you want to enter
path='here'

#the main menu function
def mainMenu():
    command=input("""
    1> log in
    2> create account
    """)
    if command=="1":
        logIn()
    elif command =="2":
        createAccount()
    else:
        print("Wrong entry")
        mainMenu()

# if the user chooses to create an account
def createAccount():
    username=input("enter the ''New'' user name")
    #geting an username and checking if it already exists
    # if it already exists user can try another username or go back to main menu
    if userExCheck(username)!=0 :
        print("SORRY!! \n Username already exists")
        command=input("""
        1> try a new user name
        2> go to main menu""")
        if command=="1":
            createAccount()
        elif command=="2":
            mainMenu()
        else:
            print("wrong entry \n heading back to main menu")
            mainMenu()
    #if the entered username doesnt exist we ask for password
    else:
        newpassword=input("enter the password please.... : ")
        #opening our excl db and dedicating the entered pasword to the entered username in excl db
        file = xlrd.open_workbook(path)
        filesheet = file.sheet_by_index(0)
        row = filesheet.nrows

        wb = copy(file)
        w_sheet = wb.get_sheet(0)


        w_sheet.write(row, 1, username)

        w_sheet.write(row, 2, newpassword)
        wb.save(path)
        print("account created!! successfully heading to main menu...")
        mainMenu()


#the function which checks if the username already exists
def userExCheck(username):
    file = xlrd.open_workbook(path)
    filesheet = file.sheet_by_index(0)
    row = 0
    for l in range(1, filesheet.nrows):

        if username == str(filesheet.cell_value(l, 1)):
            row = l
            return row
            break

    return row

#checking if the entered password matches the username which we are checking
def passCheck(password,row):
    file = xlrd.open_workbook(path)
    filesheet = file.sheet_by_index(0)
    if password == str(filesheet.cell_value(row, 2)):
        passIsRight=True
        return passIsRight


#when the user chooses to log in
def logIn():

    username=input("enter your Username")
    #checking the existance of untered username
    if(userExCheck(username)==0):
        print("username does not exist!!\n\n")
        mainMenu()
    #if the username exists we ask for the password
    else:
        row=userExCheck(username)
        loginpassword=input("enter yout Password")
    if (passCheck(loginpassword,row)==True):
        print("LOGG IN SUCCESSFULLY ACOMPLISHED")
        print("hi dude welcome to our site\n\n")
    #if the password is wrong we give the user 2 more chances to enter the correct password
    else:
        for i in range(2,4):

            print(f"attempt {i}th from 3")
            loginpassword =input("enter the password")
            passCheck(loginpassword,row)
            if (passCheck(loginpassword, row) == True):
                print("LOG IN SUCCESSFULLY ACOMPLISHED")
                print("hi dude welcome to our site\n\n")
                exit()

        print("Account susspended!!! \n(too many tries)")
        mainMenu()


mainMenu()
