import tkinter as tk
from tkinter import ttk

win = tk.Tk()
win.title("Programming GUI")

ttk.Label(win, text="A Label").grid(column=0, row=0)
win.mainloop()
