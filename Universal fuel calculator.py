import tkinter as tk
from tkinter import ttk


TO_KILOMETERS = {
    "Kilometers": 1,
    "Meters": 1 / 1000,
    "Millimeters": 1 / 1_000_000
}

DISTANCE_UNITS = list(TO_KILOMETERS.keys())


def convert_fuel():
    """Calculate fuel needed for given distance."""
    try:
        distance = float(display_var.get())
        distance_unit = distance_unit_combo.get()
        mileage = float(mileage_var.get())

        
        distance_km = distance * TO_KILOMETERS[distance_unit]
        fuel_needed = distance_km / mileage

        result_var.set(
            f"Distance: {distance_km:.2f} km\n"
            f"Fuel Needed: {fuel_needed:.2f} liters"
        )
    except:
        result_var.set("Invalid input!")

def press(key):
    """Keypad button press logic."""
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
root.title("Fuel Calculator")
root.geometry("600x450")
root.configure(bg="#111")

display_var = tk.StringVar(value="0")
display = tk.Label(root, textvariable=display_var, font=("Segoe UI", 28), bg="#111", fg="white", anchor="c")
display.pack(fill="x", padx=10, pady=10)


tk.Label(root, text="Fuel Calculator", font=("Segoe UI", 16), bg="#111", fg="#00ff99").pack(pady=(10,0))
distance_unit_combo = ttk.Combobox(root, values=DISTANCE_UNITS, state="readonly", font=("Segoe UI", 12))
distance_unit_combo.current(0)
distance_unit_combo.pack(pady=5)

mileage_var = tk.StringVar(value="12")
tk.Entry(root, textvariable=mileage_var, font=("Segoe UI", 12), justify="center").pack(pady=5)
tk.Label(root, text="(Enter Car Mileage - km per liter)", font=("Segoe UI", 10), bg="#111", fg="#aaa").pack()

tk.Button(root, text="Calculate Fuel", command=convert_fuel, font=("Segoe UI", 12), bg="#333", fg="white").pack(pady=5)

result_var = tk.StringVar()
result_label = tk.Label(root, textvariable=result_var, font=("Consolas", 12), bg="#111", fg="#ddd", justify="left")
result_label.pack(pady=10)


frame = tk.Frame(root, bg="#111")
frame.pack(side="right", padx=20)

keys = [
    ["7","8","9"],
    ["4","5","6"],
    ["1","2","3"],
    ["0",".","CE"],
    ["⌫","-"]
]

for r, row in enumerate(keys):
    row_frame = tk.Frame(frame, bg="#111")
    row_frame.pack()
    for key in row:
        btn = tk.Button(row_frame, text=key, width=17, height=2, font=("Segoe UI", 14),
                        command=lambda k=key: press(k),
                        bg="#2b2b2b", fg="white", bd=0)
        btn.pack(side='left', padx=5, pady=5)

root.mainloop()
