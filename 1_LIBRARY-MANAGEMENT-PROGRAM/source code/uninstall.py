import mysql.connector as sqltor

import os

c="n"
a=input("do you realy wnt to delete libraary_management folder (y/n) ::>> ")
if a=="y":
    try:
        try:
            os.remove("pass.txt")
        except:
            pass
        try:    
            os.remove("ser.txt")
        except:
            pass
        try:
            os.remove("ser1.txt")
        except:
            pass
        try:
            os.remove("_00intro00_.py")
        except:
            pass
        try:
            os.remove("_0clibrary.py")
        except:
            pass
        try:
            os.remove("_1inserting.py")
        except:
            pass
        try:
            os.remove("_2reading.py")
        except:
            pass
        try:
            os.remove("_2readingmenu.py")
        except:
            pass
        try:
            os.remove("_3issued.py")
        except:
            pass
        try:
            os.remove("_4returned.py")
        except:
            pass
        try:
            os.remove("_5menus.py")
        except:
            pass
        try:
            os.remove("_6thanks.py")
        except:
            pass
        try:
            os.remove("smain.py")
        except:
            pass
        try:
            os.remove("uninstall.py")
        except:
            pass
        try:
            os.remove("_0createtab.py")
        except:
            pass
        try:
            os.remove("_5menusI.py")
        except:
            pass
        try:
            os.remove("_6thank.py")
        except:
            pass
        try:
            os.rmdir("source code")
        except:
            pass
        try:
            os.remove("smain.exe")
        except:
            pass
        try:
            os.remove("uninstall.exe")
        except:
            pass
    except:
        print("")

    while c!="c":
        try:
            pas=input("enter your mysql password ::>>")
            mycon=sqltor.connect(host="localhost",user="root",passwd=pas,database="mysql")
            print("trying to drop...")
            c="c"
        except:
            print("wrong paassword")
    print("succesfull")        
    cursor=mycon.cursor()
    try:
        cursor.execute("drop database if exists library_manage;")
        print("done")
    except:
        print("already deleted")

    b=input("press Enter to exit...")
else:
    print("every thing is safe")
    b=input("press any key to exit...")
mycon.commit()
