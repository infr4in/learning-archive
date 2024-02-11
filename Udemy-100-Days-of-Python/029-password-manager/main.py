import tkinter as tk
from tkinter import messagebox
from random import randint, choice, shuffle
import pyperclip

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
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

    if len(website) == 0 or len(password) == 0 or len(email) == 0:
        messagebox.showinfo(title="Oops", message="Please don't leave any field empty!")
    else:
        is_ok = messagebox.askokcancel(title=website, message=f"These are the details entered: \n"
                                                              f"Email: {email} \n"
                                                              f"Password: {password} \n"
                                                              f"Is it ok to save?")
        if is_ok:
            with open("./data.txt", "a") as data_file:
                data_file.write(f"{" | ".join((website, email, password))}\n")
                website_input.delete(0, tk.END)
                password_input.delete(0, tk.END)

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
website_input = tk.Entry(width=35)
website_input.grid(row=1, column=1, columnspan=2)
website_input.focus()
email_input = tk.Entry(width=35)
email_input.grid(row=2, column=1, columnspan=2)
email_input.insert(0, "user@email.com")
password_input = tk.Entry(width=21)
password_input.grid(row=3, column=1)

# Buttons
password_generate_btn = tk.Button(text="Generate Password", command=generate_password)
password_generate_btn.grid(row=3, column=2)
add_btn = tk.Button(text="Add", width=36, command=save)
add_btn.grid(row=4, column=1, columnspan=2, pady=10)

window.mainloop()
