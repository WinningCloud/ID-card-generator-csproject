import tkinter as tk
import csv

def save_to_csv():
    name = name_entry.get()
    age = age_entry.get()
    gender = gender_entry.get()
    class_ = class_entry.get()
    uid = uid_entry.get()

    with open(r'D:\ID card generator\ID-card-generator-csproject\main\main2\user_data.csv', mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([name, age, gender, class_, uid])

    # Clear input fields after saving
    name_entry.delete(0, 'end')
    age_entry.delete(0, 'end')
    gender_entry.delete(0, 'end')
    class_entry.delete(0, 'end')
    uid_entry.delete(0, 'end')

app = tk.Tk()
app.title("User Information")

# Create labels and entry fields
name_label = tk.Label(app, text="Name")
name_label.grid(row=0, column=0)
name_entry = tk.Entry(app)
name_entry.grid(row=0, column=1)

age_label = tk.Label(app, text="Age")
age_label.grid(row=1, column=0)
age_entry = tk.Entry(app)
age_entry.grid(row=1, column=1)

gender_label = tk.Label(app, text="Gender")
gender_label.grid(row=2, column=0)
gender_entry = tk.Entry(app)
gender_entry.grid(row=2, column=1)

class_label = tk.Label(app, text="Class")
class_label.grid(row=3, column=0)
class_entry = tk.Entry(app)
class_entry.grid(row=3, column=1)

uid_label = tk.Label(app, text="UID")
uid_label.grid(row=4, column=0)
uid_entry = tk.Entry(app)
uid_entry.grid(row=4, column=1)

# Create a "Save" button
save_button = tk.Button(app, text="Save", command=save_to_csv)
save_button.grid(row=5, column=0, columnspan=2)

app.mainloop()