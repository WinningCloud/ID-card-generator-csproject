from PIL import Image, ImageDraw, ImageFont

# Load the template image
template = Image.open('template.png')

# Create a drawing object
draw = ImageDraw.Draw(template)

# Load a font (you may need to adjust the font path)
font = ImageFont.truetype('arial.ttf', size=24)

# Define the information to be added to the ID card
id_info = {
    'name': 'John Doe',
    'id': '12345',
    'department': 'Engineering',
    'expiry_date': '12/31/2024',
}

# Define the positions for text elements
text_positions = {
    'name': (100, 200),
    'id': (100, 260),
    'department': (100, 320),
    'expiry_date': (100, 380),
}

# Add text to the image
for field, text_position in text_positions.items():
    draw.text(text_position, f"{field.capitalize()}: {id_info[field]}", fill=(0, 0, 0), font=font)

# Save the generated ID card
template.save('generated_id_card.png')

# Display the generated ID card
template.show()

