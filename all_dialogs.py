import tkinter
from tkinter import messagebox

parent = tkinter.Tk()
parent.overrideredirect(1)
parent.withdraw()


def show_info(info_title, message):
    messagebox.showinfo(info_title, message, parent=parent)
    return

def show_warning(warning_title, message):
    messagebox.showwarning(warning_title, message, parent=parent)
    return

def show_error(error_title, message):
    messagebox.showerror(error_title, message, parent=parent)
    return

def show_instructions():
    pass

def show_credits():
    pass
