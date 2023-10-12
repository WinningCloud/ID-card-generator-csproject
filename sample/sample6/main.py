import csv
import random

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
    r_id = random.randint(1000,9999)
    name, gender, age, dob = get_user_input()
    data = [name, gender, age, dob, r_id]
    save_to_csv(r'D:\ID card generator\ID-card-generator-csproject\sample\sample6\data.csv', data)
    another_entry = input("Do you want to enter another entry? (yes/no): ")
    if another_entry.lower() != 'yes':
        break

print("Data saved to data.csv")

from PIL import Image, ImageDraw, ImageFont
import csv

# Load the ID card template
template = Image.open(r"D:\ID card generator\ID-card-generator-csproject\sample\sample6\template.png")
# font = ImageFont.truetype('Freedom-10eMf', size=24)
font = ImageFont.truetype(r'C:\Users\farha\Downloads\freedom-font\Freedom-10eM.ttf', 70)
# Read data from the CSV file
with open("data.csv", "r") as file:
    reader = csv.reader(file)
    next(reader)  # Skip the header row
    for row in reader:
        name, gender, age, dob,r_id = row

        # Create a new ID card based on the template
        id_card = template.copy()
        draw = ImageDraw.Draw(id_card)

        # Draw text on the ID card
        draw.text((278, 866), f"Name: {name}", fill="black", font=font)
        draw.text((278, 926), f"Gender: {gender}", fill="black", font=font)
        draw.text((278, 980), f"Age: {age}", fill="black", font=font)
        draw.text((278, 1010), f"DOB: {dob}", fill="black", font=font)
        draw.text((278, 1060), f"ID: {r_id}", fill="black", font=font)

        # Save the generated ID card
        id_card.save(f"D:\ID card generator\ID-card-generator-csproject\sample\sample6\cards\{name}_IDCard.png")

print("ID cards generated successfully.")
