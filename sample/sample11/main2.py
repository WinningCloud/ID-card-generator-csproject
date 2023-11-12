import mysql.connector as mysqlcon
con = mysqlcon.connect(user = "root", password = "6389", host = "localhost")
cur = con.cursor()
q1 = "show databases"
cur.execute(q1)
data = cur.fetchall()

q2 = "create database IDcards_data"
d = ("idcards_data",)
if d in data:
    pass
else:
    cur.execute(q2)
print(data)

q3 = "show tables"
q4 = "create table stud_data (roll_no int(5) primary key, name varchar(40), class gender varchar(6), dob date)"
data2 = cur.fetchall()
t = ("stud_data",)
if t in data2:
    pass
else:
    cur.execute(q4)
    