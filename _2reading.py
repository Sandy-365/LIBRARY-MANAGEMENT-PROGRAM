import mysql.connector as sqltor
import _2readingmenu

def space():
    a=("""
""")
    print(a*60)
    
def read():
    f=open("pass.txt","r")
    pas=f.read()
    f.close()

    mycon=sqltor.connect(host="localhost",user="root",passwd=pas,database="library_manage")
    cursor=mycon.cursor()
    rbook=" select * from book;"
    ribook="select * from issued_book"
    rrbook="select * from returned"

    ch=0
    while (ch!=4):
        _2readingmenu.rmenu()
        ch=int(input("ENTER YOUR CHOICE(1/4) ::>> "))
        if ch==1:
            space()
            cursor.execute(rbook)
            rb=cursor.fetchall()
            p=0
            for i in rb:
                print("Book name:",i[0],"\t\t\t\t       Book Id:",i[1],"\t\t\t\t        Location:",i[2])
                p+=1
            if p == 0:
                print("NO BOOK PRESENT")
            a=input("press enter to continue....")
            mycon.commit()
        
        elif ch==2:
            space()
            cursor.execute(ribook)
            rib=cursor.fetchall()
            p=0
            for i in rib:
                print(i)
                p+=1
            if p == 0 :
                print("NO ISSUED BOOK")
            a=input("press enter to continue....")
            mycon.commit()
        elif ch==3:
            space()
            cursor.execute(rrbook)
            rrb=cursor.fetchall()
            p=0
            for i in rrb:
                print(i)
                p+=1
            if p==0:
                print("NO DATA PRESENT")
            a=input("press enter to continue....")
            mycon.commit()
        elif ch!=4:
            print("WRONG CHOICE !!! ENTER BETWEEN (1 TO 4) ONLY ::>>")
        else:
           print("THANK YOU")

