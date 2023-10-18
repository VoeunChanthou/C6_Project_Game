


import tkinter as tk
import random

window = tk.Tk()
window.geometry('1024x600')
window.title('Game')
window.resizable(False, False)


frame=tk.Frame(window, width=1024, height=600, bg='red')
frame.pack()
canvas=tk.Canvas(frame, width=1024, height=600, bg='pink')
canvas.pack()
canvas.create_text(540, 60, text="Play Game", fill="black", font=('Helvetica 15 bold', 35, 'bold'))

canvas.create_rectangle(150, 250, 300, 270, fill='red')
canvas.create_rectangle(350, 250, 500, 270, fill='red')
canvas.create_rectangle(550, 250, 700, 270, fill='red')
canvas.create_rectangle(700, 120, 720, 270, fill='red')
canvas.create_oval(660, 210, 700, 250, fill='green')
canvas.create_rectangle(10, 350, 200, 390, fill='black')
canvas.create_rectangle(250, 350, 440, 390, fill='black')
canvas.create_oval(10, 310, 50, 350, fill='green')
canvas.create_rectangle(80, 330, 280, 350, fill='green')
canvas.create_oval(10, 550, 50, 590, fill='green')
canvas.create_rectangle(80, 570, 280, 590, fill='green')
canvas.create_rectangle(150, 530, 350, 550, fill='green')
canvas.create_rectangle(250, 490, 450, 510, fill='green')
canvas.create_rectangle(480, 450, 520, 600, fill='green')
canvas.create_rectangle(550, 370, 590, 600, fill='green')

window.mainloop()