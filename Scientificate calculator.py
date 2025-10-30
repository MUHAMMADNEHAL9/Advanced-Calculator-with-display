from tkinter import *
import math

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

def scientific(func):
    try:
        value = float(scvalue.get())
        if func == "√":
            result = math.sqrt(value)
        elif func == "sin":
            result = math.sin(math.radians(value))
        elif func == "cos":
            result = math.cos(math.radians(value))
        elif func == "tan":
            result = math.tan(math.radians(value))
        elif func == "log":
            result = math.log10(value)
        elif func == "ln":
            result = math.log(value)
        elif func == "fact":
            result = math.factorial(int(value))
        elif func == "π":
            result = math.pi
        elif func == "e":
            result = math.e
        else:
            result = "Error"
        scvalue.set(result)
    except Exception:
        scvalue.set("Error")

root = Tk()
root.geometry("500x500")
root.title("Scientific Calculator")
root.configure(bg="#1e1e1e")   
scvalue = StringVar()
scvalue.set("")


screen = Entry(root, textvar=scvalue, font="lucida 25 bold", bg="#000", fg="white",
               insertbackground="white", bd=5, relief=RIDGE, justify=RIGHT)
screen.pack(fill=X, ipadx=8, pady=10, padx=10)

f = Frame(root, bg="#1e1e1e")
f.pack()

button_style = {
    "padx": 20, "pady": 20,
    "bd": 1, "relief": RIDGE,
    "bg": "#2d2d30", "fg": "white",
    "activebackground": "#0078d7", "activeforeground": "white",
    "font": ("lucida", 14, "bold")
}
buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('÷', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('x', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('.', 4, 1), ('+', 4, 2), ('=', 4, 3),
    ('C', 5, 0)
]

for (text, row, column) in buttons:
    if text == '=':
        Button(f, text=text, command=evaluate, **button_style).grid(row=row, column=column, sticky="nsew", padx=5, pady=5)
    elif text == 'C':
        Button(f, text=text, command=clear_screen, **button_style).grid(row=row, column=column, sticky="nsew", padx=5, pady=5)
    else:
        Button(f, text=text, command=lambda t=text: button_click(t), **button_style).grid(row=row, column=column, sticky="nsew", padx=5, pady=5)


scientific_buttons = [
    ('√', 1, 4), ('sin', 2, 4), ('cos', 3, 4), ('tan', 4, 4),
    ('log', 1, 5), ('ln', 2, 5), ('fact', 3, 5), ('^', 4, 5),
    ('π', 5, 4), ('e', 5, 5)
]

for (text, row, column) in scientific_buttons:
    if text == '^':
        Button(f, text=text, command=lambda: button_click("**"), **button_style).grid(row=row, column=column, sticky="nsew", padx=5, pady=5)
    else:
        Button(f, text=text, command=lambda t=text: scientific(t), **button_style).grid(row=row, column=column, sticky="nsew", padx=5, pady=5)


f.grid_columnconfigure((0,1,2,3,4,5), weight=1)
f.grid_rowconfigure((1,2,3,4,5), weight=1)

root.mainloop()
