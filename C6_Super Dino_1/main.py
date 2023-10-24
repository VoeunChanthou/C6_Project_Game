from tkinter import *
from pygame import mixer
import time

window = Tk()
window.title('hi')
WIDTH = 1350
HEIGHT = 670
window.geometry(f"{WIDTH}x{HEIGHT}+{0}+{0}")
frame = Frame(window)
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
level3_bg = PhotoImage(file='image/Frame 14.png')
ground = PhotoImage(file='image/image 2.png')
water = PhotoImage(file='image/Frame 15.png')
turtle_enermey = PhotoImage(file='image/turtle.png')
turtle_enermey_2 = PhotoImage(file='image/turtle_2.png')
bird_1 = PhotoImage(file='image/bird.png')
bird_2 = PhotoImage(file='image/bird_2.png')
challenges_ground = PhotoImage(file='image/challenges.png')
challenges_ground_2 = PhotoImage(file='image/challenge_2s.png')
challenges_ground_3 = PhotoImage(file='image/challenge_3s.png')
challenges_ground_4 = PhotoImage(file='image/challenge_4s.png')
dino_egg = PhotoImage(file='image/dino_egg-removebg-preview 1.png')
trap = PhotoImage(file='image/trap.png')
coin = PhotoImage(file='image/coin.png')
dino_nest = PhotoImage(file='image/nest.png')
start = PhotoImage(file='image/Start_button.png')


# home_bg-------------------------------


canvas_bg_level3 = canvas.create_image(0,0,image=level3_bg,anchor=NW)
canvas_bg_level3_1 = canvas.create_image(1350,0,image=level3_bg,anchor=NW)
canvas_bg_level3_2 = canvas.create_image(3000,0,image=level3_bg,anchor=NW)
canvas_water = canvas.create_image(600,572,image=water, anchor=NW)
canvas_water = canvas.create_image(2550,572,image=water, anchor=NW)
canvas_ground = canvas.create_image(0,572,image=ground, anchor=NW, tags="PLATFORM")
canvas_ground = canvas.create_image(1250,572,image=ground, anchor=NW, tags="PLATFORM")
canvas_ground = canvas.create_image(1650,572,image=ground, anchor=NW, tags="PLATFORM")
canvas_ground = canvas.create_image(2000,572,image=ground, anchor=NW, tags="PLATFORM")
canvas_ground = canvas.create_image(3350,572,image=ground, anchor=NW, tags="PLATFORM")

id_1 = canvas.create_image(40, 250, image=challenges_ground_2, anchor=NW, tags='PLATFORM')
id_2 = canvas.create_image(110, 380, image=challenges_ground_2, anchor=NW, tags='PLATFORM')
id_3 = canvas.create_image(250, 230, image=challenges_ground_3, anchor=NW, tags='PLATFORM')
id_4 = canvas.create_image(270, 450, image=challenges_ground, anchor=NW, tags='PLATFORM')
id_5 = canvas.create_image(500, 270, image=challenges_ground_4, anchor=NW, tags='PLATFORM')
id_6 = canvas.create_image(770, 400, image=challenges_ground_2, anchor=NW, tags='PLATFORM')
id_7 = canvas.create_image(950, 230, image=challenges_ground_2, anchor=NW, tags='PLATFORM')
id_8 = canvas.create_image(950, 450, image=challenges_ground_2, anchor=NW, tags='PLATFORM')
id_9 = canvas.create_image(1100, 350, image=challenges_ground_2, anchor=NW, tags='PLATFORM')
id_10 = canvas.create_image(1300, 330, image=challenges_ground_4, anchor=NW, tags='PLATFORM')
id_11 = canvas.create_image(1650, 450, image=challenges_ground_3, anchor=NW, tags='PLATFORM')
id_12 = canvas.create_image(1850, 350, image=challenges_ground_4, anchor=NW, tags='PLATFORM')
id_13 = canvas.create_image(2220, 450, image=challenges_ground_3, anchor=NW, tags='PLATFORM')
id_13 = canvas.create_image(2420, 370, image=challenges_ground_3, anchor=NW, tags='PLATFORM')
id_14 = canvas.create_image(2650, 450, image=challenges_ground_3, anchor=NW, tags='PLATFORM')
id_15 = canvas.create_image(2850, 500, image=challenges_ground_3, anchor=NW, tags='PLATFORM')
id_16 = canvas.create_image(3100, 500, image=challenges_ground_3, anchor=NW, tags='PLATFORM')
id_17 = canvas.create_image(3300, 400, image=challenges_ground_4, anchor=NW, tags='PLATFORM')
id_18 = canvas.create_image(3850, 200, image=challenges_ground_3, anchor=NW, tags='PLATFORM')
id_19 = canvas.create_image(3700, 290, image=challenges_ground_3, anchor=NW, tags='PLATFORM')
id_19 = canvas.create_image(3740, 460, image=challenges_ground_3, anchor=NW, tags='PLATFORM')




# ---------------------coin------------------------
k = 10
for i in range(3):
    money = canvas.create_image(300, 150 + k, image=coin, tags='MONEY')
    k += 30
for i in range(10):
    money = canvas.create_image(250 + k, 450, image=coin, tags='MONEY')
    k += 30
for i in range(5):
    money = canvas.create_image(200 + k, 270, image=coin, tags='MONEY')
    k += 30
for i in range(6):
    money = canvas.create_image(850 + k, 330, image=coin, tags='MONEY')
    k += 30
for i in range(6):
    money = canvas.create_image(860 + k, 570, image=coin, tags='MONEY')
    k += 30
for i in range(6):
    money = canvas.create_image(1050 + k, 350, image=coin, tags='MONEY')
    k += 30
for i in range(6):
    money = canvas.create_image(2300 + k, 400, image=coin, tags='MONEY')
    k += 30
money = canvas.create_image(820, 400, image=coin, tags='MONEY')
money = canvas.create_image(850, 370, image=coin, tags='MONEY')
money = canvas.create_image(880, 340, image=coin, tags='MONEY')
money = canvas.create_image(910, 370, image=coin, tags='MONEY')
money = canvas.create_image(940, 400, image=coin, tags='MONEY')
money = canvas.create_image(970, 430, image=coin, tags='MONEY')

money = canvas.create_image(2500, 360, image=coin, tags='MONEY')
money = canvas.create_image(2530, 330, image=coin, tags='MONEY')
money = canvas.create_image(2560, 300, image=coin, tags='MONEY')
money = canvas.create_image(2590, 330, image=coin, tags='MONEY')
money = canvas.create_image(2620, 360, image=coin, tags='MONEY')
money = canvas.create_image(2650, 390, image=coin, tags='MONEY')
money = canvas.create_image(2680, 420, image=coin, tags='MONEY')


# ----------------------animal----------------------------
canvas.create_image(400, 570, image=turtle_enermey, tags='turtle1')
canvas.create_image(550, 270, image=turtle_enermey, tags='turtle')
canvas.create_image(3800, 570, image=turtle_enermey, tags='turtle6')
canvas.create_image(450, 450, image=turtle_enermey_2, tags='turtle2')
canvas.create_image(1900, 355, image=turtle_enermey_2, tags='turtle4')
canvas.create_image(3500, 400, image=turtle_enermey_2, tags='turtle5')
turtle = canvas.create_image(1500, 570, image=turtle_enermey_2, tags='turtle3')

bird_0=canvas.create_image(100, 100, image=bird_1, tags='BIRD')
canvas.create_image(3600, 180, image=bird_1, tags='BIRD3')
canvas.create_image(2800, 300, image=bird_2, tags='BIRD2')
trap_enermy = canvas.create_image(1350, 570, image = trap)
trap_enermy = canvas.create_image(1400, 570, image = trap)
trap_enermy = canvas.create_image(1800, 570, image = trap)
trap_enermy = canvas.create_image(1850, 570, image = trap)
trap_enermy = canvas.create_image(2550, 570, image = trap)
trap_enermy = canvas.create_image(2600, 570, image = trap)
trap_enermy = canvas.create_image(3600, 570, image = trap)
trap_enermy = canvas.create_image(3650, 570, image = trap)

egg = canvas.create_image(990, 240, image=dino_egg)
nest = canvas.create_image(3910, 190, image=dino_nest)

dino_character = canvas.create_image(90, 550, image=dino)

start_game1 = canvas.create_image(660, 330, image=start, tags='start_game')
# Auto-scrolling--------------------
scrollbar_bottom = Scrollbar(window, orient='horizontal', command=canvas.xview)
canvas.configure(xscrollcommand=scrollbar_bottom.set)
scrollbar_bottom.place(relx=0, rely=1, relwidth=1, anchor='sw')

window.bind('<Right>', lambda event: canvas.xview_scroll(1, 'units'))
window.bind('<Left>', lambda event: canvas.xview_scroll(-1, 'units'))

# def scroll_bg_img():
#     canvas.move(canvas_bg_level3,-1,0)
#     canvas.move(canvas_bg_level3_1,-1,0)
#     canvas.move(canvas_bg_level3_2,-1,0)

#     if canvas.coords(canvas_bg_level3)[0]<-2000:
#         canvas.coords(canvas_bg_level3,2000,0)
#     elif canvas.coords(canvas_bg_level3_1)[0]<-2000:
#         canvas.coords(canvas_bg_level3_1,2000,0)
#     elif canvas.coords(canvas_bg_level3_2)[0]<-2000:
#         canvas.coords(canvas_bg_level3_2,2000,0)


# # def scroll_bg_img():
# #     canvas.move('all',-1,0)
    

# #     if canvas.coords('all')[0]<-2000:
# #         canvas.coords('all',2000,0)

# # def scroll_bg_img_1():

# #     canvas.move('all',1,0)
    

# #     if canvas.coords('all')[0]<-2000:
# #         canvas.coords('all',2000,0)
    

# def scroll_bg_img_1():
#     canvas.move(canvas_bg_level3,1,0)
#     canvas.move(canvas_bg_level3_1,1,0)
#     canvas.move(canvas_bg_level3_2,1,0)

#     if canvas.coords(canvas_bg_level3)[0]<-2000:
#         canvas.coords(canvas_bg_level3,2000,0)
#     elif canvas.coords(canvas_bg_level3_1)[0]<-2000:
#         canvas.coords(canvas_bg_level3_1,2000,0)
#     elif canvas.coords(canvas_bg_level3_2)[0]<-2000:
#         canvas.coords(canvas_bg_level3_2,2000,0)


# -----------------start-game------------

def playGame(event):
    canvas.delete('start_game')
    click()
canvas.tag_bind('start_game', '<Button-1>', playGame)


# ----enermy_moving-------------
x = 3

def moveball():
    global x
    canvas.move('BIRD', x, 0)

    (leftPos, topPos, rightPos, bottomPos) = canvas.bbox('BIRD')
    if leftPos <= 0  or rightPos >= 1000 :
        x = -x
    canvas.after(30, moveball)
canvas.after(30, moveball)


#-----------bird_2------------------------
xbird = 3

def movebird2():
    global xbird

    canvas.move('BIRD2', xbird, 0)

    (leftPos, topPos, rightPos, bottomPos) = canvas.bbox('BIRD2')
    if leftPos <= 2500 or rightPos >= 3000:
        xbird = -xbird
    canvas.after(30, movebird2)
canvas.after(30, movebird2)
#-----------bird_3------------------------
xbird3 = 3

def movebird3():
    global xbird3

    canvas.move('BIRD3', xbird3, 0)

    (leftPos, topPos, rightPos, bottomPos) = canvas.bbox('BIRD3')
    if leftPos <= 3500 or rightPos >= 3850:
        xbird3 = -xbird3
    canvas.after(30, movebird3)
canvas.after(30, movebird3)



#/----------turtle---------------
x1 = 1
def moveturtle():
    global x1

    canvas.move('turtle1', -1, 0)
    canvas.move('turtle', x1, 0)

    (leftPos, topPos, rightPos, bottomPos) = canvas.bbox('turtle')
    if leftPos <= 500 or rightPos >= 800:
        x1 = -x1
    canvas.after(30, moveturtle)
canvas.after(30, moveturtle)

# -----turtle2-----------------------

x2 = 1
def moveturtle2():
    global x2

    canvas.move('turtle2', x2, 0)

    (leftPos, topPos, rightPos, bottomPos) = canvas.bbox('turtle2')
    if leftPos <= 400 or rightPos >= 700:
        x2 = -x2
    canvas.after(30, moveturtle2)
canvas.after(30, moveturtle2)

#-----------turtle3-----------

x3 = 1
def moveturtle3():
    global x3

    canvas.move('turtle3', x3, 0)

    (leftPos, topPos, rightPos, bottomPos) = canvas.bbox('turtle3')
    if leftPos <= 1450 or rightPos >= 1800:
        x3 = -x3
    canvas.after(30, moveturtle3)
canvas.after(30, moveturtle3)

# ------turtle4----------

x4 = 1
def moveturtle4():
    global x4

    canvas.move('turtle4', x4, 0)

    (leftPos, topPos, rightPos, bottomPos) = canvas.bbox('turtle4')
    if leftPos <= 1850 or rightPos >= 2150:
        x4 = -x4
    canvas.after(30, moveturtle4)
canvas.after(30, moveturtle4)

# ------turtle5----------

x5 = 1
def moveturtle5():
    global x5

    canvas.move('turtle5', x5, 0)

    (leftPos, topPos, rightPos, bottomPos) = canvas.bbox('turtle5')
    if leftPos <= 3300 or rightPos >= 3600:
        x5 = -x5
    canvas.after(30, moveturtle5)
canvas.after(30, moveturtle5)


# ------turtle5----------

x6 = 1
def moveturtle6():
    global x6

    canvas.move('turtle6', x6, 0)

    (leftPos, topPos, rightPos, bottomPos) = canvas.bbox('turtle6')
    if leftPos <= 3500 or rightPos >= 4000:
        x6 = -x6
    canvas.after(30, moveturtle6)
canvas.after(30, moveturtle6)

# -------------------defind id money----------------
def check_money():
    coord_1 = canvas.coords(dino_character)
    platforms = canvas.find_withtag("MONEY")

    overlap = canvas.find_overlapping(coord_1[0], coord_1[1], coord_1[0] + dino.width(), coord_1[1] + dino.height())

    for platform in platforms:
        if platform in overlap:
            return platform
    return 0

# ------------Grounp_sound------------------
def click():
    mixer.init()
    mixer.music.load('sound/click-menu-app-147357.mp3')
    mixer.music.play()

def playSound():
    mixer.init()
    mixer.music.load('sound/collect-ring-15982.mp3')
    mixer.music.play() 
def jumpingSound():
    mixer.init()
    mixer.music.load('sound/jump_c_02-102843.mp3')
    mixer.music.play()
def playSound_during_game():
    mixer.init()
    mixer.music.load('sound/game-music-loop-3-144252.mp3')
    mixer.music.play(loops=-1)
playSound_during_game()

# -----------------defind_id-----------------
def check_movement(dx=0, dy=0, checkGround=False):
    coord = canvas.coords(dino_character)
    platforms = canvas.find_withtag("PLATFORM")

    if coord[0] + dx < 0 or coord[1] + dx > WIDTH:
        return False

    if checkGround:
        overlap = canvas.find_overlapping(coord[0], coord[1], coord[0] + dino.width(), (coord[1] - 50) + dino.height() + dy)
    else:
        overlap = canvas.find_overlapping(coord[0]+dx, coord[1]+dy, coord[0]+ dino.width() + dx, (coord[1] - 50) + dino.height())

    for platform in platforms:
        if platform in overlap:
            return False

    return True

# -----------------------Jump by moving the player up by force pixels-----------------------------
def jump(force):
    if force > 0:
        if check_movement(0, -force):
            canvas.move(dino_character, 0, -force)
            window.after(TIMED_LOOP, jump, force-1)


# ----------------start_move------------------------
def start_move(event):
    if event.keysym not in keyPressed:
        keyPressed.append(event.keysym)
        if len(keyPressed) == 1:
            move()


#---------------Move_object----------------------------------

def move():
    
    if not keyPressed == []:
        x = 0
        if "a" in keyPressed:
            x -= SPEED
            # scroll_bg_img_1()
        if "d" in keyPressed:
            x += SPEED
            # scroll_bg_img()
            
            
        if "w" in keyPressed and not check_movement(0, GRAVITY_FORCE, True):
            jump(JUMP_FORCE)
            jumpingSound()
        if check_movement(x):
            canvas.move(dino_character, x, 0)
        window.after(TIMED_LOOP, move)
    money = check_money()
    if money != 0:
        canvas.delete(money)
        playSound()

#--------check_player_move---------------------
def gravity():
    if check_movement(0, GRAVITY_FORCE, True):
        canvas.move(dino_character, 0, GRAVITY_FORCE)
    window.after(TIMED_LOOP, gravity)


#--------------stop_move and remove key------------------------
def stop_move(event):
    global keyPressed
    if event.keysym in keyPressed:
        keyPressed.remove(event.keysym)



gravity()


window.bind("<Key>", start_move)
window.bind("<KeyRelease>", stop_move)

window.resizable(0,0)

window.mainloop()