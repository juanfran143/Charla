import random


def executioner(names: str) -> None:
    name = random.choice(names)
    print(name + " has been executed")

"""
if __name__ == '__main__':
    names = ["Vero", "Peyman", "Elnaz", "Yuda", "Xabier"]
    executioner(names)
"""

import random
import tkinter as tk
from tkinter import messagebox

def executioner(names: str) -> None:
    name = random.choice(names)
    messagebox.showinfo("Execution", name + " has been executed")

if __name__ == '__main__':
    root = tk.Tk()
    root.withdraw()  # Oculta la ventana principal de tkinter
    names = ["Vero", "Peyman", "Elnaz", "Yuda", "Xabier"]
    executioner(names)

