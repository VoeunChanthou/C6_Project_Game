

import tkinter as tk


window = tk.Tk()
window.geometry("400x500")
window.title("Hello World")

frame = tk.Frame(window,width=400, height=500)
frame.pack()
canvas = tk.Canvas(frame, width=500, height=500, bg='purple')
canvas.pack()


# result = canvas.create_rectangle(10, 10, 100, 100, fill='red')
for i in range(1, 10):
    for j in range(1, 10):
        canvas.create_rectangle(10 + i * 100, 10 + j*100, 100 + i * 100, 100+j*100, fill='red')





window.mainloop()