import tkinter as tk

window = tk.Tk()
window.title("Miles to Km Converter")
window.config(padx=20, pady=20)


def calculate():
    miles = float(miles_input.get())
    km = round(miles * 1.61, 1)
    converted_number_label.config(text=f"{km}")


# 3x3 grid
# row 1
miles_input = tk.Entry(width=8)
miles_input.insert(0, string="0")
miles_input.grid(column=2, row=1)

miles_label = tk.Label(text="Miles")
miles_label.grid(column=3, row=1)

# row 2
is_equal_label = tk.Label(text="is equal to")
is_equal_label.grid(column=1, row=2)

converted_number_label = tk.Label(text="0")
converted_number_label.grid(column=2, row=2)

km_label = tk.Label(text="Km")
km_label.grid(column=3, row=2)

# row 3
calc_button = tk.Button(text="Calculate", command=calculate)
calc_button.grid(column=2, row=3)

window.mainloop()
