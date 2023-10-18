import tkinter as tk
from tkinter import colorchooser
import random 

color_draw = 'red'
color = ['red', 'blue', 'pink', 'black', 'purple', 'yellow', 'orange', 'green', 'brown']

def draw(event):
    
    canvas.create_oval(event.x - 10, event.y-10, event.x+20, event.y+20, fill=color_draw, outline='')

def eraser():
    canvas.delete("all")


def choose_color():
    global color_draw
    color_draw = colorchooser.askcolor()[1]

window = tk.Tk()
window.title('Draw Picture')
window.geometry('1000x600')


frame = tk.Frame(window, width=1000, height=600)
frame.pack()

color = tk.Button(frame, text='choose color', command=choose_color)
color.place(x=10, y=10)

btn = tk.Button(frame, text='Click on me', command=eraser)
btn.pack()


canvas = tk.Canvas(frame, width=1000, height=600, bg='pink')
canvas.pack(pady=30)


canvas.bind('<B1-Motion>', draw)


window.mainloop()