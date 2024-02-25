import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

def get_time():
    time = f"{hour_var.get()}:{minute_var.get()} {ampm_var.get()}"
    messagebox.showinfo("Selected Time", f"The selected time is: {time}")

root = tk.Tk()
root.title("Time Picker")

# Hour
hour_label = ttk.Label(root, text="Hour:")
hour_label.grid(row=0, column=0, padx=5, pady=5)
hour_var = tk.StringVar()
hour_combo = ttk.Combobox(root, textvariable=hour_var, values=[str(i) for i in range(1, 13)])
hour_combo.grid(row=0, column=1, padx=5, pady=5)
hour_combo.current(0)

# Minute
minute_label = ttk.Label(root, text="Minute:")
minute_label.grid(row=0, column=2, padx=5, pady=5)
minute_var = tk.StringVar()
minute_combo = ttk.Combobox(root, textvariable=minute_var, values=[str(i).zfill(2) for i in range(60)])
minute_combo.grid(row=0, column=3, padx=5, pady=5)
minute_combo.current(0)

# AM/PM
ampm_label = ttk.Label(root, text="AM/PM:")
ampm_label.grid(row=0, column=4, padx=5, pady=5)
ampm_var = tk.StringVar()
ampm_combo = ttk.Combobox(root, textvariable=ampm_var, values=["AM", "PM"])
ampm_combo.grid(row=0, column=5, padx=5, pady=5)
ampm_combo.current(0)

# Button to get selected time
get_time_button = ttk.Button(root, text="Get Time", command=get_time)
get_time_button.grid(row=1, columnspan=6, padx=5, pady=5)

root.mainloop()
