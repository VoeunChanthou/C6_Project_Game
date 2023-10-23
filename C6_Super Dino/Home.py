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

# group_image----------------------
id_1 = PhotoImage(file='image/bg_home.png')
start_game = PhotoImage(file='image/play.png')
restart_game = PhotoImage(file='image/restart.png')
exit_game = PhotoImage(file='image/exit.png')



# home_bg-------------------------------

canvas.create_image(0,0,image=id_1, anchor=NW)
canvas_start = canvas.create_image(560,200, image=start_game, anchor=NW)
canvas_restart = canvas.create_image(560,330, image=restart_game, anchor=NW)
canvas_exit = canvas.create_image(560,460, image=exit_game, anchor=NW)









window.mainloop()