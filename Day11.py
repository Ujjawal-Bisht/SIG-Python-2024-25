import mysql.connector

def view(tableName):
    cursor.execute(f"select* from {tableName}")
    data = cursor.fetchall()
    if not data:
        print("No data found")
        return
    else:
        for i in data:
            print(i)

def insert(tableName):
    try:
        id = int(input("Enter id: "))
        name = input("Enter name: ")
        mobile = int(input("Enter mobile: "))
        age = int(input("Enter age: "))
        cursor.execute("Insert into %s values(%s, '%s', %s, %s)" % (tableName, id, name, mobile, age))
        db.commit()
        print("Data inserted")
    except:
        print("Error")
        
def search(tableName):
    # dataReq = int(input("Enter id: "))
    nameSearch = input("Enter name: ") # y

    query = f'select* from {tableName} where name like "%{nameSearch}%" '
    query2 = f"Select* from {tableName} where name like '_____' "
    #query3 = f"Select* from {tableName} where id = {dataReq} "
    cursor.execute(query)
    data = cursor.fetchall()
    if not data:
        print("No data found")
        return
    else:
        for i in data:
            print(i)


try:
    db = mysql.connector.connect(host = "localhost", user = "root", password="Dragoon")
    cursor = db.cursor()
    # cursor.execute("show databases")
    cursor.execute("use student")
    view('student_info')
    #insert('student_info')
    #view('student_info')
    search('student_info')
except:
    print("Error")
    db.close()

