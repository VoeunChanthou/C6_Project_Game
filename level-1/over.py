from tkinter import *

window = Tk()
window.title('SUPER DINO')
WIDTH = 1350
HEIGHT = 670
window.geometry(f"{WIDTH}x{HEIGHT}+{0}+{0}")
frame = Frame(window)
frame.pack()
canvas=Canvas(frame, width=WIDTH, height=HEIGHT)
canvas.pack()


# group image
bg_over = PhotoImage(file='image/bg-win_over.png')
over = PhotoImage(file='image/text-over.png')
restart= PhotoImage(file='image/restart.png')
home= PhotoImage(file='image/home.png')
lose= PhotoImage(file='image/dino-lose.png')

# canvas

canvas.create_image(0,0,image=bg_over, anchor=NW)
canvas.create_image(180,0,image=over, anchor=NW)
canvas.create_image(430,480,image=home, )
canvas.create_image(850,480,image=restart,)
canvas.create_image(850,480,image=restart,)
canvas.create_image(650,380,image=lose,)


window.mainloop()