from PIL import Image, ImageDraw, ImageFont

# Create a blank image with a white background
width, height = 600, 400
img = Image.new('RGB', (width, height), 'white')
draw = ImageDraw.Draw(img)

# Load a font
font = ImageFont.load_default()

# Define user data
user_data = {
    'name': 'John Doe',
    'employee_id': '12345',
    'department': 'IT',
    'photo': 'path_to_user_photo.jpg'
}

# Draw the ID card elements
draw.text((10, 10), f"Name: {user_data['name']}", fill='black', font=font)
draw.text((10, 40), f"Employee ID: {user_data['employee_id']}", fill='black', font=font)
draw.text((10, 70), f"Department: {user_data['department']}", fill='black', font=font)

# Paste the user photo
photo = Image.open(user_data['photo'])
img.paste(photo, (400, 10))

# Save the generated ID card
img.save('generated_id_card.png')
