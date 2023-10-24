from tkinter import *

screen = Tk()
screen.title('Level_2')
WIDTH = 1350
HEIGHT = 670
screen.geometry(f"{WIDTH}x{HEIGHT}+{0}+{0}")
frame = Frame(screen)
frame.pack()
canvas=Canvas(frame, width=WIDTH, height=HEIGHT, scrollregion= (0,0,4000,5000))
canvas.pack()

# ------------- Constants ---------------------
GRAVITY_FORCE = 9
JUMP_FORCE = 25
SPEED = 4

TIMED_LOOP = 15

# ------------- Variables ---------------------
keyPressed = []

# group_image----------------------
dino = PhotoImage(file='image/photo_2023-10-20_10-09-36-removebg-preview 1.png')
level2_bg = PhotoImage(file='level2_img/renfores 1.png')
level2_bg1 = PhotoImage(file='level2_img/renfores 2.png')
ground = PhotoImage(file='level2_img/ground.png')
water = PhotoImage(file='level2_img/water.png')
turtle_enermey = PhotoImage(file='image/turtle.png')
turtle_enermey_2 = PhotoImage(file='image/turtle_2.png')
bird_1 = PhotoImage(file='image/bird.png')
bird_2 = PhotoImage(file='image/bird_2.png')
challenges_ground_1 = PhotoImage(file='level2_img/challenge1.png')
challenges_ground_2 = PhotoImage(file='level2_img/challenge2.png')
challenges_ground_3 = PhotoImage(file='level2_img/challenge3.png')
challenges_ground_4 = PhotoImage(file='level2_img/challenge4.png')
dino_egg = PhotoImage(file='image/dino_egg-removebg-preview 1.png')
trap = PhotoImage(file='image/trap.png')
coin = PhotoImage(file='image/coin.png')
dino_nest = PhotoImage(file='image/nest.png')
dino_challenges1 = PhotoImage(file='level2_img/dino_challenge1.png')
dino_challenges2 = PhotoImage(file='level2_img/dino_challenge2.png')

# home_bg-------------------------------


canvas_bg_level3 = canvas.create_image(0,0,image=level2_bg,anchor=NW)
canvas_bg_level3 = canvas.create_image(1350,0,image=level2_bg1,anchor=NW)
canvas_bg_level3 = canvas.create_image(2350,0,image=level2_bg,anchor=NW)
canvas_bg_level3 = canvas.create_image(3700,0,image=level2_bg1,anchor=NW)

canvas_water = canvas.create_image(550,545,image=water, anchor=NW)
canvas_water = canvas.create_image(2200,545,image=water, anchor=NW)

canvas_ground = canvas.create_image(0,545,image=ground, anchor=NW, tags="PLATFORM")
canvas_ground = canvas.create_image(1100,545,image=ground, anchor=NW, tags="PLATFORM")
canvas_ground = canvas.create_image(1650,545,image=ground, anchor=NW, tags="PLATFORM")
canvas_ground = canvas.create_image(2750,545,image=ground, anchor=NW, tags="PLATFORM")
canvas_ground = canvas.create_image(3300,545,image=ground, anchor=NW, tags="PLATFORM")
canvas_ground = canvas.create_image(3700,545,image=ground, anchor=NW, tags="PLATFORM")

id_1 = canvas.create_image(0, 400, image=challenges_ground_1, anchor=NW, tags='PLATFORM')
id_2 = canvas.create_image(270, 310, image=challenges_ground_4, anchor=NW, tags='PLATFORM')
id_3 = canvas.create_image(400, 430, image=challenges_ground_2, anchor=NW, tags='PLATFORM')
id_4 = canvas.create_image(570, 350, image=challenges_ground_2, anchor=NW, tags='PLATFORM')
id_5 = canvas.create_image(740, 470, image=challenges_ground_4, anchor=NW, tags='PLATFORM')
id_6 = canvas.create_image(840, 400, image=challenges_ground_2, anchor=NW, tags='PLATFORM')
id_7 = canvas.create_image(1000, 330, image=challenges_ground_2, anchor=NW, tags='PLATFORM')
id_8 = canvas.create_image(1200, 330, image=challenges_ground_2, anchor=NW, tags='PLATFORM')
id_9 = canvas.create_image(1369, 260, image=challenges_ground_4, anchor=NW, tags='PLATFORM')
id_10 = canvas.create_image(1450, 330, image=challenges_ground_2, anchor=NW, tags='PLATFORM')
id_11 = canvas.create_image(1900, 430, image=challenges_ground_3, anchor=NW, tags='PLATFORM')
id_12 = canvas.create_image(2050, 370, image=challenges_ground_2, anchor=NW, tags='PLATFORM')
id_13 = canvas.create_image(2220, 430, image=challenges_ground_2, anchor=NW, tags='PLATFORM')
id_13 = canvas.create_image(2390, 480, image=challenges_ground_4, anchor=NW, tags='PLATFORM')
id_14 = canvas.create_image(2490, 440, image=challenges_ground_4, anchor=NW, tags='PLATFORM')
id_15 = canvas.create_image(2590, 480, image=challenges_ground_4, anchor=NW, tags='PLATFORM')
id_16 = canvas.create_image(2700, 450, image=challenges_ground_3, anchor=NW, tags='PLATFORM')
id_17 = canvas.create_image(3000, 440, image=challenges_ground_2, anchor=NW, tags='PLATFORM')
id_18 = canvas.create_image(3220, 400, image=challenges_ground_4, anchor=NW, tags='PLATFORM')
id_19 = canvas.create_image(3340, 350, image=challenges_ground_3, anchor=NW, tags='PLATFORM')
id_19 = canvas.create_image(3480, 300, image=challenges_ground_3, anchor=NW, tags='PLATFORM')
id_19 = canvas.create_image(3540, 200, image=challenges_ground_4, anchor=NW, tags='PLATFORM')
id_19 = canvas.create_image(3740, 460, image=challenges_ground_3, anchor=NW, tags='PLATFORM')


# ---------------------coin------------------------
k = 10
for i in range(3):
    money = canvas.create_image(300, 220 + k, image=coin)
    k += 30
for i in range(4):
    money = canvas.create_image(324 + k, 410, image=coin)
    k += 30
for i in range(7):
    money = canvas.create_image(130 + k, 525, image=coin)
    k += 30
for i in range(4):
    money = canvas.create_image(160 + k, 330, image=coin)
    k += 30
for i in range(4):
    money = canvas.create_image(310 + k, 380, image=coin)
    k += 30
for i in range(4):
    money = canvas.create_image(800 + k, 310, image=coin)
    k += 30
for i in range(4):
    money = canvas.create_image(350 + k, 525, image=coin)
    k += 30
for i in range(5):
    money = canvas.create_image(950 + k, 525, image=coin)
    k += 30
for i in range(4):
    money = canvas.create_image(1010 + k, 350, image=coin)
    k += 30
for i in range(4):
    money = canvas.create_image(1060 + k, 410, image=coin)
    k += 30
for i in range(4):
    money = canvas.create_image(1600 + k, 525, image=coin)
    k += 30
for i in range(3):
    money = canvas.create_image(1935 + k, 333, image=coin)
    k += 30
for i in range(3):
    money = canvas.create_image(2100 + k, 525, image=coin)
    k += 30

money = canvas.create_image(1025, 320, image=coin)
money = canvas.create_image(1060, 320, image=coin)
money = canvas.create_image(1100, 310, image=coin)
money = canvas.create_image(1120, 280, image=coin)
money = canvas.create_image(1145, 250, image=coin)
money = canvas.create_image(1180, 250, image=coin)
money = canvas.create_image(1200, 280, image=coin)
money = canvas.create_image(1225, 310, image=coin)
money = canvas.create_image(1265, 320, image=coin)
money = canvas.create_image(1295, 320, image=coin)

money = canvas.create_image(2420, 460, image=coin)
money = canvas.create_image(2520, 420, image=coin)
money = canvas.create_image(2620, 460, image=coin)
money = canvas.create_image(3250, 380, image=coin)

# animal..............
canvas_dino = canvas.create_image(50,355,image=dino, anchor=NW)
canvas_dino_nest = canvas.create_image(3750,420,image=dino_nest, anchor=NW)
canvas_dino_egg = canvas.create_image(3547,170,image=dino_egg, anchor=NW)

# turtle
canvas_turtle_enermey = canvas.create_image(3840,540,image=turtle_enermey, tags='turtle')
canvas_turtle_enermey = canvas.create_image(2150,540,image=turtle_enermey, tags='turtle1')
canvas_turtle_enermey_2 = canvas.create_image(2750,540,image=turtle_enermey_2, tags='turtle2')

# dino
canvas_dino_challenges2 = canvas.create_image(1310,460,image=dino_challenges2, tags='dino')
canvas_dino_challenges1 = canvas.create_image(3250,460,image=dino_challenges1, tags='dino1')

# trap
canvas_trap = canvas.create_image(255,535,image=trap, anchor=NW)
canvas_trap = canvas.create_image(1700,535,image=trap, anchor=NW)
canvas_trap = canvas.create_image(1750,535,image=trap, anchor=NW)
canvas_trap = canvas.create_image(3700,535,image=trap, anchor=NW)
canvas_trap = canvas.create_image(3530,288,image=trap, anchor=NW)

# bird
canvas_bird_1 = canvas.create_image(200, 170,image=bird_1, tags= 'BIRD')
canvas_bird_2 = canvas.create_image(3830,138,image=bird_2, tags= 'BIRD2')
canvas_bird_2 = canvas.create_image(2070, 180,image=bird_2)


# Auto-scrolling--------------------
scrollbar_bottom = Scrollbar(screen, orient='horizontal', command=canvas.xview)
canvas.configure(xscrollcommand=scrollbar_bottom.set)
scrollbar_bottom.place(relx=0, rely=1, relwidth=1, anchor='sw')

# ---------enermy_moving-------------
x = 3

def moveball():
    global x

    canvas.move('BIRD', x, 0)

    (leftPos, topPos, rightPos, bottomPos) = canvas.bbox('BIRD')
    if leftPos <= 0 or rightPos >= 1000:
        x = -x
    canvas.after(30, moveball)
canvas.after(30, moveball)

#----------turtle---------------
x1 = 1
def moveturtle():
    global x1

    canvas.move('turtle1', -1, 0)
    # canvas.move('turtle', x1, 0)

    (leftPos, topPos, rightPos, bottomPos) = canvas.bbox('turtle')
    if leftPos <=  100 or rightPos >= 800:
        x1 = -x1
    canvas.after(30, moveturtle)
canvas.after(30, moveturtle)

screen.mainloop()