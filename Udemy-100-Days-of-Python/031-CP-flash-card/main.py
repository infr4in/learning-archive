from tkinter import *
import pandas
import random

TARGET_LANG = "German"
NATIVE_LANG = "Russian"
BACKGROUND_COLOR = "#B1DDC6"
current_card = {}
to_learn = {}

try:
    data = pandas.read_csv("./words_to_learn.csv")
except FileNotFoundError:
    original_data = pandas.read_csv("./data/german_words.csv")
    to_learn = original_data.to_dict(orient="records")
else:
    to_learn = data.to_dict(orient="records")


# ---------------------------- MECHANISM ------------------------------- #
def next_card():
    global current_card, flip_timer

    try:
        window.after_cancel(flip_timer)
    except NameError:
        pass

    if to_learn:
        current_card = random.choice(to_learn)
        canvas.itemconfig(card_bg, image=card_front)
        canvas.itemconfig(card_title, text=TARGET_LANG, fill="black")
        canvas.itemconfig(card_word, text=current_card[TARGET_LANG], fill="black")
        flip_timer = window.after(3000, func=flip_card)
    else:
        no_words()


def flip_card():
    canvas.itemconfig(card_bg, image=card_back)
    canvas.itemconfig(card_title, text=NATIVE_LANG, fill="white")
    canvas.itemconfig(card_word, text=current_card[NATIVE_LANG], fill="white")


def is_know():
    if to_learn:
        to_learn.remove(current_card)
        words_to_learn = pandas.DataFrame(to_learn)
        words_to_learn.to_csv("./data/words_to_learn.csv", index=False)
        next_card()
    else:
        no_words()


def no_words():
    canvas.itemconfig(card_bg, image=card_front)
    canvas.itemconfig(card_title, text="No Words in Deck", fill="black")
    canvas.itemconfig(card_word, text="You learned all the words.\n\nUpdate deck, \nif you want to study further",
                      justify=CENTER, fill="black", font=("Arial", 20, "bold"))


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Flash Card App")
window.config(padx=50, pady=50, background=BACKGROUND_COLOR)

# 2x2 grid
canvas = Canvas(width=800, height=528, bg=BACKGROUND_COLOR, highlightthickness=0)
card_front = PhotoImage(file="./images/card_front.png")
card_back = PhotoImage(file="./images/card_back.png")
card_bg = canvas.create_image(400, 264, image=card_front)
card_title = canvas.create_text(400, 150, text="Title", font=("Arial", 40, "italic"))
card_word = canvas.create_text(400, 263, text="word", font=("Arial", 60, "bold"))
canvas.grid(row=0, column=0, columnspan=2)

# Buttons
wrong_img = PhotoImage(file="./images/wrong.png")
wrong = Button(image=wrong_img, command=next_card, highlightthickness=0, borderwidth=0)
wrong.grid(row=1, column=0)
right_img = PhotoImage(file="./images/right.png")
right = Button(image=right_img, command=is_know, highlightthickness=0, borderwidth=0)
right.grid(row=1, column=1)

next_card()

window.mainloop()
