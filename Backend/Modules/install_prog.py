from os import chdir,mkdir,makedirs
from tkinter import filedialog

def install_mff():
    filename = filedialog.askdirectory()
    chdir(filename)



s=install_mff()
