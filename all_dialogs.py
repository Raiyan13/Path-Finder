import tkinter
from tkinter import messagebox
from tkinter import *

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
    root = tkinter.Tk()
    root.title("Credits...")
    root.geometry("500x300")
    root.resizable(0, 0)
    root.configure(bg='coral1')

    frame = Frame(root, bg='gray12')

    main_menu_lbl = Label(frame, text="Creators...\n\nS.m. Tahmin Kabir Raiyan\n&\nHillol Talukdar", padx=52, pady=45, font="none 20 bold", bg='gray12', fg='coral1')
    main_menu_lbl.pack(side=TOP)

    frame.pack(side=TOP)
    frame.place(x=23, y=22)

    root.mainloop()
