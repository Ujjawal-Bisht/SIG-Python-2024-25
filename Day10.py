# sql - mysql, sqllite
# nosql- mongodb

import mysql.connector

obj = mysql.connector.connect(host="localhost", user="root", password="Dragoon")
# print(obj.is_connected())
'''
query1 = "Show Databases" 
cursor = obj.cursor()

cursor.execute(query1)
# records = cursor.fetchall()
# for i in records:
#     print(i[0])
# print(records)
rec = cursor.fetchone()# 1
# print(rec)
records = cursor.fetchall()# 8
print(cursor.rowcount)# 9
# print(records)
# fetchone(), fetchmany(), fetchall()

cursor.execute("use college")
cursor.execute("select * from student_info")
tables = cursor.fetchall()
print(tables)

old_name = 'abc'
new_name = 'abcd'
query2 = f"Update student_info set  fullname  = '{new_name}' where  fullname  = '{old_name}'"
cursor.execute(query2)
obj.commit()
cursor.execute("select * from student_info")
data = cursor.fetchall()
print(data)
'''

query1 = "Show Databases" 
cursor = obj.cursor()

cursor.execute(query1)
records = cursor.fetchall()
print(records)
cursor.execute("use world")
cursor.execute('show tables')
tables = cursor.fetchall()
print(tables)
cursor.execute("Desc country")
data = cursor.fetchall()
for i in data :
    print(i[0])

# cursor.execute("select * from country")
# data = cursor.fetchall()
# for i in data :
#     print(i)