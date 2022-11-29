import mysql.connector as sqltor
import _0clibrary , _0createtab    #created library
import _5menus

_0clibrary.clib()    #importing the clib

c="n"
while c!="c":
    try:
        pas=input("ENTER YOUR MYSQL PASSWORD ::>>  ")
        mycon=sqltor.connect(host="localhost",user="root",passwd=pas,database="library_manage")
        print("trying to connect...")
        c="c"
    except:
        print("wrong paassword")
cursor=mycon.cursor()
print("connection succesfull")        


f=open("pass.txt","w")
f.write(pas)
f.close() 



_0createtab.cr()      #importing the cr
_5menus.menu()


mycon.close()

