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
    message = "\n"
    root = tkinter.Tk()
    root.title("Instructions...")
    root.geometry("600x680")
    root.resizable(0, 0)
    root.configure(bg='#21272E')

    instructions = Frame(root, bg='#21272E')

    instructions_title_label = Label(instructions, text=message, font="none 5", bg="#21272E", fg="#21272E")
    instructions_title_label.pack(side=TOP)

    instructions_title_label = Label(instructions, text="Instructions", padx=15, pady=5, relief="ridge",
                                     font="none 22 bold", fg="white", bg="#33444E")
    instructions_title_label.pack(side=TOP)

    instructions_title_label = Label(instructions, text=message, font="none 5", bg="#21272E", fg="#21272E")
    instructions_title_label.pack(side=TOP)

    instructions.pack(side=TOP)

    step1 = Frame(root, bg='#21272E')

    step_label = Label(step1, text="Step1: Select Source", padx=15, pady=5, relief="ridge", font="none 14 bold",
                       fg="white", bg="#21272E")
    step_label.pack(side=TOP)

    instructions_label = Label(step1, text="Click LEFT MOUSE BUTTON.\n", font="none 13", fg="white", bg='#21272E')
    instructions_label.pack(side=TOP)

    step1.pack(side=TOP)

    step2 = Frame(root, bg='#21272E')

    step_label = Label(step2, text="Step2: Select Destination", padx=15, pady=5, relief="ridge", font="none 14 bold",
                       fg="white", bg="#21272E")
    step_label.pack(side=TOP)

    instructions_label = Label(step2, text="Click LEFT MOUSE BUTTON.\n", font="none 13", fg="white", bg='#21272E')
    instructions_label.pack(side=TOP)

    step2.pack(side=TOP)

    step3 = Frame(root, bg='#21272E')

    step_label = Label(step3, text="Step3: Select Obstacle.", padx=15, pady=5, relief="ridge", font="none 14 bold",
                       fg="white", bg="#21272E")
    step_label.pack(side=TOP)

    instructions_label = Label(step3, text="For Single Obstacle:", font="none 13 bold", fg="white", bg='#21272E')
    instructions_label.pack(side=TOP)

    instructions_label = Label(step3, text="Click LEFT MOUSE BUTTON.", font="none 13", fg="white", bg='#21272E')
    instructions_label.pack(side=TOP)

    instructions_label = Label(step3, text="For Multiple Obstacles:", font="none 13 bold", fg="white", bg='#21272E')
    instructions_label.pack(side=TOP)

    instructions_label = Label(step3, text="Click LEFT MOUSE BUTTON & Drag The CURSOR\n", font="none 13", fg="white",
                               bg='#21272E')
    instructions_label.pack(side=TOP)

    step3.pack(side=TOP)

    instructions.pack(side=TOP)

    start_search = Frame(root, bg='#21272E')

    step_label = Label(start_search, text="Start Search", padx=15, pady=5, relief="ridge", font="none 14 bold",
                       fg="white", bg="#21272E")
    step_label.pack(side=TOP)

    instructions_label = Label(start_search, text="SPACE\n", font="none 13", fg="white", bg='#21272E')
    instructions_label.pack(side=TOP)

    start_search.pack(side=TOP)

    step4 = Frame(root, bg='#21272E')

    step_label = Label(step4, text="Reset", padx=15, pady=5, relief="ridge", font="none 14 bold", fg="white",
                       bg="#21272E")
    step_label.pack(side=TOP)

    instructions_label = Label(step4, text="Reset All:", font="none 13 bold", fg="white", bg='#21272E')
    instructions_label.pack(side=TOP)

    instructions_label = Label(step4, text="BACKSPACE", font="none 13", fg="white", bg='#21272E')
    instructions_label.pack(side=TOP)

    instructions_label = Label(step4, text="Reset Single Grid:", font="none 13 bold", fg="white", bg='#21272E')
    instructions_label.pack(side=TOP)

    instructions_label = Label(step4, text="Click RIGHT MOUSE BUTTON Over Specific Square.", font="none 13", fg="white",
                               bg='#21272E')
    instructions_label.pack(side=TOP)

    instructions_label = Label(step4, text="Reset Multiple Grid:", font="none 13 bold", fg="white", bg='#21272E')
    instructions_label.pack(side=TOP)

    instructions_label = Label(step4, text="Click RIGHT MOUSE BUTTON & Drag The CURSOR.", font="none 13", fg="white",
                               bg='#21272E')
    instructions_label.pack(side=TOP)

    step4.pack(side=TOP)

    instructions.pack()
    root.mainloop()

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
