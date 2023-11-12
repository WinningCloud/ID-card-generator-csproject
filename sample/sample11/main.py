from PIL import Image, ImageDraw, ImageFont
import random
from barcode import EAN13 
from barcode.writer import ImageWriter

#data storage
#No. of ID cards you want to genarate
n = int(input("Enter number of ID cards you want to genarate"))
inst = input("Enter name of institution")

def user_inputs():
    name = input(("Enter full name: "))
    Class = int(input("Enter class: "))
    gender = input("Gender (M/F): ")
    DOB = input("Enter DOB")
    Roll_no = int(input("Enter roll number: "))
    return(name, Class, gender, DOB, Roll_no)
    
k = user_inputs()

fnt_name = ImageFont.truetype(r"D:\ID card generator\ID-card-generator-csproject\sample\sample11\Elianto-Regular.ttf", 65)
fnt_inst = ImageFont.truetype(r"D:\ID card generator\ID-card-generator-csproject\sample\sample11\Elianto-Regular.ttf", 45)


fnt_rest = ImageFont.truetype(r"D:\ID card generator\ID-card-generator-csproject\sample\sample11\PTS55F.ttf",30)


img = Image.open(r'D:\ID card generator\ID-card-generator-csproject\sample\sample11\template.png')
draw = ImageDraw.Draw(img)




# image manipulation
# for institution

draw.text(xy=(233,130),
          text = inst,
          fill=(0,0,0),
          font = fnt_inst)




# for name
name_text = k[0].upper()

draw.text(xy=(747,537), 
          text=name_text,
          fill=(255,255,255),
          font=fnt_name)

# UID
num = str(random.randint(10000,99999999))
draw.text(xy=(245,266),
          text = str(num),
          font = fnt_rest,
          fill = (0,0,128))


#barcode
# number = str(num)
barcode_path = r"D:\ID card generator\ID-card-generator-csproject\sample\sample11\barcodes\{}".format(k[4])

# number = str(num)
my_code = EAN13(num, writer=ImageWriter()) 
my_code.save(barcode_path)


#Class
draw.text(xy=(245,315),
          text=str(k[1]),
          fill=(0,0,128),
          font=fnt_rest)


# gender
if k[2] == "M":
    gender_dat = "Male"
else:
    gender_dat = "Female"

draw.text(xy=(245,360),
          text=gender_dat,
          fill = (0,0,128),
          font=fnt_rest)

#DOB
draw.text(xy=(245,403),
          text = k[3],
          fill = (0,0,128),
          font = fnt_rest
          )



# for passport size image
image_path = r'D:\ID card generator\ID-card-generator-csproject\sample\sample11\photos\{}.jpg'.format(k[4])
passport_image = Image.open(image_path)
newsize = (370,370)
passport_image_resized = passport_image.thumbnail(newsize)
print(passport_image.size)
img.paste(passport_image,(705,100))




# #for pasting barcode
bar_path = r"D:\ID card generator\ID-card-generator-csproject\sample\sample11\barcodes\{}.png".format(k[4])
bar = Image.open(bar_path)
bar.thumbnail((360,360))
img.paste(bar,(54,477)) 



#displaying the image
img.show()


#saving the image
save_dir = r'D:\ID card generator\ID-card-generator-csproject\sample\sample11\cards\{}.png'.format(k[4])
img.save(save_dir)