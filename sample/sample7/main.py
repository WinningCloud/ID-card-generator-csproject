from PIL import Image, ImageDraw, ImageFont

# Load the ID card template
template = Image.open(r"D:\ID card generator\ID-card-generator-csproject\sample\sample7\template.png")
draw = ImageDraw.Draw(template)

# Function to add personal information
font = ImageFont.truetype('arial.ttf', size=260)
def add_info(template, text, position, font, fill_color):
    draw = ImageDraw.Draw(template)
    draw.text(position, text, fill=fill_color, font=font)

# Add text
font = ImageFont.load_default()  # You can choose a different font if desired
add_info(template, "Name: John Doe", (290, 850), font, (0, 0, 0, 0))
add_info(template, "ID: 12345", (290, 983), font, (0, 0, 0, 0))


# Add a photo
photo = Image.open(r"D:\ID card generator\ID-card-generator-csproject\sample\sample7\photos\1.png")     
template = template.convert("RGBA")
photo = photo.convert("RGBA")
new_photo = photo.resize((250,250))
template.paste(new_photo, (284,311))

# Save the generated ID card
template.save(r"D:\ID card generator\ID-card-generator-csproject\sample\sample7\cards\generated_id_card16.png")
