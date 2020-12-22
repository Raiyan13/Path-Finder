from tkinter import *
from all_dialogs import show_credits, show_instructions
root = Tk()

root.title("Path Finder...")
root.geometry("700x550")
root.resizable(0, 0)
root.configure(bg='gray12')

def instructions_button_click():
    show_instructions()

def start_button_click():
    pass

def credit_button_click():
    show_credits()


frm_top = Frame(root)

main_menu_lbl = Label(frm_top, text="Path Finder", padx=30, font="none 40 bold", fg="white", bg='GRAY')
main_menu_lbl.pack(side=LEFT)

frm_top.pack(side=TOP)
frm_top.place(x=180, y=50)

frm_mid = Frame(root, bg="gray12")

start_btn = Button(frm_mid, text="Start", font="none 14 bold", width=15, height=1, command=start_button_click)
start_btn.pack(side=TOP, fill=X)

instructions_btn = Button(frm_mid, text="Instructions", font="none 14 bold", width=20, height=1, command=instructions_button_click)
instructions_btn.pack(side=TOP, fill=X)

credits_btn = Button(frm_mid, text="Credits", font="none 14 bold", width=15, height=1, command=credit_button_click)
credits_btn.pack(side=TOP, fill=X)

frm_mid.pack(side=TOP)
frm_mid.place(x=230, y=180)

frm_mid_right = Frame(root, bg="gray12")
instructions_lbl = Label(frm_mid_right, text="Game Indicator Colors", font="none 16 bold", fg="white", bg="gray12")
instructions_lbl.pack(side=TOP)
instructions_lbl = Label(frm_mid_right, text="Source Color = CYAN", font="none 10", fg="cyan", bg="gray12")
instructions_lbl.pack(side=TOP)

instructions_lbl = Label(frm_mid_right, text="Obstacle Color = RED", font="none 10", fg="red", bg="gray12")
instructions_lbl.pack(side=TOP)
instructions_lbl = Label(frm_mid_right, text="Shortest Path Color = LIME", font="none 10", fg="lime", bg="gray12")
instructions_lbl.pack(side=TOP)
instructions_lbl = Label(frm_mid_right, text="Visited Node Color = WHITE", font="none 10", fg="WHITE", bg="gray12")
instructions_lbl.pack(side=TOP)
instructions_lbl = Label(frm_mid_right, text="Destination Color = MAGENTA", font="none 10", fg="Magenta", bg="gray12")
instructions_lbl.pack(side=TOP)
instructions_lbl = Label(frm_mid_right, text="Next Possible Node Color = GRAY", font="none 10", fg="gray", bg="gray12")
instructions_lbl.pack(side=TOP)

frm_mid_right.pack(side=TOP)
frm_mid_right.place(x=242, y=350)

root.mainloop()
