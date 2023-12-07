import random
import mysql.connector as sqlcon

#===================================================================#

con = sqlcon.connect(user = 'root', password = '6389', host = 'localhost')
cur = con.cursor()
q_show_databases = 'show databases'
cur.execute(q_show_databases)
databases = cur.fetchall()

q_create_database = 'create database idcards'
d = ('idcards',)

if d in databases:
    pass
else:
    cur.execute(q_create_database)

q_use_database = 'use idcards'
cur.execute(q_use_database)

q_show_tables = 'show tables'
cur.execute(q_show_tables)
tables = cur.fetchall()

q_create_table = 'create table student_data (roll_no int(5) primary key, name varchar(40), class int(2), gender varchar(6), dob date)'

t = ('student_data',)
if t in tables:
    pass
else:
    cur.execute(q_create_table)

#Adding records to our student_data table in idcards database



inputs = int(input("Enter number of records to input: "))
if inputs == 0:
     pass
else:
    for i in range(1,inputs):
        if i == 1:
            var = 'st'
        elif i == 2:
            var = 'nd'
        elif i == 3:
            var = 'rd'
        else:
            var = 'th'

        print("Enter data for ",i,var,' record:')
        name = input("Enter name: ")
        Class = int(input("Enter class: "))
        gender = input("Enter gender(M/F)")
        dob = input("Enter DOB:")
        roll_no = random.randint(100000,999999)


        if gender == "M":
                gender = "Male"
        elif gender == "F":
                gender = "Female"
        else:
            print("Enter a valid gender(M/F)")

        q_adding_records = ("insert into student_data values (%s, %s, %s, %s, %s)",(roll_no, name, Class, gender, dob))
        cur.execute(*q_adding_records)
con.commit()
print(inputs,' records successfully added to database - idcards')




#-----------------------------------------------------------------------------------------------------------------------------------#
#taking out data

q_taking_data = 'select * from student_data'
cur.execute(q_taking_data)
data = cur.fetchall()
print(data)

#----------------------------------------------------------------------------------------------------------------#
#Image manipulation for creating barcode

from PIL import Image, ImageDraw, ImageFont
from barcode import EAN13_GUARD
from barcode.writer import ImageWriter

inst = input("Enter name of institution: ")
fnt_name = ImageFont.truetype(r"D:\ID card generator\ID-card-generator-csproject\sample\sample11\Elianto-Regular.ttf", 65)
fnt_inst = ImageFont.truetype(r"D:\ID card generator\ID-card-generator-csproject\sample\sample11\Elianto-Regular.ttf", 45)
fnt_rest = ImageFont.truetype(r"D:\ID card generator\ID-card-generator-csproject\sample\sample11\PTS55F.ttf",30)

