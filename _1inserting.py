import mysql.connector as sqltor

def insert():

    f=open("pass.txt","r")
    pas=f.read()
    f.close()

    mycon=sqltor.connect(host="localhost",user="root",passwd=pas,database="library_manage")
    cursor=mycon.cursor()
    y="y"
    while y=="y":
        s="n"
        while s=="n":
            bname=input("Enter The Book Name ::>> ")
            bid=input("Enter The book Id ::>> ")
            print("Enter The Location")
            s=input("  Enter The Shelfe Number ::>> ")
            r=input("  Enter The Row Number ::>> ")
            c=input("  Enter The Column Number ::>> ")
            locat=str("S.no-"+s+"  R-"+r+"  C-"+c)
            a=(bname,bid,s,r,c)
            for i in a:
                if len(i)==0:
                    s="n"
                    print("SOME INFO IS MISSING PLEASE CHECK")
                    break
            else:   
                s=input("is the give data correct(y/n) ::>> ")
        try:   
            data="insert into book (Bname,Bid,location_S_R_C) value('"+bname.upper()+"','"+bid.upper()+"','"+locat.upper()+"');"
            cursor.execute(data)
        except:
            print("DATA ALREADY EXIST")
        mycon.commit()

        y=input("enter more data y/n ::>> ")

