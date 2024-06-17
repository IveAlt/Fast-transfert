import os
import sys
import ctypes
import subprocess
from tkinter import messagebox


def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

if is_admin():
    IP1 = sys.argv[1]
    user = sys.argv[2]
    user2 = sys.argv[3]
    IP2 = sys.argv[4]
    Desktop = bool(int(sys.argv[5]))
    Documents = bool(int(sys.argv[6]))
    Downloads = bool(int(sys.argv[7]))

    pathdesktop = f"\\\\{IP1}\\C$\\Users\\{user}\\Desktop"
    pathdocuments = f"\\\\{IP1}\\C$\\Users\\{user}\\Documents"
    pathdownloads = f"\\\\{IP1}\\C$\\Users\\{user}\\Downloads"

    dest_desktop = f"\\\\{IP2}\\C$\\Users\\{user2}\\Desktop"
    dest_documents = f"\\\\{IP2}\\C$\\Users\\{user2}\\Documents"
    dest_downloads = f"\\\\{IP2}\\C$\\Users\\{user2}\\Downloads"

    try:
        if os.path.exists(pathdesktop) and Desktop:
            subprocess.call(['robocopy', pathdesktop, dest_desktop, '/E', '/MT:6', '/XO'])
        if os.path.exists(pathdocuments) and Documents:
            subprocess.call(['robocopy', pathdocuments, dest_documents, '/E', '/MT:6', '/XO'])
        if os.path.exists(pathdownloads) and Downloads:
            subprocess.call(['robocopy', pathdownloads, dest_downloads, '/E', '/MT:6', '/XO'])

        print("Transfer Complete")

    except Exception as e:
        messagebox.showerror("Error", str(e))
        print(f"Error: {e}")

else:

    ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, " ".join(sys.argv), None, 1)
