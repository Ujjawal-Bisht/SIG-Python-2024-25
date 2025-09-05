import mysql.connector as connect

mydb = connect.connect(host="localhost", user="root", password="Dragoon")

# print(mydb.is_connected())

# print(mydb)

cur = mydb.cursor()
# cur.execute("SHOW databases;")

# data = cur.fetchall()
# print(data)

# for i in data:
#     print(i)

# newData = cur.fetchall()
# print(newData)

# data = cur.fetchone()
# print(data)

# # data2 = cur.fetchone()
# # print(data2)

# data2 = cur.fetchmany(4)
# print(data2)

# data2 = cur.fetchall()
# print(data2)

# # data3 = cur.fetchmany(3)
# # print(data3)

# # data2 = cur.fetchmany()
# # print(data2)

# # data2 = cur.fetchmany()
# # print(data2)

# # data2 = cur.fetchone()
# # print(data2)

# # data2 = cur.fetchone()
# # print(data2)

# data = cur.fetchall()
# print(data)

# cur.execute("USE xyz;")

# cur.execute("SHOW tables;")
# data = cur.fetchone()
# print(data)

# print("Total records:- ",cur.rowcount)

# data = cur.fetchall()
# print(data)

# print("Total records:- ",cur.rowcount)

# cur.execute("SELECT * FROM empinfo;")
# data = cur.fetchall()
# print(data)
# name = input("Enter name:- ")
# sal = input("Enter salary:- ")
# cur.execute("SELECT * FROM empinfo where name = '%s' and salary > %s;"%(name,sal))
# data = cur.fetchall()
# print(data)


# cur.execute("SELECT * FROM empinfo where name = '{}' and salary > {};".format(name, sal))
# data = cur.fetchall()
# print(data)


query = "SELECt* from empinfo;"
# cur.execute(query)
# data = cur.fetchall()
# print(data)

query2 = "INSERT into empinfo(id, name, salary) values(4, 'UB', 50000);"
cur.execute(query2)
mydb.commit()
cur.execute(query)
data = cur.fetchall()
print(data)