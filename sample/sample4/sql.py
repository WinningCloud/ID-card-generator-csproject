import sqlite3

# Function to insert ID card information into the database
def insert_id_card_data(data):
    conn = sqlite3.connect('farhan6389.db')
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO id_cards (name, employee_id, department, expiry_date)
        VALUES (?, ?, ?, ?)
    ''', (data['name'], data['employee_id'], data['department'], data['expiry_date']))
    conn.commit()
    conn.close()

while True:
    name = input("Enter name:")
    employee_id = int(input("Enter employee Id:"))
    department = input("Enter department:")
    expiry_date = input("Enter expiry date:")

    user_data = {
        "name":name,
        "employee_id":employee_id,
        'department': department,
        'expiry_date': expiry_date
    }
    insert_id_card_data(user_data)
    another_entry = "Do you wish to add another entry? y or n"
    if another_entry == n or another_entry == N:
        break


    from PIL import Image, ImageDraw, ImageFont

# Load the template image
template = Image.open('id_template.png')

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