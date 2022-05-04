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

# First we change our RadioButton global variables into a list
colors = ["Blue", "Gold", "Red"]


def radCall():
    radSel = radVar.get()
    if radSel == 1: win.configure(background=colors[0])
    if radSel == 2: win.configure(background=colors[1])
    if radSel == 3: win.configure(background=colors[2])


# create three radio buttons using one variable
radVar = tk.IntVar()

# Next we are selecting a non-exiting index value for radVar
radVar.set(99)

# Now we are creating all three RadioButton widgets within one loop
for col in range(3):
    curRad = "rad" + str(col)
    curRad = tk.Radiobutton(win, text=colors[col], variable=radVar, value=col, command=radCall)
    curRad.grid(column=col, row=6, sticky=tk.W)

# Create a container to hold labels
labelsFrame = ttk.LabelFrame(win, text=" Labels in a frame")
labelsFrame.grid(column=0, row=7, padx=20, pady=40)

# Place labels into the container element
ttk.Label(labelsFrame, text="Label1").grid(column=0, row=0)
ttk.Label(labelsFrame, text="Label2").grid(column=0, row=1)
ttk.Label(labelsFrame, text="Label3").grid(column=0, row=2)

#After setting layout, at the end decide on the spacing - assigns padding to each label in labelsFrame
for child in labelsFrame.winfo_children():
    child.grid_configure(padx=8, pady=4)


nameEntered.focus()  # Place cursor into name Entry
win.mainloop()
