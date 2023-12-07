import mysql.connector as mysqlcon
import random

#-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
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
# print(data)

q3 = "use idcards_data"
cur.execute(q3)

q4 = "show tables"
cur.execute(q4)
data2 = cur.fetchall()
# print(data2)

q5 = "create table stud_data (roll_no int(5) primary key, name varchar(40), class int(2), gender varchar(6), dob date)"
t = ("stud_data",)
if t in data2:
    pass
else:
    cur.execute(q5)


n = int(input("Enter number of records to input: "))
for i in range(n) :
        name = input("Enter name: ")
        clas = int(input("Enter class: "))
        gender = input("Enter gender(M/F)")
        if gender == "M":
            gender = "Male"
        elif gender == "F":
            gender = "Female"
        else:
            print("Enter a valid gender(M/F)")
            
        dob = input("Enter Date of Birth: ")
        roll_no = random.randint(100000,999999)

        q6 = "INSERT INTO stud_data VALUES (%s, %s, %s, %s, %s)(roll_no, name, clas, gender, dob)"
        cur.execute(q6)
print(n," students data successfully entered.")
con.commit()







#-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-#
#for taking out data


q7 = "select roll_no from stud_data"
cur.execute(q7)
rno = cur.fetchall()

q8 = "select name from stud_data"
cur.execute(q8)
nm = cur.fetchall()

q9 = "select class from stud_data"
cur.execute(q9)
cls = cur.fetchall()

q10 = "select dob from stud_data"
cur.execute(q10)
db = cur.fetchall()

q11 = "select gender from stud_data"
cur.execute(q11)
gdr = cur.fetchall()
# print(rno, nm, cls, db, gdr)



#-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-#


from PIL import Image, ImageDraw, ImageFont
from barcode import EAN13_GUARD
from barcode.writer import ImageWriter


inst = input("Enter name of institution: ")


#fonts
fnt_name = ImageFont.truetype(r"D:\ID card generator\ID-card-generator-csproject\sample\sample11\Elianto-Regular.ttf", 65)
fnt_inst = ImageFont.truetype(r"D:\ID card generator\ID-card-generator-csproject\sample\sample11\Elianto-Regular.ttf", 45)
fnt_rest = ImageFont.truetype(r"D:\ID card generator\ID-card-generator-csproject\sample\sample11\PTS55F.ttf",30)

img = Image.open(r'D:\ID card generator\ID-card-generator-csproject\sample\sample11\template.png')
draw = ImageDraw.Draw(img)




#For name
for i in range(0,n):

    #For institution
    draw.text(xy=(233,130),
              text = inst,
              fill=(0,0,0),
              font = fnt_inst)

    name_text = nm[i][0]
    draw.text(xy=(747,537), 
              text=name_text,
              fill=(255,255,255),
              font=fnt_name)
    
    # UID
    num_text = rno[i][0]
    draw.text(xy=(245,266),
            text = str(num_text),
            font = fnt_rest,
            fill = (0,0,128))
    img.show()

#barcode

# barcode_path = r"D:\ID card generator\ID-card-generator-csproject\sample\sample11\barcodes\{}".format(k[4])


# my_code = EAN13(num_text, writer=ImageWriter()) 
# my_code.save(barcode_path)

























con.close()