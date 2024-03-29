import tkinter as tk
import math as m
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
CHECKMARK = "✔"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None


# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    title_label.config(text="Title", fg=GREEN)
    global reps
    reps = 0
    checkmarks_label.config(text="")


# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    reps += 1

    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if reps % 8 == 0:
        count_down(long_break_sec)
        title_label.config(text="Break", fg=RED)
    elif reps % 2 == 0:
        count_down(short_break_sec)
        title_label.config(text="Break", fg=PINK)
    else:
        count_down(work_sec)
        title_label.config(text="Work", fg=GREEN)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    count_min = m.floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        checkmarks_label.config(text=CHECKMARK * (reps // 2))


# ---------------------------- UI SETUP ------------------------------- #
window = tk.Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

# 4x3 grid
# row 1
title_label = tk.Label(text="Timer", bg=YELLOW, fg=GREEN, font=(FONT_NAME, 50), width=5)
title_label.grid(row=1, column=2)

# row 2
canvas = tk.Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
pomodoro_img = tk.PhotoImage(file="./tomato.png")
canvas.create_image(100, 112, image=pomodoro_img)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(row=2, column=2)

# row 3
start_btn = tk.Button(text="Start", command=start_timer, highlightthickness=0)
start_btn.grid(row=3, column=1)

reset_btn = tk.Button(text="Reset", command=reset_timer, highlightthickness=0)
reset_btn.grid(row=3, column=3)

# row 4
checkmarks_label = tk.Label(text="", bg=YELLOW, fg=GREEN, font=(FONT_NAME, 20, "bold"))
checkmarks_label.grid(row=4, column=2)

window.mainloop()
