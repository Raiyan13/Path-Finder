from tkinter import *

root = Tk()

root.title("Path Finder...")
root.geometry("700x550")
root.resizable(0,0)
root.configure(bg='gray12')


def instructions_btn_clck():
    pass

def start_btn_clck():
    pass

def credits_btn_clck():
    pass


frm_top = Frame(root)

main_menu_lbl = Label(frm_top, text="Main Menu", font="none 40 bold")
main_menu_lbl.pack(side=LEFT)

frm_top.pack(side = TOP)


frm_mid = Frame(root)

instructions_btn = Button(frm_mid, text="Instructions", font=15, width=20, height=1, command = "instructions_btn_clck")
instructions_btn.pack(side = LEFT)

frm_mid.pack(side= LEFT)


frm_mid_right = Frame(root , bg="midnight blue")

# instructions_lbl = Label(frm_mid_right, text='''Source color= CYAN
#                                           \nDestination color = MAGENTA
#                                           \nOBSTACLES color = RED
#                                           \nSHORTEST PATH color = GREEN
#                                           \nVISITED NODE color = WHITE
#                                           \nNext possible way color = GRAY''', font="node 10 bold")
# instructions_lbl.pack(side= RIGHT)

instructions_lbl = Label(frm_mid_right, text="Source color= CYAN", fg="cyan", bg="midnight blue")
instructions_lbl.pack(side= TOP)
instructions_lbl = Label(frm_mid_right, text="Destination color = MAGENTA", fg="Magenta", bg="midnight blue")
instructions_lbl.pack(side= TOP)
instructions_lbl = Label(frm_mid_right, text="Obstacle color = RED", fg="red", bg="midnight blue")
instructions_lbl.pack(side= TOP)
instructions_lbl = Label(frm_mid_right, text="Shortest Path color = Lime", fg="lime", bg="midnight blue")
instructions_lbl.pack(side= TOP)
instructions_lbl = Label(frm_mid_right, text="Visited Node color = WHITE", fg="WHITE", bg="midnight blue")
instructions_lbl.pack(side= TOP)
instructions_lbl = Label(frm_mid_right, text="Next Possible Way color = GRAY", fg="gray", bg="midnight blue")
instructions_lbl.pack(side= TOP)

frm_mid_right.pack(side=RIGHT)


frm_bottom = Frame(root)

start_btn = Button(frm_bottom, text="Start", font=15, width=20, height=1, command = "start_btn_clck")
start_btn.pack(side=LEFT)
credits_btn = Button(frm_bottom, text="Credits", font=15, width=20, height=1, command = "credits_btn_clck")
credits_btn.pack(side=LEFT)

frm_bottom.pack(side=BOTTOM)

root.mainloop()
