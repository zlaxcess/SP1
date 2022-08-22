import tkinter as tk
from ctypes import windll
from tkinter import ttk

try:
    # DPI adjust to suitable
    windll.shcore.SetProcessDpiAwareness(1)

    root = tk.Tk()
    root.title('Tkinter Window Demo')
    root.geometry('1200x800+50+50')

    # Always on top
    root.attributes('-topmost', 1)

    # place a label on the root window
    ttk.Label(root, text='Hi, there').pack()

finally:
    root.mainloop()
