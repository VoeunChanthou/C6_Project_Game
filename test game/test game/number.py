import tkinter as tk


window = tk.Tk()
window.geometry("400x500")
window.title("Hello World")

frame = tk.Frame(window,width=400, height=500)
frame.pack()
canvas = tk.Canvas(frame)
canvas.pack()
total = 0

canvas.create_rectangle(10, 10, 100,100)
result = canvas.create_text(55, 60, text="0", fill="red", font=("bold", 60))

def increament():
    global total
    total += 1
    canvas.itemconfig(result, text = total)

def increament1():
    global total
    total -= 1
    canvas.itemconfig(result, text = total)

btn = tk.Button(frame, text='click (+)', command=increament)
btn.pack()

btn1 = tk.Button(frame, text='click (-)', command=increament1)
btn1.pack()

window.mainloop()