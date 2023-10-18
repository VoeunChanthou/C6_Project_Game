import tkinter as tk
from PIL import Image, ImageTk
window = tk.Tk()
window.title('Image')
# window.geometry('1024x600')
window.attributes('-fullscreen', True)

frame = tk.Frame(window, width=1024, height=600)
frame.pack()


#put.image
getImageFile = Image.open('Img/295839.jpg')

#convert image
img = ImageTk. PhotoImage(getImageFile)

#canvas
label = tk.Label(frame, image=img)
label.pack()

window.resizable(0, 0)
window.mainloop()
