import tkinter as tk
import random

window = tk.Tk()

# window.attributes('-fullscreen', True)
window.geometry('600x500')
window.title('Gameplay')

# ---------------របៀបដាក់color----------------------------------
window.configure(bg="blue")

# ---------------មិនអាចបង្រីកបង្រួមបាន----------------------------
window.resizable(True, True)

# -----------Frameមាន canvas
frame = tk.Frame(window, width=400, height=400)
frame.pack()

canvas = tk.Canvas(frame)
canvas.pack()


# arr = ['red', 'blue', 'green', 'yellow', 'pink', 'white', 'black', 'teal']
# color = random.choice(arr)

# circle_id = canvas.create_oval(10, 10, 100, 100, fill='pink')
# rect_id = canvas.create_rectangle(110, 10, 200, 100, fill='blue')
# rect1_id = canvas.create_rectangle(210, 10, 300, 100, fill=color)


def redColor():
    canvas.itemconfig(circle_id, fill='red')
def blueColor():
    canvas.itemconfig(circle_id, fill='blue')



btn = tk.Button(frame, text="Click on me to change red", command = increaseNumber, bg='red')
btn.pack()

btn = tk.Button(frame, text="Click on me to change blue", command = blueColor)
btn.pack()


# -----button-change---------
# def changeColor():
#     canvas.itemconfig(circle_id, fill=random.choice(arr))
#     canvas.itemconfig(rect_id, fill=random.choice(arr))
    

# btn = tk.Button(frame, text="chick here", command=changeColor, bg='pink')
# btn.pack()

# canvas.itemconfig(circle_id, fill='green')
# canvas.itemconfig(rect1_id, fill='red')
# canvas.itemconfig(rect_id, fill='purple')

# canvas.create_rectangle(10, 10, 400, 50, fill='blue')
# canvas.create_rectangle(10, 60, 100, 140, fill=color)
# canvas.create_rectangle(110, 60, 200, 140, fill=color)
# canvas.create_rectangle(210, 60, 300, 140, fill='orange')
# canvas.create_rectangle(310, 60, 400, 140, fill='orange')
# canvas.create_rectangle(10, 150, 100, 230, fill= 'pink')
# canvas.create_rectangle(110, 150, 200, 230, fill= color)
# canvas.create_rectangle(210, 150, 300, 230, fill= 'pink')
# canvas.create_rectangle(310, 150, 400, 230, fill= 'pink')
# canvas.create_rectangle(10, 240, 100, 320, fill= color)
# canvas.create_rectangle(110, 240, 200, 320, fill= 'green')
# canvas.create_rectangle(210, 240, 300, 320, fill= color)
# canvas.create_rectangle(310, 240, 400, 320, fill= color)
# canvas.create_rectangle(10, 330, 400, 400, fill= 'yellow')

window.mainloop()


