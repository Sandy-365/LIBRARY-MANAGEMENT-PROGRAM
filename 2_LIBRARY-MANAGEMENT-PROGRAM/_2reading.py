import mysql.connector as sqltor
import _2readingmenu
import os


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
        os.system('cls') 
        _2readingmenu.rmenu()
        ch=int(input("ENTER YOUR CHOICE(1/4) ::>> "))
        os.system('cls') 
        if ch==1: 
            cursor.execute(rbook)
            rb=cursor.fetchall()
            p=0
            print("                                                 LIST OF BOOKS PRESENT")
            for i in rb:
                print("※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※")
                print("Book name:",i[0],"\t\t\t\t       Book Id:",i[1],"\t\t\t\t        Location:",i[2])
                p+=1
            if p == 0:
                print("NO BOOK PRESENT")
            if(p):
                print("※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※")
            a=input("press enter to continue....")
            mycon.commit()

        elif ch==2:
            cursor.execute(ribook)
            rib=cursor.fetchall()
            p=0
            print("                                                 LIST OF ISSUED BOOK")
            for i in rib:
                print("※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※")
                print("STUDENT NAME : '"+i[0]+"'\t\tREG NO : '"+i[1]+"'\t\tBOOK NAME : '"+i[2]+"'\t\tBOOK ID : '"+i[3]+"'\t\tDATE-TIME : "+str(i[4]))
                p+=1
            if p == 0 :
                print("NO ISSUED BOOK")
            if(p):
                print("※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※")
            a=input("press enter to continue....")
            mycon.commit()

        elif ch==3: 
            cursor.execute(rrbook)
            rrb=cursor.fetchall()
            p=0
            print("                                                   LIST OF RETURNED BOOK")
            for i in rrb:
                print("※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※")
                print("STUDENT NAME : '"+i[0]+"'\t\tREG NO : '"+i[1]+"'\t\tBOOK NAME : '"+i[2]+"'\t\tBOOK ID : '"+i[3]+"'\t\tDATE-TIME : "+str(i[4]))
            if p==0:
                print("NO DATA PRESENT")
            if(p):
                print("※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※")
            a=input("press enter to continue....")
            mycon.commit()

        elif ch!=4:
            print("WRONG CHOICE !!! ENTER BETWEEN (1 TO 4) ONLY ::>>")

        else:
           print("THANK YOU")

