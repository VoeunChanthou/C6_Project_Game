import tkinter as tk
import random

window = tk.Tk()
window.geometry('600x600')
window.title('Game')

frame=tk.Frame(window, width=700, height=600, bg='red')
frame.pack()
canvas=tk.Canvas(frame, width=510, height=510, bg='pink')
canvas.pack()

arr = ['red', 'blue', 'pink', 'green', 'purple', 'black', 'brown', 'orange', 'gray']
# def up(event):
#     canvas.itemconfig(r1, fill=random.choice(arr))
# window.bind('<Button-1>', up)


def change_color(event):
    x = canvas.canvasx(event.x)
    y = canvas.canvasy(event.y)
    shape_id = canvas.find_closest(x, y)
    canvas.itemconfig(shape_id, fill=random.choice(arr))

window.bind('<Button-1>', change_color)


r1=canvas.create_rectangle(10, 10, 100, 100, fill=random.choice(arr))
canvas.create_rectangle(110, 10, 200, 100, fill=random.choice(arr))
canvas.create_rectangle(210, 10, 300, 100, fill='yellow')
canvas.create_rectangle(310, 10, 400, 100, fill='yellow')
canvas.create_rectangle(410, 10, 500, 100, fill='yellow')

canvas.create_rectangle(10, 110, 100, 200, fill='yellow')
canvas.create_rectangle(10, 210, 100, 300, fill='yellow')
canvas.create_rectangle(10, 310, 100, 400, fill='yellow')
canvas.create_rectangle(10, 410, 100, 500, fill='yellow')


canvas.create_rectangle(110, 410, 200, 500, fill='yellow')
canvas.create_rectangle(210, 410, 300, 500, fill='yellow')
canvas.create_rectangle(310, 410, 400, 500, fill='yellow')
canvas.create_rectangle(410, 410, 500, 500, fill='yellow')


canvas.create_rectangle(410, 310, 500, 400, fill='yellow')
canvas.create_rectangle(410, 210, 500, 300, fill='yellow')
canvas.create_rectangle(410, 110, 500, 200, fill='yellow')

canvas.create_oval(210, 210, 300, 300, fill='red')



window.mainloop()