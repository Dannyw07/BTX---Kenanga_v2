import tkinter as tk
import tkinter.ttk as tb
from tkinter import messagebox
import configparser


CONFIG_FILE  = "config.ini"

class ConfigurationTab:

    def __init__(self, master):
        self.master = master
        self.setup_gui()

    def save_to_config(self):
        config = configparser.ConfigParser()
        config.read(CONFIG_FILE)
        config['Time'] = {'Hour': self.hour_var.get(),
                          'Minute': self.minute_var.get(),
                          'AM/PM': self.ampm_var.get()}
        with open(CONFIG_FILE, 'w') as configfile:
            config.write(configfile)

    def setup_gui(self):
         # Create a frame for configuration elements
        self.frame = tb.Frame(self.master)
        self.frame.pack(fill=tk.BOTH, expand=True)

        # Example configuration elements
        self.label = tk.Label(self.frame, text="Configuration Options", font=("Helvetica", 16))
        self.label.pack(pady=10)

        # Frame for hour, minute, and AM/PM selection
        selection_frame = tb.LabelFrame(self.frame, text="Time 1")
        selection_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

        # Hour
        hour_label = tb.Label(selection_frame, text="Hour:")
        hour_label.grid(row=0, column=0, padx=5, pady=5)
        self.hour_var = tk.StringVar()
        hour_combo = tb.Combobox(selection_frame, textvariable=self.hour_var, values=[str(i) for i in range(1, 13)], width=3)
        hour_combo.grid(row=0, column=1, padx=5, pady=5)
        hour_combo.current(0)

        # Minute
        minute_label = tb.Label(selection_frame, text="Minute:")
        minute_label.grid(row=0, column=2, padx=5, pady=5)
        self.minute_var = tk.StringVar()
        minute_combo = tb.Combobox(selection_frame, textvariable=self.minute_var, values=[str(i).zfill(2) for i in range(60)], width=3)
        minute_combo.grid(row=0, column=3, padx=5, pady=5)
        minute_combo.current(0)

        # AM/PM
        ampm_label = tb.Label(selection_frame, text="AM/PM:")
        ampm_label.grid(row=0, column=4, padx=5, pady=5)
        self.ampm_var = tk.StringVar()
        ampm_combo = tb.Combobox(selection_frame, textvariable=self.ampm_var, values=["AM", "PM"], width=3)
        ampm_combo.grid(row=0, column=5, padx=5, pady=5)
        ampm_combo.current(0)

        
        # Button to get selected time
        save_button = tb.Button(self.frame, text="Save", 
            command=self.save_to_config,
            bootstyle = 'success',
            style= 'success.Tbutton',
            )
        save_button.pack(pady=5)
        
