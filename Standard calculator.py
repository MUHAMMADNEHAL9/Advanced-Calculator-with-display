from tkinter import *


def button_click(number):
    current = scvalue.get()
    scvalue.set(current + str(number))


def clear_screen():
    scvalue.set("")

def evaluate():
    try:
        expression = scvalue.get()
        expression = expression.replace("÷", "/").replace("x", "*")
        result = eval(expression)
        scvalue.set(result)
    except Exception:
        scvalue.set("Error")

root = Tk()
root.geometry("500x500")
root.title("Calculator")
root.configure(bg="#1e1e1e")

scvalue = StringVar()
scvalue.set("")

screen = Entry(root, textvar=scvalue, font="lucida 25 bold", bg="#1e1e1e", fg="white",
               insertbackground="white", bd=5, relief=RIDGE, justify=RIGHT)
screen.pack(fill=X, ipadx=10, pady=12, padx=15)

f = Frame(root, bg="#1e1e1e")
f.pack()

# Black buttons with white text
button_style = {
    "padx": 20, "pady": 20,
    "bd": 1, "relief": RIDGE,
    "bg": "black", "fg": "white",
    "activebackground": "#0078d7", "activeforeground": "white",
    "font": ("lucida", 14, "bold")
}

buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('.', 4, 1), ('+', 4, 2), ('=', 4, 3),
    ('C', 5, 0)
]

for (text, row, column) in buttons:
    if text == '=':
        Button(f, text=text, command=evaluate, **button_style).grid(row=row, column=column)
    elif text == 'C':
        Button(f, text=text, command=clear_screen, **button_style).grid(row=row, column=column)
    else:
        Button(f, text=text, command=lambda t=text: button_click(t), **button_style).grid(row=row, column=column)


f.grid_columnconfigure((0,1,2,3,4,5), weight=1)
f.grid_rowconfigure((1,2,3,4,5), weight=1)

root.mainloop()
