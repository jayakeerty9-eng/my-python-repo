import tkinter as tk
from time import strftime


def update_clock():
    clock_label.config(text=strftime("%H:%M:%S"))
    root.after(1000, update_clock)


root = tk.Tk()
root.title("Digital Clock")
clock_label = tk.Label(root, font=("Arial", 48), padx=20, pady=10)
clock_label.pack()
update_clock()
root.mainloop()