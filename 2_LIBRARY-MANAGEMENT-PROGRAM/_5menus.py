import _00intro00_ , _1inserting , _2reading , _3issued , _4returned , _5menusI , _6thank
import os

def menu():
    ch=0
    while (ch!=6):
        os.system('cls')
        _5menusI.menu()
        ch=int(input("ENTER YOUR CHOICE(1/6) ::>> "))
        os.system('cls')
        if ch==1:
            _1inserting.insert()   #importing 
        elif ch==2:
            _2reading.read()
        elif ch==3:
            _3issued.issue()   #importing 
        elif ch==4:
            _4returned.retur()   #importing
        elif ch==5:
            _00intro00_.intro()
        elif ch!=6:
            print("WRONG CHOICE !!! ENTER YOUR CHOICE BETWEEN 1 TO 5 ONLY ::>>")
        else:
           _6thank.thank()
    a=input("press enter to exit..")
