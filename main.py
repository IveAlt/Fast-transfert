import tkinter as tk
import subprocess
import os

desktop_path = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')

root = tk.Tk()
root.title('Fast Transfert')
root.geometry('725x200')

IP1 = tk.StringVar()
IP2 = tk.StringVar()
user = tk.StringVar()
user2 = tk.StringVar()
same_user = tk.IntVar()

tk.Label(root, text='Entrer IP Poste 1 :').grid(row=0, column=0)
tk.Entry(root, textvariable=IP1).grid(row=0, column=1)

tk.Label(root, text='Utilisateur  :').grid(row=1, column=0)
tk.Entry(root, textvariable=user).grid(row=1, column=1)

user2_label = tk.Label(root, text='Utilisateur 2 :')
user2_label.grid(row=2, column=0)
user2_entry = tk.Entry(root, textvariable=user2)
user2_entry.grid(row=2, column=1)

tk.Label(root, text='Entrer IP Poste 2 :').grid(row=0, column=2)
tk.Entry(root, textvariable=IP2).grid(row=0, column=3)

Bureau = tk.IntVar()
Documents = tk.IntVar()
Téléchargement = tk.IntVar()

tk.Checkbutton(root, text='Bureau', variable=Bureau).place(relx=.3, rely=.1)
tk.Checkbutton(root, text='Documents', variable=Documents).place(relx=.3, rely=.2)
tk.Checkbutton(root, text='Téléchargement', variable=Téléchargement).place(relx=.3, rely=.3)

def toggle_user2():
    if same_user.get():
        user2_entry.grid_remove()
        user2_label.grid_remove()
    else:
        user2_entry.grid()
        user2_label.grid()

tk.Checkbutton(root, text='Même Utilisateur', variable=same_user, command=toggle_user2).place(relx=.0, rely=.4)

subprocesses = []

def long_running_task():
    log_file_path = os.path.join(desktop_path, 'logfile.txt')

    with open(log_file_path, 'w') as f:
        if same_user.get():
            user2.set(user.get())
        filetrsf_process = subprocess.Popen(
            ['python', 'filetrsf.py', IP1.get(), user.get(), user2.get(), IP2.get(), str(Bureau.get()), str(Documents.get()), str(Téléchargement.get())],
            stdout=f,
            stderr=subprocess.STDOUT,
            bufsize=1,
            universal_newlines=True
        )
        subprocesses.append(filetrsf_process)

    terminal_process = subprocess.Popen(['python', 'terminal.py', log_file_path])
    subprocesses.append(terminal_process)

def on_closing():
    for p in subprocesses:
        p.terminate()
    root.destroy()

tk.Button(root, text='Copié', command=long_running_task).grid(row=6, column=1)

root.protocol("WM_DELETE_WINDOW", on_closing)

# Run the main loop
root.mainloop()
