import tkinter as tk
from tkinter import ttk


TO_SECONDS = {
    "Microseconds": 1e-6,
    "Milliseconds": 1e-3,
    "Seconds": 1,
    "Minutes": 60,
    "Hours": 3600,
    "Days": 86400,
    "Weeks": 604800,
    "Years": 31536000,   
}

UNITS = list(TO_SECONDS.keys())

def convert():
    try:
        value = float(display_var.get())
        unit = unit_combo.get()
        seconds = value * TO_SECONDS[unit]

       
        breakdown = (
          f"{int(value):,} {unit}\n\n"
          f"≈ {int(seconds/60)} min, {int(seconds/3600)} hr, {int(seconds/86400)} day, {int(seconds/604800)} wk, {seconds/31536000:.2f} yr\n\n"
          f"{int(seconds):,} s\n"
          f"{int(seconds*1000):,} ms\n"
          f"{int(seconds*1_000_000):,} μs"
        )
        result_var.set(breakdown)
    except:
        result_var.set("Invalid input!")

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
root.title("Time Calculator")
root.geometry("600x400")
root.configure(bg="#111")


display_var = tk.StringVar(value="0")
display = tk.Label(root, textvariable=display_var, font=("Segoe UI", 28), bg="#111", fg="white", anchor="c")
display.pack(fill="x", padx=10, pady=10)


unit_combo = ttk.Combobox(root, values=UNITS, state="readonly", font=("Segoe UI", 12))
unit_combo.current(3) 
unit_combo.pack(pady=5)


tk.Button(root, text="Convert", command=convert, font=("Segoe UI", 12)).pack(pady=5)


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
