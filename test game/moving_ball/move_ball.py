from tkinter import *


tk = Tk()
tk.title("Moving Ball")
tk.resizable(0,0)


#----------create canvas and ball------
WIDTH = 400
HEIGHT = 300
canvas = Canvas(tk, width=WIDTH, height=HEIGHT)
canvas.pack()


ball = canvas.create_oval(10, 10, 50, 50, fill='black')


# ----move the ball-----
x = 3
y = 3

def moveball():
    global x
    global y

    canvas.move(ball, x, y)

    (leftPos, topPos, rightPos, bottomPos) = canvas.coords(ball)
    if leftPos <= 0 or rightPos>=WIDTH:
        x = -x
    if topPos <= 10 or bottomPos >= HEIGHT:
        y = -y
    
    canvas.after(30, moveball)
canvas.after(30, moveball)
tk.mainloop()