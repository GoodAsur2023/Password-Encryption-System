'''Functions used:
    exit_func
    login
    register




'''

def exit_func():
    print('Thank you for paying a visit to us! Have a fulfilling day! :)')
    wait = input('\n\n\n Press any key to exit...') 
    
def login():


def register():


def menu2():
    print("      MENU       ")
    entry=input("1. Access your Pass - A \n2. Generate Pass - G \n3. Encrypt Pass \n4. Decrypt Pass")
    


#DISPLAY MENU1 - Login, Register, Exit
def startmenu1():
    print("    Welcome to the Neo Culture Library    ")
    entry = input(" 1. Login - L \n2. Register - R \n3. Exit - E \n\n ^_^ --- ")

    if entry == 'L':
        login()
        

    elif entry == 'R':
        register()
        menu2()

    elif entry == 'E':
        exit_func()
                      
    
startmenu1() 


def login():
