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
bg_win = PhotoImage(file='image/bg-win_over.png')
win = PhotoImage(file='image/text-win.png')
next= PhotoImage(file='image/next.png')
home= PhotoImage(file='image/home.png')
dino_win= PhotoImage(file='image/dino-win.png')

# canvas

canvas.create_image(0,0,image=bg_win, anchor=NW)
canvas.create_image(180,0,image=win , anchor=NW)
canvas.create_image(430,480,image=home, )
canvas.create_image(850,480,image=next,)
canvas.create_image(650,320,image=dino_win,)


window.mainloop()