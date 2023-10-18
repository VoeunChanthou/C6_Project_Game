
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

canvas.create_rectangle(30, 470, 120, 600, fill='red')
canvas.create_oval(40, 390, 110, 460, fill='red')
canvas.create_rectangle(250, 470, 340, 600, fill='red')
canvas.create_rectangle(380, 340, 470, 600, fill='red')
canvas.create_rectangle(120, 170, 380, 250, fill='red')
canvas.create_rectangle(600, 150, 800, 230, fill='red')
window.mainloop()