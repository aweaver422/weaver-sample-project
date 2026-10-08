# Following Geeks for Geeks Simple Calculator Tutorial
# Making notes as I go in order to understand the process...

# Function for adding
def add(n1, n2):
    return n1 + n2;

# Function for subtracting
def subtract(n1, n2):
    return n1 - n2;

# Function for multiplying
def multiply(n1, n2):
    return n1 * n2;

# Function for dividing
def divide(n1, n2):
    return n1 / n2;

print("Please select operation -\n"
      "1. Add\n"
      "2. Subtract\n"
      "3. Multiply\n"
      "4. Divide\n")

# This asks the user to select a number from the above list
sel = int(input("Select operation (1-4): "))

# This asks the user for the first number they'd like to input
n1 = int(input("Enter first number: "))

# This asks the user for the second number they'd like to input
n2 = int(input("Enter second number: "))


# If the user selects 1, the program adds n1 and n2
if sel == 1:
    print(n1, "+", n2, "=", add(n1, n2))

# If the user selects 2, the program subtracts n1 and n2
elif sel == 2:
    print(n1, "-", n2, "=", subtract(n1, n2))

# If the user selects 3, the program multiplies n1 and n2
elif sel == 3:
    print(n1, "*", n2, "=", multiply(n1, n2))

# If the user selects 4, the program divides n1 and n2
elif sel == 4:
    print(n1, "/", n2, "=", divide(n1, n2))

# If no valid input, the program outputs an error message
else:
    print("Invalid input")

import tkinter as tk
import tkinter.messagebox
from tkinter.constants import SUNKEN

win = tk.Tk()
win.title('Calculator')

frame = tk.Frame(win, bg="skyblue", padx=10)
frame.pack()

entry = tk.Entry(frame, relief=SUNKEN, borderwidth=3, width=30)
entry.grid(row=0, column=0, columnspan=3, ipady=2, pady=2)

def click(num):
    entry.insert(tk.END, num)

def equal():
    try:
        res = str(eval(entry.get()))
        entry.delete(0, tk.END)
        entry.insert(0, res)
    except:
        tk.messagebox.showinfo("Error", "Syntax Error")

def clear():
    entry.delete(0, tk.END)

buttons = [
    ('1', 1, 0), ('2', 1, 1), ('3', 1, 2),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2),
    ('7', 3, 0), ('8', 3, 1), ('9', 3, 2),
    ('0', 4, 1), ('+', 5, 0), ('-', 5, 1),
    ('*', 5, 2), ('/', 6, 0)
]

for txt, r, c in buttons:
    tk.Button(frame, text=txt, padx=15, pady=5, width=3, command=lambda t=txt: click(t)).grid(row=r, column=c, pady=2)

tk.Button(frame, text="Clear", padx=15, pady=5, width=12, command=clear).grid(row=6, column=1, columnspan=2, pady=2)
tk.Button(frame, text="=", padx=15, pady=5, width=9, command=equal).grid(row=7, column=0, columnspan=3, pady=2)

win.mainloop()