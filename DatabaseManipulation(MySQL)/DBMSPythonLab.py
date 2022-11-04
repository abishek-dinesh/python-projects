from asyncio.windows_events import NULL
import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="root",
  database="UserReg"
)

tableName = 'Students'
cursor = mydb.cursor()

def insertStudent():
    sid = int(input("Enter the Student's ID : "))
    name = input("Enter the Student's Name : ")
    dept = input("Enter the Department : ")
    num = input("Enter the Mobile Number : ")
    dob = input("Enter Student's DOB - (YYYY-MM-DD) : ")
    doj = input("Enter Student's DOJ - (YYYY-MM-DD) : ")
    cursor.execute(f"insert into {tableName} (SID, name, department, mobile_no, DOB, DOJ) values ({sid}, '{name}', '{dept}', '{num}', DATE('{dob}'), DATE('{doj}'))")
    mydb.commit()
    print("Record Successfully Inserted!")
    print()

def modifyStudent():
    sid = int(input("Enter the Student's ID"))
    column = input("Type attribute you want to modify - (SID, name, department, mobile_no, DOB, DOJ)")
    value = input('Enter the value you want to set it to : ')

    if column == 'SID':
        value = int(value)
    else:
        value = f"'{value}'"
    
    cursor.execute(f"update {tableName} set {column} = {value} where SID = {sid}")
    mydb.commit()
    print("Record Successfully Updated!")
    print()

def deleteStudent():
    sid = int(input("Enter the Student's ID"))
    cursor.execute(f"delete from {tableName} where SID = {sid}")
    mydb.commit()
    print("Record Successfully Deleted!")
    print()

def showStudents():
    cursor.execute("select * from students")
    print("(SID, name, department, mobile_no, DOB, DOJ)")
    records = cursor.fetchall()
    for record in records:
        print(record)
    print()

while(1):
    print("\t\tMAIN MENU")
    print("1. Register a Student")
    print("2. Modify a Student Record")
    print("3. Delete a Student Record")
    print("4. Show all students")
    print("Choose an option... ")
    ch = int(input())
    print()

    if ch == 1:
        insertStudent()
    elif ch == 2:
        modifyStudent()
    elif ch == 3:
        deleteStudent()
    elif ch == 4:
        showStudents()
    else:
        break



