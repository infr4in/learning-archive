import tkinter as tk
from tkinter import messagebox
from random import randint, choice, shuffle
import pyperclip
import json


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers
    shuffle(password_list)

    password = "".join(password_list)

    password_input.delete(0, tk.END)
    password_input.insert(0, password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = website_input.get()
    email = email_input.get()
    password = password_input.get()

    new_data = {
        website: {
            "email": email,
            "password": password,
        }
    }

    if len(website) == 0 or len(password) == 0 or len(email) == 0:
        messagebox.showinfo(title="Oops", message="Please don't leave any field empty!")
    else:
        try:
            with open("./data.json", "r") as data_file:
                data = json.load(data_file)
        except FileNotFoundError:
            with open("./data.json", "w") as data_file:
                json.dump(new_data, data_file, indent=4)
        else:
            data.update(new_data)

            with open("./data.json", "w") as data_file:
                json.dump(data, data_file, indent=4)
        finally:
            website_input.delete(0, tk.END)
            password_input.delete(0, tk.END)


# ---------------------------- FIND PASSWORD ------------------------------- #
def find_password():
    website = website_input.get()

    try:
        with open("data.json", "r") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo(title="Oops", message="No Data File Found")
    else:
        if website in data:
            email = data[website]["email"]
            password = data[website]["password"]
            messagebox.showinfo(title=website, message=f"Email: {email}\nPassword: {password}")
        else:
            messagebox.showinfo(title="Oops", message="No details for website exists.")


# ---------------------------- UI SETUP ------------------------------- #
window = tk.Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

# 5x3 grid
canvas = tk.Canvas(width=200, height=200, highlightthickness=0)
logo = tk.PhotoImage(file="./logo.png")
canvas.create_image(100, 100, image=logo)
canvas.grid(row=0, column=1)

# Labels
website_label = tk.Label(text="Website: ")
website_label.grid(row=1, column=0)
email_label = tk.Label(text="Email/Username: ")
email_label.grid(row=2, column=0)
password_label = tk.Label(text="Password: ")
password_label.grid(row=3, column=0)

# Entries
website_input = tk.Entry(width=30)
website_input.grid(row=1, column=1)
website_input.focus()
email_input = tk.Entry(width=30)
email_input.grid(row=2, column=1)
email_input.insert(0, "user@email.com")
password_input = tk.Entry(width=30)
password_input.grid(row=3, column=1)

# Buttons
search_btn = tk.Button(text="Search", command=find_password, width=15)
search_btn.grid(row=1, column=2)
password_generate_btn = tk.Button(text="Generate Password", command=generate_password, width=15)
password_generate_btn.grid(row=3, column=2)
add_btn = tk.Button(text="Add", width=44, command=save)
add_btn.grid(row=4, column=1, columnspan=2, pady=10)

window.mainloop()
