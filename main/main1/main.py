import csv

# Function to get user input
def get_user_input():
    name = input("Enter name: ")
    gender = input("Enter gender: ")
    age = input("Enter age: ")
    dob = input("Enter date of birth (YYYY-MM-DD): ")
    return name, gender, age, dob

# Function to save data to a CSV file
def save_to_csv(filename, data):
    with open(filename, mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(data)

# Input data and save to CSV
while True:
    name, gender, age, dob = get_user_input()
    data = [name, gender, age, dob]
    save_to_csv('data.csv', data)
    another_entry = input("Do you want to enter another entry? (yes/no): ")
    if another_entry.lower() != 'yes':
        break

print("Data saved to data.csv")

from PIL import Image, ImageDraw, ImageFont
import csv

# Load the ID card template
template = Image.open(r"x.png")
draw = ImageDraw.Draw(template)
font = ImageFont.truetype('Freedom-10eM.ttf', size=24)

# Read data from the CSV file
with open("data.csv", "r") as file:
    reader = csv.reader(file)
    next(reader)  # Skip the header row
    for row in reader:
        name, gender, age, dob = row

        # Draw text on the template
        draw.text((x, y), f"Name: {name}", fill="black", font=font)
        draw.text((x, y), f"Gender: {gender}", fill="black", font=font)
        draw.text((x, y), f"Age: {age}", fill="black", font=font)
        draw.text((x, y), f"DOB: {dob}", fill="black", font=font)

        # Save the generated ID card
        template.save(f"{name}_IDCard.png")

print("ID cards generated successfully.")