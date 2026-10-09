import tkinter as tk
import tkinter.messagebox
from tkinter.constants import SUNKEN

# Creates window with title
win = tk.Tk()
win.title('Test')

# Creates frame with background color and padding
frame = tk.Frame(win, bg="gray", padx=10)
frame.pack()

# Creates border
entry = tk.Entry(frame, relief=SUNKEN, borderwidth=3, width=30)
