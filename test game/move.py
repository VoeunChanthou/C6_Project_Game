

import tkinter as tk
import time
from PIL import Image, ImageTk



window = tk.Tk()
window.geometry('1300x600')
# window.attributes('-fullscreen', True)d
window.title('Event')
window.resizable(0,0)

#frame
frame = tk.Frame(window)
frame.pack()



#canvas
canvas = tk.Canvas(frame, width=1700, height=600, bg='gray')
canvas.pack()



# ---------------------------------------------Image-------------------------------------------------------

bullet = Image.open('Img/bullet.png')
bullet_size = bullet.resize((20, 20))
bullet_1 = ImageTk.PhotoImage(bullet_size)

boom = Image.open('Img/exp3.png')
boom_size = boom.resize((100, 100))
boom_1 = ImageTk.PhotoImage(boom_size)

enermy = Image.open('Img/enermy.png')
enermy_size = enermy.resize((80, 80))
enermy_1 = ImageTk.PhotoImage(enermy_size)

sky = Image.open('Img/sky_cloud.png')
sky_size = sky.resize((2600, 600))
sky_1 = ImageTk.PhotoImage(sky_size)

forest = Image.open('Img/pine1.png')
forest_size = forest.resize((2600, 200))
forest_1 = ImageTk.PhotoImage(forest_size)

bg = Image.open('Img/mountain.png')
bg_size = bg.resize((2600, 500))
bg_1 = ImageTk.PhotoImage(bg_size)

Img_1= Image.open('Img/0.png')
Img_1_size = Img_1.resize((80,80))
Img_2 = ImageTk.PhotoImage(Img_1_size)


Img_down = Image.open('Img/2.png')
Img_down_size = Img_down.resize((80, 80))
Img_down_2 = ImageTk.PhotoImage(Img_down_size)

Img_right = Image.open('Img/1.png')
Img_right_size = Img_right.resize((80, 80))
Img_right_2 = ImageTk.PhotoImage(Img_right_size)


Img_left = Image.open('Img/3.png')
Img_left_size = Img_left.resize((80, 90))
Img_left_2 = ImageTk.PhotoImage(Img_left_size)
# -------------------------------------------------------------------------------------------------------------------#

id_3 = canvas.create_image(0, 300, image = sky_1)
id_1 = canvas.create_image(0, 580, image = bg_1)
id_2 = canvas.create_image(0, 560, image = forest_1)
id = canvas.create_image(50, 560, image = Img_2)
id_5 = canvas.create_image(700, 560, image = enermy_1)





def moveRight():
    if canvas.coords(id)[0] < 1290:
        canvas.move(id, +10, 0)
def moveLeft():
    if canvas.coords(id)[0] >60:
        canvas.move(id, -10, 0)
        canvas.itemconfig(id, image = Img_2)
def moveUp():
    if canvas.coords(id)[1] > 500:
        canvas.move(id, 0, -10)
        canvas.itemconfig(id, image = Img_2)
def moveDown():
    if canvas.coords(id)[1] < 550:
        canvas.move(id, 0, +10)
        canvas.itemconfig(id, image = Img_2)
def shoot():
    x = canvas.coords(id)[0] + 50
    y = canvas.coords(id)[1] 
    kk = canvas.create_image(x+10, y+10, image = bullet_1)
    while canvas.coords(kk)[0] < canvas.coords(id_5)[0]: 
        canvas.move(kk, +10, 0)
        window.update()
        time.sleep(0.02)
    canvas.itemconfig(kk, image=boom_1)
def deleteB():
    global kk
    canvas.delete('kk')




def move(event):
    if event.keysym == "d":
        moveRight()
        canvas.itemconfig(id, image = Img_left_2)
            
    elif event.keysym == 'a':
        moveLeft()
    elif event.keysym == 'w':
        moveUp()
    elif event.keysym == 's':
        moveDown()
    if event.keysym == 'f':
        canvas.itemconfig(id, image=Img_right_2)
    if event.keysym == 'j':
        shoot()
        deleteB()
    if event.keysym == 'e':
        deletei()
        
window.bind('<Key>', move)

# btn = tk.Button(frame, text='delete', command=eraser)
# btn.place(x=10, y=10)

window.bind('<Right>')

window.mainloop()