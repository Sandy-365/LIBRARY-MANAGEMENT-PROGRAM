import mysql.connector as sqltor

def retur():
    f=open("pass.txt","r")
    pas=f.read()
    f.close()

    mycon=sqltor.connect(host="localhost",user="root",passwd=pas,database="library_manage")
    cursor=mycon.cursor()
    s="n"
    while s=="n":
        sadm=input("ENTER STUDENT ADMISSION NUMBER ::>> ")
        bid=input("ENTER BOOK ID ::>> ")
        d="select now();"
        cursor.execute(d)
        da=cursor.fetchone()
        for i in da:
            dat=str(i)
        print("DATE & TIME IS (",dat,")")
        date=dat
        s=input("is the give data correct(y/n) ::>>")
    s="select * from issued_book where book_id = '"+bid.upper()+"' and student_adm_no = '"+sadm.upper()+"';"
    cursor.execute(s)
    rec=cursor.fetchall()
    if rec == []:
        print("please check the provided information")
    for i in rec:
        r="insert into returned values('"+i[0]+"','"+i[1]+"','"+i[2]+"','"+i[3]+"','"+date+"');"
        cursor.execute(r)
        d="delete from issued_book where book_id = '"+bid.upper()+"';"
        cursor.execute(d)
        print(i[0],"(",i[1],")"," successfully returned ",i[2],"(",i[3],")")
    mycon.commit()
    a=input("press any key to continue...")
