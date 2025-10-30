import tkinter as tk
from tkinter import ttk
import math

TO_RAD = {
    "Degrees": math.pi / 180,
    "Radians": 1,
    "Gradians": math.pi / 200
}

UNITS = list(TO_RAD.keys())

def convert():
    try:
        value = float(display_var.get())
        from_unit = from_combo.get()
        to_unit = to_combo.get()

        value_in_rad = value * TO_RAD[from_unit]
        converted = value_in_rad / TO_RAD[to_unit]

        result_var.set(f"{converted:,.6f} {to_unit}")
    except:
        result_var.set("Invalid Input!")

def press(key):
    cur = display_var.get()
    if cur == "0" and key not in ["."]:
        cur = ""
    if key == "CE":
        display_var.set("0")
    elif key == "⌫":
        display_var.set(cur[:-1] if len(cur) > 1 else "0")
    else:
        if key == "." and "." in cur:
            return
        display_var.set(cur + key)

root = tk.Tk()
root.title("Angle Converter")
root.geometry("700x450")
root.configure(bg="#111")

display_var = tk.StringVar(value="0")
display = tk.Label(root, textvariable=display_var,
                   font=("Segoe UI", 28), bg="#111", fg="white", anchor="c")
display.pack(fill="x", padx=10, pady=10)

from_combo = ttk.Combobox(root, values=UNITS, state="readonly", font=("Segoe UI", 12))
from_combo.current(0)  
from_combo.pack(pady=5)

to_combo = ttk.Combobox(root, values=UNITS, state="readonly", font=("Segoe UI", 12))
to_combo.current(1)  
to_combo.pack(pady=5)

tk.Button(root, text="Convert", command=convert,
          font=("Segoe UI", 12), bg="#2b2b2b", fg="white", bd=0).pack(pady=5)

result_var = tk.StringVar()
result_label = tk.Label(root, textvariable=result_var,
                        font=("Segoe UI", 16), bg="#111", fg="#ddd", justify="center")
result_label.pack(pady=15)

frame = tk.Frame(root, bg="#111")
frame.pack(side="right", padx=20)

keys = [
    ["CE", "⌫"],
    ["7", "8", "9"],
    ["4", "5", "6"],
    ["1", "2", "3"],
    ["0", "."]
]

for r, row in enumerate(keys):
    row_frame = tk.Frame(frame, bg="#111")
    row_frame.pack()
    for key in row:
        btn = tk.Button(row_frame, text=key, width=17, height=2,
                        font=("Segoe UI", 14),
                        command=lambda k=key: press(k),
                        bg="#2b2b2b", fg="white", bd=0)
        btn.pack(side='left', padx=5, pady=5)

root.mainloop()
