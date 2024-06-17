import os
import tkinter as tk
import threading
import time

class AutoUpdatingTextbox:
    def __init__(self, root, file_path, update_interval):
        self.root = root
        self.file_path = file_path
        self.update_interval = update_interval

        self.textbox = tk.Text(root)
        self.textbox.pack()

        self.update_textbox()

    def update_textbox(self):
        with open(self.file_path, 'rb') as file:  
            content = file.read().decode('utf-8-sig', errors='replace')  

        self.textbox.delete('1.0', tk.END)
        self.textbox.insert(tk.END, content)
        self.textbox.see(tk.END)  # Scroll to the end of the textbox

        self.root.after(self.update_interval * 1000, self.update_textbox)




# Usage
root = tk.Tk()
desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")
file_path = os.path.join(desktop_path, 'logfile.txt')
textbox = AutoUpdatingTextbox(root, file_path, 1)  # Update every 2 seconds
root.mainloop()
