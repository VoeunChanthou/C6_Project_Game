import tkinter as tk
from PIL import Image, ImageTk

window = tk.Tk()
window.title("Image Viewer")
window.geometry("600x500")

frame = tk.Frame(window, width=600, height=400)
frame.pack()

canvas = tk.Canvas(frame, width=500, height=400, bg="white")
canvas.pack(pady=20)

# Image 1
file_1 = Image.open('1.png')
file_1_size = file_1.resize((100, 100))
img_1 = ImageTk.PhotoImage(file_1_size)
canvas.create_image(50, 50, image=img_1, )

# Text
canvas.create_text(250, 200, text="Football Game", font=("Robus", 60, "bold"), fill="purple")




window.resizable(0, 0)
window.mainloop()