from PIL import Image, ImageDraw, ImageFont
import tkinter as tk
import csv

# Function to save the user inputs to a CSV file
def save_to_csv():
    name = name_entry.get()
    _class = class_entry.get()
    gender = gender_var.get()
    dob = dob_entry.get()
    uid = uid_entry.get()

    with open('user_data.csv', 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([name, _class, gender, dob, uid])

    # Clear the entry fields
    name_entry.delete(0, 'end')
    class_entry.delete(0, 'end')
    dob_entry.delete(0, 'end')
    uid_entry.delete(0, 'end')

# Create the main window
root = tk.Tk()
root.title("User Data Entry")

# Label and Entry widgets for Name
name_label = tk.Label(root, text="Name:")
name_label.pack()
name_entry = tk.Entry(root)
name_entry.pack()

# Label and Entry widgets for Class
class_label = tk.Label(root, text="Class:")
class_label.pack()
class_entry = tk.Entry(root)
class_entry.pack()

# Label and Radio buttons for Gender
gender_label = tk.Label(root, text="Gender:")
gender_label.pack()
gender_var = tk.StringVar()
male_radio = tk.Radiobutton(root, text="Male", variable=gender_var, value="Male")
female_radio = tk.Radiobutton(root, text="Female", variable=gender_var, value="Female")
male_radio.pack()
female_radio.pack()

# Label and Entry widgets for Date of Birth
dob_label = tk.Label(root, text="Date of Birth (YYYY-MM-DD):")
dob_label.pack()
dob_entry = tk.Entry(root)
dob_entry.pack()

# Label and Entry widgets for UID
uid_label = tk.Label(root, text="UID:")
uid_label.pack()
uid_entry = tk.Entry(root)
uid_entry.pack()

# Button to save the data to CSV
save_button = tk.Button(root, text="Save to CSV", command=save_to_csv)
save_button.pack()

# Start the Tkinter main loop
root.mainloop()



# # Function to generate ID cards
# def generate_id_cards():
#     with open('user_data.csv', 'r') as file:
#         reader = csv.reader(file)
#         next(reader)  # Skip the header row
#         for row in reader:
#             name, _class, gender, dob, uid = row
#             generate_id_card(name, _class, gender, dob, uid)










#------------------------------------------------------------------------------------------------------#


# Function to generate an ID card image
def generate_id_card(name, _class, gender, dob, uid):
    # Create a blank ID card template
    template = Image.open('Template.png')
    id_card = template.copy()
    draw = ImageDraw.Draw(id_card)

    # Add user information to the ID card
    font = ImageFont.truetype("arial.ttf", 16)
    draw.text((20, 20), f"Name: {name}", fill='black', font=font)
    draw.text((20, 50), f"Class: {_class}", fill='black', font=font)
    draw.text((20, 80), f"Gender: {gender}", fill='black', font=font)
    draw.text((20, 110), f"DOB: {dob}", fill='black', font=font)
    draw.text((20, 140), f"UID: {uid}", fill='black', font=font)

#----------------------------------------------------------------------------------------------------------#


















    # Save the ID card as an image file
    id_card.save(f"{name}_IDCard.png")

# Create the main window
root = tk.Tk()
root.title("ID Card Generator")

# Button to generate ID cards
generate_button = tk.Button(root, text="Generate ID Cards", command=generate_id_card)
generate_button.pack()

# Start the Tkinter main loop
root.mainloop()
