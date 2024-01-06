import random
import mysql.connector as sqlcon
import os
from PIL import Image, ImageDraw, ImageFont
from barcode import Code128
from barcode.writer import ImageWriter
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

q_create_table = 'create table student_data (roll_no int(5) primary key, name varchar(40), class int(2), gender varchar(6), dob date, email varchar(30), phone varchar(20), address varchar(50))'

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
        roll_no = int(input("Enter roll number(): "))
        email = input("Enter Email ID:")
        address = input("Enter address")
        phone = int(input("Enter phone number"))

        if gender == "M":
                gender = "Male"
        elif gender == "F":
                gender = "Female"
        else:
            print("Enter a valid gender(M/F)")

        q_adding_records = ( "INSERT INTO student_data (roll_no, name, class, gender, dob, email, phone, address) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)",(roll_no, name, Class, gender, dob, email, phone, address))
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



base_dir = r'D:\Farhan\Python\ID card generator\ID-card-generator-csproject\sample\sample11'

inst = input("Enter name of institution: ")
fnt_name = ImageFont.truetype(r"D:\Farhan\Python\ID card generator\ID-card-generator-csproject\sample\sample11\Elianto-Regular.ttf", 65)
fnt_inst = ImageFont.truetype(r"D:\Farhan\Python\ID card generator\ID-card-generator-csproject\sample\sample11\Elianto-Regular.ttf", 45)
fnt_rest = ImageFont.truetype(r"D:\Farhan\Python\ID card generator\ID-card-generator-csproject\sample\sample11\PTS55F.ttf",30)
logo_path = os.path.join(base_dir,'logos','kvslogo.png')


img_path = os.path.join(base_dir, 'templates', '1.png' )



for i in data:
     print(i)




def crop_circle(input_path, output_path):
    # Open the image
    image = Image.open(input_path)

    # Create a mask in the shape of a circle
    mask = Image.new("L", image.size, 0)
    draw = ImageDraw.Draw(mask)
    draw.ellipse((0, 0, image.width, image.height), fill=255)

    # Apply the circular mask to the image
    result = Image.new("RGBA", image.size)
    result.paste(image, mask=mask)

    # Save the result
    result.save(output_path, "PNG")













for num in range (0,len(data)):
    img = Image.open(img_path)
    draw = ImageDraw.Draw(img)
    id = data[num][0]
    name_text = data[num][1]
    class_text = data[num][2]
    num_text = data[num][0]
    gender_text = data[num][3]
    # dob_text = data[num][]
    print(num)



    # #For logo
    # logo = Image.open(logo_path)
    # logo_with_white_background = Image.new("RGBA", logo.size, (255, 255, 255))
    # logo_with_white_background.resize((50,50))
    # logo_with_white_background.paste(logo, (0, 0), logo)
    # logo_position = (50,50)
    # img.paste(logo_with_white_background, logo_position)


    #For institution
    draw.text(xy=(266,71),
                text = inst,
                fill=(0,0,0),
                font = fnt_inst
                )
    
    #For name
    if len(name_text) > 9:
         draw.text(xy=(90,490), 
                text=name_text,
                fill=(0,0,0),
                font = fnt_name
                )
    else:
         draw.text(xy=(180,490), 
                text=name_text,
                fill=(0,0,0),
                font = fnt_name
                )   
    
        
        # UID
    draw.text(xy=(245,570),
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
    
        #barcode
    barcode_value = str(id)
    bc =  Code128(barcode_value, writer=ImageWriter())
    barcode_path = os.path.join(base_dir, 'barcodes', f'barcode_{id}.png')
    bc.write(barcode_path)
    
        #photo
    



    input_image_path = os.path.join(base_dir,'photos',f"{num_text}.jpg")
    output_image_path = os.path.join(base_dir,'cropped photos',f"photo ({num_text}).png")
    crop_circle(input_image_path, output_image_path)



   
    photo_to_be_pasted = Image.open(output_image_path)
    photo_position = (162, 107)
    photo_box = (
        photo_position[0],
        photo_position[1],
        photo_position[0] + photo_to_be_pasted.width,
        photo_position[1] + photo_to_be_pasted.height
        )
        
    # img.paste(photo_to_be_pasted, photo_box)

    # img.show() 
    save_path = os.path.join(base_dir,'cards',f'{name_text}.png') 
    img.save(save_path)


# Paste the cropped photo onto the ID card

# Save or display the modified image
# img.save(f'output_image_with_photo_{num}.png')
    

#         bar_path = r"D:\ID card generator\ID-card-generator-csproject\sample\sample11\barcodes\{}.png".format(k[4])
# bar = Image.open(bar_path)
# bar.thumbnail((360,360))
# img.paste(bar,(54,477)) 



