#           A project by
#        AAKASH DEEP KUMAR
#         of class 12th on
#topic of student managment using mysql 


import mysql.connector
mydb = mysql.connector.connect(host ="localhost",user ="root",passwd ="lata")
mycur = mydb.cursor()
mycur.execute("create database if not exists student_db1")
mycur.execute("use student_db1")
abc="Y"
print(" ================================= \n ================================= \n ======= AAKASH DEEP 12th ======== \n ================================= \n ================================= \n \n")
def while_fn ():
    while abc=="Y" or abc=="y":
        if menu==1 :
            userinput()
        elif menu==2 :
            search_fn()
            menu_fn()
    while abc=="N" or abc=="n":
        if menu==1 and abc=="N" or abc=="n" : 
            userinput()
        elif menu==2 :
            search_fn()
            menu_fn
def userinput ():
    roll=str(input("enter roll no. of the student : "))
    name=str(input("enter name of the student : "))
    dob=str(input("enter  year of birth of the student : "))
    att=str(input("enter attendence of the student P/A : "))
    creat_tb = "create table if not exists student_tb ( sroll varchar(30) primary key, sname varchar(30), sdob varchar(30), satt varchar(30))"
    mycur.execute(creat_tb)
    colum_tb = "insert into student_tb (sroll, sname, sdob, satt) values ('"+roll+"','"+name+"','"+dob+"','"+att+"')"
    mycur.execute(colum_tb)
    mydb.commit()
    mycur.execute("select * from student_tb")
    result = mycur.fetchall()
    print("|| roll || name || birth y || attendence || ")
    for x in result:
        print(x)
    global abc
    abc = input("do you want to continue adding student ? [y/n] : ")

def search_fn ():
    menu2=int(input(" ================================= \n [1] search by rollno. \n [2] search by name \n [3] search by birth year \n [4] search present student \n [5] search absebt student \n [6] main menu \n =================================\n:"))
    if menu2==1 :
        print("==================== \n [1] search by rollno. \n====================")
        search=str(input("Enter roll no. of student :"))
        mycur.execute("select * from student_tb where sroll='"+search+"'")
        result = mycur.fetchall()
        print("|| roll || name || birth y || attendence ||\n=====================================\n")
        for x in result:
            print(x)
    elif menu2==2 :
        print("==================== \n [2] search by name \n====================")
        search=str(input("Enter name of student :"))
        mycur.execute("select * from student_tb where sname='"+search+"'")
        result = mycur.fetchall()
        print("\n|| roll || name || birth y || attendence ||\n=====================================\n")
        for x in result:
            print(x)
    elif menu2==3 :
        print("==================== \n [3] search by birth year \n====================")
        search=str(input("Enter birth year of student :"))
        mycur.execute("select * from student_tb where sdob='"+search+"'")
        result = mycur.fetchall()
        print("|| roll || name || birth y || attendence ||\n=====================================\n")
        for x in result:
            print(x)
    elif menu2==4 :
        print("==================== \n [4] search present student \n====================")
        mycur.execute("select * from student_tb where satt='P'")
        result = mycur.fetchall()
        print("\n|| roll || name || birth y || attendence ||\n=====================================\n")
        for x in result:
            print(x)
    elif menu2==5 :
        print("==================== \n [5] search absent student \n====================")
        mycur.execute("select * from student_tb where satt='A'")
        result = mycur.fetchall()
        print("\n|| roll || name || birth y || attendence ||\n=====================================\n")
        for x in result:
            print(x)
    elif menu2==6 :
        menu_fn ()
        
def menu_fn () :
    global menu
    menu=int(input("====================================\n press [1] for entery of new student \n press [2] for searching student \n====================================\n   :"))
    while_fn()
    print(abc)

menu_fn ()

while_fn
    
    
