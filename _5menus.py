import _00intro00_ , _1inserting , _2reading , _3issued , _4returned , _5menusI , _6thank

def space():
    a=("""
""")
    print(a*60)
def menu():
    ch=0
    while (ch!=6):
        _5menusI.menu()
        ch=int(input("ENTER YOUR CHOICE(1/6) ::>> "))
        if ch==1:
            space()
            _1inserting.insert()   #importing 
        elif ch==2:
            space()
            _2reading.read()
        elif ch==3:
            space()
            _3issued.issue()   #importing 
        elif ch==4:
            space()
            _4returned.retur()   #importing
        elif ch==5:
            _00intro00_.intro()
        elif ch!=6:
            print("WRONG CHOICE !!! ENTER YOUR CHOICE BETWEEN 1 TO 5 ONLY ::>>")
        else:
           _6thank.thank()
    a=input("press enter to exit..")
