import tkinter as tk
from tkinter import ttk

win = tk.Tk()
win.title("Python GUI")

# Modify adding a Label

aLabel = ttk.Label(win, text="A Label")
aLabel.grid(column=0, row=0)


# Button Click Event Function
def clickMe():
    action.configure(text="Hello " + name.get())


# Changing our label
ttk.Label(win, text="Enter a name:").grid(column=0, row=0)

# Adding a textbox Entry Widget
name = tk.StringVar()
nameEntered = ttk.Entry(win, width=12, textvariable=name)
nameEntered.grid(column=0, row=1)

# Adding a button
action = ttk.Button(win, text="Click Me!", command=clickMe)
action.grid(column=1, row=1)

win.mainloop()
