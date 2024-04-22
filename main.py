from tkinter import *
from tkinter import messagebox
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
# Password Generator Project
import random
import json

def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [random.choice(letters) for _ in range(random.randint(8, 10))]
    password_numbers = [random.choice(symbols) for _ in range(random.randint(2, 4))]
    password_symbols = [random.choice(numbers) for _ in range(random.randint(2, 4))]

    password_list = password_letters + password_numbers + password_symbols

    random.shuffle(password_list)

    password = "".join(password_list)

    print(f"Your password is: {password}")
    password_entry.insert(0, f"f{password}")
# ---------------------------- find password -------------------------------#


def find_password():
    website = site_entry.get()
    try:
        with open("data.json")as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo(title="error", message="no data file found")
    else:
        if website in data:
            messagebox.showinfo(title="password", message=f"the Email and password for this site is \n"
                                                          f"email: {data[website]['password']}\n"
                                                          f"password: {data[website]['password']}")
        else:
            messagebox.showinfo(title="error", message=f"no detail for the site {website}")

# ---------------------------- SAVE PASSWORD ------------------------------- #


def save():
    website = site_entry.get()
    email_username = email_username_entry.get()
    password = password_entry.get()
    new_data = {
        website: {
            "email": email_username,
            "password": password
        }
    }

    if len(website) == 0 or len(password) == 0 or len(email_username) == 0:
        messagebox.showinfo(title="Error", message="you have unfilled entry")
    else:
        try:
            with open("data.json", "r") as data_file:
                # json.dump(new_data, data_file, indent=4)
                data = json.load(data_file)
        except FileNotFoundError:
            with open("data.json", "w")as data_file:
                json.dump(new_data, data_file, indent=4)
        else:
            data.update(new_data)
            with open("data.json", "w") as data_file:
                json.dump(data, data_file, indent=4)
        finally:
            site_entry.delete(0, END)
            password_entry.delete(0, END)
            # data_file.write(f"{website} | {email_username} | {password} \n")


# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("password manager")
window.config(padx=50, pady=50)

canvas = Canvas(height=200, width=200)
logo_img = PhotoImage(file='logo.png')
canvas_image = canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0, column=1)

site_label = Label(text="Website:", font=("Arial", 11))
site_label.focus()
site_label.grid(column=0, row=1)
site_entry = Entry(width=28)
site_entry.grid(row=1, column=1)
search_button = Button(width=13, text="search", command=find_password)
search_button.grid(row=1, column=2)

email_username_label = Label(text="emil/username:", font=("Arial", 11))
email_username_label.grid(column=0, row=2)
email_username_entry = Entry(width=35)
email_username_entry.insert(0, "eyoelZewde9876@gmail.com")
email_username_entry.grid(row=2, column=1, columnspan=2)

password_label = Label(text="Password:", font=("Arial", 11))
password_label.grid(column=0, row=3)
password_entry = Entry(width=21)
password_entry.grid(row=3, column=1)

password_generate = Button(text="Generate Password", command=generate_password)
password_generate.grid(column=2, row=3)

add_button = Button(width=36, text="add", command=save)
add_button.grid(column=1, row=4, columnspan=2)

window.mainloop()
