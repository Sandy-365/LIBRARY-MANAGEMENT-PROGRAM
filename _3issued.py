import mysql.connector as sqltor

def issue():
    f=open("pass.txt","r")
    pas=f.read()
    f.close()
    mycon=sqltor.connect(host="localhost",user="root",passwd=pas,database="library_manage")
    cursor=mycon.cursor()
    s="n"
    while s=="n":
        sname=input("enter the student name ::>> ")
        sadm=input("enter the student adm no. ::>> ")
        bname=input("enter the book name ::>> ")
        bid=input("enter the book id ::>> ")
        d="select now();"
        cursor.execute(d)
        da=cursor.fetchone()
        for i in da:
            dat=str(i)
        print(" DATE & TIME IS (",dat,")")
        date=dat
        a=(sname.upper(),sadm.upper(),bname.upper(),bid.upper(),date.upper())
        for i in a:
            if len(i)==0:
                s="n"
                print("SOME INFO IS MISSING PLEAASE CHECK")
                break
        else:   
            s=input("is the give data correct(y/n) ::>> ")
    che="select * from book where bid = '"+bid.upper()+"' ;"
    cursor.execute(che)
    rche=cursor.fetchall()
    c=0
    if rche == []:
        print("\n")
        print("\n")
        print(" !!!!!!!!!!!!  PLEASE ADD THIS BOOK TO OUR LIST OR CHECK THE PROVIDED INFORMATION !!!!!!!!!!!!!!")
        print("\n")
        print("          BOOK NOT ISSUED AS INFO PROVIDED IS WRONG OR THIS BOOK IS NOT IN OUR LIST")
        print("\n")
        c=+1
    if c==0:
        try:        
            issue="insert into issued_book values('"+sname.upper()+"','"+sadm.upper()+"','"+bname.upper()+"','"+bid.upper()+"','"+date.upper()+"');"
            cursor.execute(issue)
            print(bname.upper()+"("+bid.upper()+") "+"issued to "+sname.upper()+"("+sadm.upper()+")"," on ",dat," .")
        except:
            print("GIVEN DATA IS ALREDY THERE")

    b=input("press enter to exit")
    mycon.commit()



