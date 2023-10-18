import tkinter as tk

window = tk.Tk()
window.geometry('600x400')
window.title('Event')

#frame
frame = tk.Frame(window, width=600, height=400)
frame.pack()

#canvas
canvas = tk.Canvas(frame, width=600, height=400, bg="pink")
canvas.pack()

id = canvas.create_rectangle(10, 10, 100, 100, fill='red')


def change_color(event):
    if event.keysym == 'w':
        canvas.itemconfig(id, fill='green')
    elif event.keysym == 'd':
        canvas.itemconfig(id, fill='blue')
    elif event.keysym == 's':
        canvas.itemconfig(id, fill='black')
    elif event.keysym == 'a':
        canvas.itemconfig(id, fill='orange')
    elif event.keysym == 't':
        canvas.create_text(200, 60, text='I LOVE YOU')

window.bind('<Key>', change_color)




window.bind('<Right>')

window.mainloop()