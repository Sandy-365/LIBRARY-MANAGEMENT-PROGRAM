f=open("ser1.txt","a")
f.close()
def clib():
    a="""
"""
    import mysql.connector as sqltor
    f=open("ser1.txt","r+")
    r=f.read()
    if r=="":
        f.write("0")
        c="n"
        while c!="c":
            try:
                pas=input("ENTER YOUR MYSQL PASSWORD ::>>")
                mycon=sqltor.connect(host="localhost",user="root",passwd=pas)
                print("TRYING TO CREATE LIBRARY .......")
                c="c"
            except:
                print("WRONG PASSWORD")
                
        cursor=mycon.cursor()
        cursor.execute("create database if not exists library_manage")
        mycon.commit()
        print("SUCCESSFULLY CREATED")
    else:
        f.write("0")
    f.close()
