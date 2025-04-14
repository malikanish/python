import MySQLdb as db

def createdb():
    con = db.connect(host="localhost", user="root", password="rootpassword")
    cur = con.cursor()
    a = "CREATE DATABASE student_management"
    cur.execute(a)
    cur.close()
    con.close()
    print("Database is createqd successfully")

def createtable():
    con = db.connect(host="localhost", user="root", password="rootpassword", database="student_management")
    cur = con.cursor()
    a = "CREATE TABLE students (id INT PRIMARY KEY, name VARCHAR(100), age INT NOT NULL, email VARCHAR(100))"
    cur.execute(a)
    cur.close()
    con.close()
    print("Table created successfully")
def insertrecord():
    con = db.connect(host="localhost", user="root", password="rootpassword", database="student_management")
    cur = con.cursor()
    
    a = "INSERT INTO students VALUES (1, 'anish', 23, 'anishbilal001@gmail.com')"
    cur.execute(a)
    
    a = "INSERT INTO students VALUES (2, 'usama', 26, 'usama001@gmail.com')"
    cur.execute(a)
    
    a = "INSERT INTO students VALUES (3, 'abdullah', 21, 'abdullah001@gmail.com')"
    cur.execute(a)
    
    con.commit()
    cur.close()
    con.close()
    print("Insertion of records completed")
def deleterecord():
    con = db.connect(host="localhost", user="root", password="rootpassword", database="student_management")
    cur = con.cursor()
    a="delete from students where id =3"
    cur.execute(a)
    con.commit()
    cur.close()
    con.close()
    print("delete records sucessfully")

def readrecord():
    con = db.connect(host="localhost", user="root", password="rootpassword", database="student_management")
    cur = con.cursor()
    a="select * from students"
    cur.execute(a)
    data=cur.fetchall()
    print(data)

def updaterecord():
    con = db.connect(host="localhost", user="root", password="rootpassword", database="student_management")
    cur = con.cursor()
    a="update students set name='usama' where id=1"
    cur.execute(a)

    a="update students set name='anish' where id=2"
    cur.execute(a)
    con.commit()
    cur.close()
    con.close()
    print("record updated")



while True:
    print("1 Create DATABASE")
    print("2 Create Table")
    print("3 Insert record") 
    print("4 delete record")
    print("5 update record")
    print("6 read record")
    print("7 Exit")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        createdb()
    elif choice == 2:
        createtable()
    elif choice ==3:
        insertrecord()
    elif choice ==4:
        deleterecord()
    elif choice==5:
        updaterecord()
    elif choice==6:
        readrecord()
    elif choice ==7:
        exit
        break
       
        
        
