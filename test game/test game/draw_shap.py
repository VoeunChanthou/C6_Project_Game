import tkinter as tk
import random

window = tk.Tk()
window.geometry('600x600')
window.title('Game')
window.resizable(False, False)

frame=tk.Frame(window, width=700, height=600, bg='red')
frame.pack()
canvas=tk.Canvas(frame, width=510, height=510, bg='pink')
canvas.pack()

arr = ['black', 'pink', 'yellow', 'orange', 'green', 'purple']

def change_color(event):
    x = canvas.canvasx(event.x)
    y = canvas.canvasy(event.y)
    id = canvas.find_closest(x, y)
    canvas.itemconfig(id, fill=random.choice(arr))
window.bind('<Button-1>', change_color)

# canvas.create_rectangle(410, 10, 500, 100, fill="red")
# canvas.create_oval(310, 110, 400, 200, fill="red")
# canvas.create_oval(210, 210, 300, 300, fill="red")
# canvas.create_oval(110, 310, 200, 400, fill="red")
# canvas.create_rectangle(10, 410, 100, 500, fill="red")

# canvas.create_rectangle(10, 10, 100, 100, fill='yellow')
# canvas.create_oval(110, 110, 200, 200, fill='yellow')
# canvas.create_oval(310, 310, 400, 400, fill='yellow')
# canvas.create_rectangle(410, 410, 500, 500, fill='yellow')


# canvas.create_oval(100, 50, 160, 130, fill='red')
# canvas.create_oval(360, 50, 420, 130, fill='red')
# canvas.create_rectangle(250, 100, 280, 210, fill='blue')
# canvas.create_rectangle(230, 210, 300, 260, fill='blue')

# canvas.create_oval(100, 250, 120, 270, fill='red' )
# canvas.create_oval(120, 270, 140, 290, fill='red' )
# canvas.create_oval(140, 290, 160, 310, fill='red' )
# canvas.create_oval(160, 310, 180, 330, fill='red' )
# canvas.create_oval(180, 310, 200, 330, fill='red' )
# canvas.create_oval(200, 310, 220, 330, fill='red' )
# canvas.create_oval(220, 310, 240, 330, fill='red' )
# canvas.create_oval(240, 310, 260, 330, fill='red' )
# canvas.create_oval(260, 310, 280, 330, fill='red' )
# canvas.create_oval(280, 310, 300, 330, fill='red' )
# canvas.create_oval(300, 310, 320, 330, fill='red' )
# canvas.create_oval(320, 310, 340, 330, fill='red' )
# canvas.create_oval(340, 290, 360, 310, fill='red' )
# canvas.create_oval(360, 270, 380, 290, fill='red' )
# canvas.create_oval(380, 250, 400, 270, fill='red' )

window.mainloop()