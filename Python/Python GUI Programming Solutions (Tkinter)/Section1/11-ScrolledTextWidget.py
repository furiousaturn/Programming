import tkinter as tk
from tkinter import ttk
from tkinter import scrolledtext

win = tk.Tk()
win.title("Python GUI")

# Modify adding a Label
aLabel = ttk.Label(win, text="A Label")
aLabel.grid(column=0, row=0)


# Button Click Event Function
def clickMe():
    action.configure(text="Hello " + name.get() + " " + numberChosen.get())


# Changing our label
ttk.Label(win, text="Enter a name:").grid(column=0, row=0)

# Adding a textbox Entry Widget
name = tk.StringVar()
nameEntered = ttk.Entry(win, width=12, textvariable=name)
nameEntered.grid(column=0, row=1)

# Adding a button
action = ttk.Button(win, text="Click Me!", command=clickMe)
action.grid(column=2, row=1)
# action.configure(state="disabled")  # Disable the Button Widget

ttk.Label(win, text="Choose a number:").grid(column=1, row=0)
number = tk.StringVar()
numberChosen = ttk.Combobox(win, width=12, textvariable=number, state="readonly")
numberChosen["values"] = (1, 2, 4, 42, 100)
numberChosen.grid(column=1, row=1)
numberChosen.current(0)

# Creating three checkbuttons
chVarDis = tk.IntVar()
check1 = tk.Checkbutton(win, text="Disabled", variable=chVarDis, state="disabled")
check1.select()
check1.grid(column=0, row=4, sticky=tk.W)

chVarUn = tk.IntVar()
check2 = tk.Checkbutton(win, text="UnChecked", variable=chVarUn)
check2.deselect()
check2.grid(column=1, row=4, sticky=tk.W)

chVarEn = tk.IntVar()
check3 = tk.Checkbutton(win, text="Enabled", variable=chVarEn)
check3.select()
check3.grid(column=2, row=4, sticky=tk.W)

# RadioButton Globals
COLOR1 = "Blue"
COLOR2 = "Gold"
COLOR3 = "Red"


def radCall():
    radSel = radVar.get()
    if radSel == 1: win.configure(background=COLOR1)
    if radSel == 2: win.configure(background=COLOR2)
    if radSel == 3: win.configure(background=COLOR3)


# create three radio buttons using one variable
radVar = tk.IntVar()

rad1 = tk.Radiobutton(win, text=COLOR1, variable=radVar, value=1, command=radCall)
rad1.grid(column=0, row=5, sticky=tk.W, columnspan=3)

rad2 = tk.Radiobutton(win, text=COLOR2, variable=radVar, value=2, command=radCall)
rad2.grid(column=1, row=5, sticky=tk.W, columnspan=3)

rad3 = tk.Radiobutton(win, text=COLOR3, variable=radVar, value=3, command=radCall)
rad3.grid(column=2, row=5, sticky=tk.W, columnspan=3)

# USing a scrolled text widget
scrolW = 30
scrolH = 3

scr = scrolledtext.ScrolledText(win, width=scrolW, height=scrolH, wrap=tk.WORD)
scr.grid(column=0, columnspan=3)

nameEntered.focus()  # Place cursor into name Entry
win.mainloop()
