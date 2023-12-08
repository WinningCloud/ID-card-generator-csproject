import random
import mysql.connector as sqlcon
import os
PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))

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
    for i in range(inputs):
        if i == 1:
            var = 'st'
        elif i == 2:
            var = 'nd'
        elif i == 3:
            var = 'rd'
        else:
            var = 'th'

        print("Enter data for ",i+1,var,' record:')
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
# from barcode import EAN13_GUARD
# from barcode import ImageWriter



font_path = os.path.join(PROJECT_ROOT, 'Elianto-Regular.ttf')
fnt_rest_path = os.path.join(PROJECT_ROOT,'PTS55F.ttf')
img_path = os.path.join(PROJECT_ROOT, 'template.png')


# img = Image.open(img_path)


inst = input("Enter name of institution: ")
fnt_name = ImageFont.truetype(font_path, 65)
fnt_inst = ImageFont.truetype(font_path, 45)
fnt_rest = ImageFont.truetype(fnt_rest_path,30)


# img = Image.open(img_path)
# draw = ImageDraw.Draw(img)


for i in data:
     print(i)



for student in data:
    img = Image.open(img_path).copy()  # Create a fresh copy of the template
    draw = ImageDraw.Draw(img)
    name_text = student[1]
    class_text = student[2]
    num_text = student[0]
    gender_text = student[3]
    print(name_text)
    psp_img_path = os.path.join(PROJECT_ROOT, 'passport_images', name_text+'.jpg')




    #For institution
    draw.text(xy=(233,130),
                text = inst,
                fill=(0,0,0),
                font = fnt_inst
                )

    #for name
    draw.text(xy=(747,537), 
                text=name_text,
                fill=(255,255,255),
                font = fnt_name
                )
        
        # UID
    draw.text(xy=(245,266),
            text = str(num_text),
            fill = (0,0,128),
            font = fnt_rest)


        #class
    draw.text(xy=(245,316),
                text = str(class_text),
                fill = (0,0,128),
                font = fnt_rest)
        #gender
    draw.text(xy=(245,360),
                text = gender_text,
                fill = (0,0,128),
                font = fnt_rest)
    #photo
    passport_image = Image.open(psp_img_path)
    newsize = (370,370)
    passport_image_resized = passport_image.thumbnail(newsize)
    print(passport_image.size)
    img.paste(passport_image,(705,100))
    img.show()
        
