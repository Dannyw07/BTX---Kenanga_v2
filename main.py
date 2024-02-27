from libraries import *
# Import the ConfigurationTab class from config.py
# from config import ConfigurationTab

class BTX:

    def update_message(self, message):
        # Update the message label text
        self.outputMsg.config(text=message)

    def is_internet_available(self):
        try:
            # Attempt to make a requet to google
            response = requests.get("http://www.google.com",timeout=5)
            response.raise_for_status()
            print("Internet connection is available.")
            return True
        except requests.RequestException as e:
            print("No internet connection. Error:", str(e))
            return False

    def handle_SocketError(self):
       try:
            # Check for internet connection
            if not self.is_internet_available():
                self.button_Disabled()
                print("No internet connection.")
                # Display a dialog box with the message
                messagebox.showinfo("Network Error Detected", "No internet connection. Please exit the program and configure your network.")
                
                return False
            return True
       except Exception as e:
                # Log other exceptions, if any
                print(f"Error in handle_SocketError: {str(e)}")
                return False

    def start_program(self):
        
        # Disable the Start and Stop buttons
        self.startBtn["state"] = tk.DISABLED
        self.endBtn["state"] = tk.DISABLED

        # Set the running flag to True
        self.running = True
        
        # Start the program in a separate thread
        self.program_thread = Thread(target=self.run_program)
        self.program_thread.start()

    def stop_program(self):

        # Set the running flag to False to stop the loop
        self.running = False
        print("The program stopped the checking process")
        self.update_message("The program stopped the checking process")
        self.outputMsg.after(2000, lambda: self.update_message("Ready"))
        # Additional cleanup tasks if needed
        self.startBtn["state"] = tk.NORMAL

    def run_program(self):
        try:
            # Enable the Stop button
            self.endBtn["state"] = tk.NORMAL
            print("The program started the checking process")
        
            # Check for socket error before proceeding
            if not self.handle_SocketError():
                self.startBtn["state"] = tk.NORMAL
                return
            
            # Initialize a flag to track if email has been sent for 4:30 am
            email_sent_430am = False
            # Initialize a flag to track if email has been sent for 5:45 am
            email_sent_545am = False
            # Initialize a flag to track if email has been sent for 6:30 am
            email_sent_630am = False
            # Initialize a flag to track if email has been sent for 7:00 am
            email_sent_700am = False

            # Keep running until the user presses the Stop button or the program stops
            while self.running:
                current_time = datetime.datetime.now().time()
                
                # Check if it's 4:30 AM
                if current_time.hour == 15  and current_time.minute == 26:
                    # Check if email for 5:45 AM has already been sent
                    if not email_sent_430am:
                        subprocess.run(["python", "one.py"])
                        messagebox.showinfo("Processing Ended", f"Processing for {current_time.hour}:{current_time.minute} AM has ended.")
                        email_sent_430am = True
                else:
                    # Reset email_sent_430am if the time is not 4:30 AM
                    email_sent_430am = False

                # Check if it's 5:45 AM
                if current_time.hour == 13 and current_time.minute == 59:
                    # Check if email for 5:45 AM has already been sent
                    if not email_sent_545am:
                        subprocess.run(["python", "two.py"])
                        messagebox.showinfo("Processing Ended", f"Processing for {current_time.hour}:{current_time.minute} AM has ended.")
                        email_sent_545am = True
                else:
                    # Reset email_sent_545am if the time is not 5:45 AM
                    email_sent_545am = False

                # Check if it's 6:30 AM
                if current_time.hour == 14 and current_time.minute == 15:
                    # Check if email for 6:30 AM has already been sent
                    if not email_sent_630am:
                        subprocess.run(["python", "three.py"])
                        messagebox.showinfo("Processing Ended", f"Processing for {current_time.hour}:{current_time.minute} AM has ended.")
                        email_sent_630am = True
                else:
                    # Reset email_sent_545am if the time is not 5:45 AM
                    email_sent_630am = False

                # Check if it's 7:00 AM
                # if current_time.hour == 13 and current_time.minute == 1:
                if current_time.hour == 15 and current_time.minute == 20:
                    # Check if email for 7:00 AM has already been sent
                    if not email_sent_700am:
                        subprocess.run(["python", "four.py"])
                        messagebox.showinfo("Processing Ended", f"Processing for {current_time.hour}:{current_time.minute} AM has ended.")
                        email_sent_700am = True
                else:
                    # Reset email_sent_700am if the time is not 7:00 AM
                    email_sent_700am = False

                print('waiting...')
                self.update_message('Waiting...')
                # If neither of the conditions are met, wait for 5 seconds
                time.sleep(5)
        
        except TimeoutError as e:
            print(f"TimeoutError occurred in run_program: {e}")
            # Additional handling for the timeout error, such as logging the error or notifying the user.
            # You can also add a messagebox here to inform the user about the timeout error.
            messagebox.showerror("Timeout Error", "A timeout error occurred. Please check your internet connection and try again.")
        
        finally:
        # Enable the Start button after stopping
            self.startBtn["state"] = tk.NORMAL

    def setup_gui(self):
        # Create a notebook (tabbed interface)
        self.tabControl = tb.Notebook(self.master)
        self.tabControl.pack(expand=True, fill='both')

        self.tab1 = tb.Frame(self.tabControl)
        self.tabControl.add(self.tab1, text='Main')

        # Configuration tab
        # self.tab2 = tb.Frame(self.tabControl)
        # self.tabControl.add(self.tab2, text='Configuration')

        # Create an instance of ConfigurationTab and pass the tab2 frame as the master
        # self.configuration_tab = ConfigurationTab(self.tab2)

        frame4 = tk.Frame(self.tab1, borderwidth=2)
        frame4.pack(side="top", padx=10, pady=30)
        self.outputMsg = tk.Label(frame4, text="")
        self.outputMsg.pack(padx=10)

        frame5 = tk.Frame(self.tab1, borderwidth=2)
        frame5.pack(side="top", padx=30)
        my_style = tb.Style()
        my_style.configure('success.TButton', font=("Helvetica", 18))
        my_style.configure('danger.TButton', font=("Helvetica", 18))

        self.startBtn = tb.Button(frame5, text="Start", 
            command=self.start_program,
            bootstyle="success",
            style="success.Tbutton",
            width=10)
        self.startBtn.pack(pady=40)

        frame6 = tk.Frame(self.tab1, borderwidth=2)
        frame6.pack(side="top", padx=10, pady=30)
        self.displayMsg = tk.Label(frame6, text="")
        self.displayMsg.pack(padx=10)

        self.endBtn = tb.Button(frame5, text="End", 
            command=self.stop_program,
            bootstyle="danger",
            style="danger.Tbutton",
            width=10)
        self.endBtn.pack(pady=0)

        self.footer_label = tk.Label(self.master, text="Danny Wong Jia Hong © 2024  ", bd=1, anchor=tk.W)
        self.footer_label.pack(side=tk.BOTTOM, fill=tk.X)

        self.width_limit = 350
        self.height_limit = 450
        self.master.geometry(f"{self.width_limit}x{self.height_limit}")

    def __init__(self, master):
        self.master = master
        self.master.title("BTX Email Monitoring")
        self.setup_gui()
        # root.after(1000, self.check_message_queue)  # Check the queue every 1 second (adjust the time interval as needed)
        # Bind an event to check and prevent resizing
        self.master.bind("<Configure>", self.check_resize)
       
        
    def check_resize(self, event):
        current_width = self.master.winfo_width()
        current_height = self.master.winfo_height()

        # Check if the width exceeds the limit
        if current_width > self.width_limit:
            self.master.geometry(f"{self.width_limit}x{current_height}")

        # Check if the height exceeds the limit
        if current_height > self.height_limit:
            self.master.geometry(f"{current_width}x{self.height_limit}")


if __name__ == "__main__":
    root = tb.Window(themename="cosmo")
    app = BTX(root)
    root.mainloop()
