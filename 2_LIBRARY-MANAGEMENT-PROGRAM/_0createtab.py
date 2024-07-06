import mysql.connector as sqltor
f=open("ser.txt","a")
f.close()
def cr():
    f=open("pass.txt","r")
    pas=f.read()
    f.close()
    f=open("ser.txt","r+")
    r=f.read()
    if r=="":
        f.write("1")
        c="n"
        while c!="c":
            try:
                mycon=sqltor.connect(host="localhost",user="root",passwd=pas,database="library_manage")
                print("trying to create tables...")
                c="c"
            except:
                print("wrong paassword")        
        cursor=mycon.cursor()
        book="create table if not exists book (Bname varchar(40),Bid varchar(10) primary key,location_S_R_C varchar(20));"
        issu="create table if not exists issued_book (student_name varchar(30),student_adm_no varchar(10) primary key,book_name varchar(40),book_id varchar(10) unique,date_time datetime);"
        retu="create table if not exists returned (sname varchar(40),sadm varchar(10) ,bname varchar(40),bid varchar(10),date_time datetime);"
        cursor.execute(book)
        cursor.execute(issu)
        cursor.execute(retu)
        print("succesfull created")
    else:
        f.write("1")
    f.close()

