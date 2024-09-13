from tkinter import *
from tkinter import ttk

root = Tk()
frm = ttk.Frame(root, padding=10)

frm.grid()

ttk.Label(frm, text="ola tonoto").grid(column=0, row=0)
ttk.Button(frm, text="adio tonoto", command=root.destroy).grid(column=1, row=1)

root.mainloop()