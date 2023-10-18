import tkinter as tk
import time
window=tk.Tk()
window.geometry('600x400')
frame=tk.Frame(window, width=600, height=400)
frame.pack()
canvas=tk.Canvas(frame, width=600, height=400)
canvas.pack()

id = canvas.create_text(150, 150, text='10:10:10', font=('bold', 20))

def clock():
    hour = time.strftime('%H: %M: %S')
    canvas.itemconfigure(id, text=hour)
def updateTime():
    clock()
    window.after(1000, updateTime)


window.after(1000, updateTime)
window.mainloop()