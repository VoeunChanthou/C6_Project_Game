from tkinter import *
import winsound
import time


# ------------- Constants ---------------------
GRAVITY_FORCE = 9
JUMP_FORCE = 25
SPEED = 4

TIMED_LOOP = 15
IsEgg = 0
heat_life = 0
# ------------- Variables ---------------------
keyPressed = []


window = Tk()
window.title('SUPER DINO')
WIDTH = 1350
HEIGHT = 670
window.geometry(f"{WIDTH}x{HEIGHT}+{0}+{0}")
frame = Frame(window)
frame.pack()
canvas=Canvas(frame, width=WIDTH, height=HEIGHT, scrollregion= (0,0,4000,5000))
canvas.pack()

# ==========================group_image===============================================
round = PhotoImage(file='image/Round.png')
round_1 = PhotoImage(file="image/Round_1.png")
round_2 = PhotoImage(file="image/Round_2.png")
round_3 = PhotoImage(file="image/Round_3.png")
id_1 = PhotoImage(file='image/bg_home.png')
start_game = PhotoImage(file='image/play.png')
restart_game = PhotoImage(file='image/restart.png')
exit_game = PhotoImage(file='image/exit.png')
dino = PhotoImage(file='image/photo_2023-10-20_10-09-36-removebg-preview 1.png')
dino2 = PhotoImage(file='image/photo_2023-10-20_10-09-36-removebg-preview 2.png')
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
intro = PhotoImage(file='image/intro.png')
title = PhotoImage(file="image/intro_title.png")
heart = PhotoImage(file='image/heart.png')
control = PhotoImage(file='image/control_intro.png')
stop_menu = PhotoImage(file='image/stop.png')
restart_back = PhotoImage(file='image/restart_back.png')
# =======win===========
bg_over = PhotoImage(file='image/bg-win_over.png')
win = PhotoImage(file='image/text-win.png')
next= PhotoImage(file='image/next.png')
home= PhotoImage(file='image/home.png')
dino_win= PhotoImage(file='image/dino-win.png')

# =======lose========
lose= PhotoImage(file='image/dino-lose.png')
over = PhotoImage(file='image/text-over.png')
back_home = PhotoImage(file='image/back.png')

# ---------------level_1------
ground1 = PhotoImage(file='image/bg-lv1.png')
whater = PhotoImage(file='image/whater-lv1.png')
lead1 = PhotoImage(file='image/lend-lv1.png')
lead2 = PhotoImage(file='image/lead2-lv1.png')
lead3 = PhotoImage(file='image/lead3-lv1.png')
lead4 = PhotoImage(file='image/lead4-lv1.png')
blue_turtle = PhotoImage(file="image/blue_turtle.png")

# -------------------level_2--------------
level2_bg = PhotoImage(file='level2_img/renfores 1.png')
level2_bg1 = PhotoImage(file='level2_img/renfores 2.png')
ground2 = PhotoImage(file='level2_img/ground.png')
challenges_ground_l1 = PhotoImage(file='level2_img/challenge1.png')
challenges_ground_l2 = PhotoImage(file='level2_img/challenge2.png')
challenges_ground_l3 = PhotoImage(file='level2_img/challenge3.png')
challenges_ground_l4 = PhotoImage(file='level2_img/challenge4.png')
water_2 = PhotoImage(file='level2_img/water.png')
dino_challenges1 = PhotoImage(file='level2_img/dino_challenge1.png')
dino_challenges2 = PhotoImage(file='level2_img/dino_challenge2.png')

# ----------------home_bg-------------------------------
def home_game():
    canvas.create_image(0, 0, image=id_1, anchor=NW)
    canvas_start = canvas.create_image(560, 200, image=start_game, anchor=NW, tags='Start')
    canvas_restart = canvas.create_image(560, 330, image=restart_game, anchor=NW, tags='Restart')
    canvas_exit = canvas.create_image(560, 460, image=exit_game, anchor=NW, tags="Exit")
    winsound.PlaySound("sound/T-rex (Tyrannosaurus Rex Dinosaur) song I Kid & family friendly Dinosaurs Songs by Fun For Kids TV (mp3cut.net).wav", winsound.SND_ASYNC | winsound.SND_ASYNC)
home_game()
# ===================Home_function=============================
winsound.PlaySound("sound/T-rex (Tyrannosaurus Rex Dinosaur) song I Kid & family friendly Dinosaurs Songs by Fun For Kids TV (mp3cut.net).wav", winsound.SND_ASYNC | winsound.SND_ASYNC)

# ============scroll======



def scroll_bg_img():
    canvas.move('all', -3, 0)
    canvas.move('HEART0', 3, 0)
    canvas.move('HEART1', 3, 0)
    canvas.move('HEART2', 3, 0)
    canvas.move('bg', 3, 0)
    canvas.move('HOME', 3, 0)
    canvas.move('SCORE', 3, 0)
    canvas.move('TIME', 3, 0)


def scroll_bg_img_1():
    canvas.move('all', 4,0)
    canvas.move('HEART0', -4, 0)
    canvas.move('HEART1', -4, 0)
    canvas.move('HEART2', -4, 0)
    canvas.move('bg', -4, 0)
    canvas.move('HOME', -4, 0)
    canvas.move('SCORE', -4, 0)
    canvas.move('TIME', -4, 0)


def Exit(event):
    window.destroy()



def introduce(event):
    canvas.delete(ALL)
    winsound.PlaySound("sound/T-rex (Tyrannosaurus Rex Dinosaur) song I Kid & family friendly Dinosaurs Songs by Fun For Kids TV (mp3cut.net).wav", winsound.SND_ASYNC | winsound.SND_ASYNC)
    canvas.create_image(0,0,image=intro,anchor=NW)
    canvas.create_image(530, 50, image=title, anchor=NW)
    canvas.create_image(235, 160, image=control, anchor=NW)
    canvas.create_image(100, 100, image=back_home, tags='HOME')

canvas.tag_bind('Restart', '<Button-1>', introduce)

def start(event):
    canvas.delete(ALL)
    winsound.PlaySound("sound/T-rex (Tyrannosaurus Rex Dinosaur) song I Kid & family friendly Dinosaurs Songs by Fun For Kids TV (mp3cut.net).wav", winsound.SND_ASYNC | winsound.SND_ASYNC)
    canvas.create_image(0,0,image=round, anchor=NW)
    canvas.create_image(250, 320, image=round_1, tags='ROUND_1')
    canvas.create_image(680, 250, image=round_2, tags='ROUND_2')
    canvas.create_image(1100, 320, image=round_3, tags='ROUND_3')
    canvas.create_image(100, 100, image=back_home, tags='HOME')

time_game_play = 0
def time_game():
    global time_game_play
    canvas.itemconfigure('TIME', text=time_game_play)
    time_game_play += 1
    canvas.after(2000, time_game)
# ====================win and lose==============
def win_game():
    canvas.delete(ALL)
    winsound.PlaySound("sound/piglevelwin2mp3-14800 (1).wav", winsound.SND_ASYNC | winsound.SND_ASYNC)
    canvas.create_image(0, 0, image=bg_over, anchor=NW)
    canvas.create_image(750, 100, image=win)
    canvas.create_image(500, 450, image=home, tags='HOME')
    if play_again == 1:
        canvas.create_image(860, 450, image=next, tags='ROUND_2')
    elif play_again == 2:
        canvas.create_image(860, 450, image=next, tags='ROUND_3')
    elif play_again == 3:
        canvas.create_image(860, 450, image=next, tags='HOME')
    canvas.create_image(700, 300, image=dino_win)
    

def lose_game():
    canvas.delete(ALL)
    winsound.PlaySound("sound/DVHZS29-sad-trombone.wav", winsound.SND_ASYNC | winsound.SND_ASYNC)
    canvas.create_image(0, 0, image=bg_over, anchor=NW)
    canvas.create_image(660, 100, image=over)
    canvas.create_image(700,300,image=lose)
    canvas.create_image(500, 450, image=home, tags='HOME')
    if play_again == 1:
        canvas.create_image(860, 450, image=restart_back, tags='ROUND_1')
    elif play_again == 2:
        canvas.create_image(860, 450, image=restart_back, tags='ROUND_2')
    elif play_again == 3:
        canvas.create_image(860, 450, image=restart_back, tags='ROUND_3')


canvas.tag_bind('Start', '<Button-1>', start)
def home_game1(event):
    home_game()

canvas.tag_bind('HOME', '<Button-1>', home_game1)



# ===============================level1================================
def level_1(event):
    canvas.delete(ALL)
    global play_again
    winsound.PlaySound("sound/click-menu-app-147357.wav", winsound.SND_ASYNC | winsound.SND_ASYNC)

    # ============background===========
    canvas.create_image(0, 0, image=ground1, anchor=NW, tags='bg')

    # ==================Whater====================
    water = [0, 1144, 2288]
    for i in range(len(water)):
        canvas.create_image(water[i], 572, image=whater, anchor=NW, tags='WATER')

    # -----------
    land1_x = [0, 500, 1000, 1600, 2010, 2505, 3150, 950, 2090, 3090, 1590]
    land1_y = [520, 520, 520, 520, 520, 520, 520, 325, 390, 270, 290]
    land1 = 0
    for i in range(len(land1_x)):
        canvas.create_image(land1_x[i], land1_y[land1], image=lead1, anchor=NW, tags="PLATFORM")
        land1 += 1

    # ---------------------leand2-----------------

    land2_x = [0, 0, 230, 250, 470, 470, 670, 740, 1140, 2340, 3860, 2860, 1860, 2560, 3370, 1340]
    land2_y = [355, 190, 405, 260, 390, 170, 260, 400, 200, 140, 290, 290, 290, 290, 400, 379]
    land2 = 0
    for i in range(len(land2_x)):
        canvas.create_image(land2_x[i], land2_y[land2], image=lead2, anchor=NW, tags="PLATFORM")
        land2 += 1

    land3_x = [1400, 2950, 2700, 2050, 2190]
    land3_y = [525, 525, 200, 200, 170]
    land3 = 0
    for i in range(len(land3_x)):
        canvas.create_image(land3_x[i], land3_y[land3], image=lead3, anchor=NW, tags="PLATFORM")
        land3 += 1

    k = 10
    for i in range(3):
        money = canvas.create_image(200+k, 525, image=coin, tags='MONEY')
        k += 30
    for i in range(5):
        money = canvas.create_image(480 + k, 525, image=coin, tags='MONEY')
        k += 30

    for i in range(4):
        money = canvas.create_image(240 + k, 379, image=coin, tags='MONEY')
        k += 30
    for i in range(4):
        money = canvas.create_image(110 + k,160, image=coin, tags='MONEY')
        k += 30
    for i in range(4):
        money = canvas.create_image(260 + k,380, image=coin, tags='MONEY')
        k += 30
    for i in range(4):
        money = canvas.create_image(85 + k,240, image=coin, tags='MONEY')
        k += 30
    for i in range(7):
        money = canvas.create_image(300 + k,300, image=coin, tags='MONEY')
        k += 30
    for i in range(7):
        money = canvas.create_image(120 + k, 525, image=coin, tags='MONEY')
        k += 30
    for i in range(4):
        money = canvas.create_image(10 + k,180, image=coin, tags='MONEY')
        k += 30   
    for i in range(4):
        money = canvas.create_image(100 + k,350, image=coin, tags='MONEY')
        k += 30
    for i in range(8):
        money = canvas.create_image(250 + k,500, image=coin, tags='MONEY')
        k += 30
    for i in range(8):
        money = canvas.create_image(145 + k,280, image=coin, tags='MONEY')
        k += 30
    for i in range(8):
        money = canvas.create_image(210 + k,500, image=coin, tags='MONEY')
        k += 30
    for i in range(3):
        money = canvas.create_image(210 + k,350, image=coin, tags='MONEY')
        k += 30
    for i in range(4):
        money = canvas.create_image(400 + k,270, image=coin, tags='MONEY')
        k += 30
    for i in range(4):
        money = canvas.create_image(570 + k,270, image=coin, tags='MONEY')
        k += 30
    for i in range(8):
        money = canvas.create_image(130 + k,500, image=coin, tags='MONEY')
        k += 30
    for i in range(6):
        money = canvas.create_image(600 + k,500, image=coin, tags='MONEY')
        k += 30
    for i in range(6):
        money = canvas.create_image(350 + k,250, image=coin, tags='MONEY')
        k += 30
    for i in range(4):
        money = canvas.create_image(350 + k, 379, image=coin, tags='MONEY')
        k += 30




    money = canvas.create_image(1430, 515, image=coin, tags='MONEY')
    money = canvas.create_image(2980, 515, image=coin, tags='MONEY')
    money = canvas.create_image(240, 380, image=coin, tags='MONEY')
    money = canvas.create_image(270, 380, image=coin, tags='MONEY')
    money = canvas.create_image(300, 380, image=coin, tags='MONEY')
    money = canvas.create_image(330, 380, image=coin, tags='MONEY')
    money = canvas.create_image(260, 250, image=coin, tags='MONEY')
    money = canvas.create_image(290, 250, image=coin, tags='MONEY')
    money = canvas.create_image(320, 250, image=coin, tags='MONEY')
    money = canvas.create_image(350, 250, image=coin, tags='MONEY')
    money = canvas.create_image(2730, 180, image=coin, tags='MONEY')
    money = canvas.create_image(2210, 160, image=coin, tags='MONEY')
    money = canvas.create_image(2080, 190, image=coin, tags='MONEY')

    money = canvas.create_image(50, 330, image=coin, tags='MONEY')
    money = canvas.create_image(80, 330, image=coin, tags='MONEY')
    money = canvas.create_image(110, 330, image=coin, tags='MONEY')
    money = canvas.create_image(50, 160, image=coin, tags='MONEY')
    money = canvas.create_image(80, 160, image=coin, tags='MONEY')
    money = canvas.create_image(110, 160, image=coin, tags='MONEY')

    canvas.create_image(3660,425, image=lead4, anchor=NW, tags='PLATFORM')


    canvas_bird_1 = canvas.create_image(2200, 90,image=bird_1, tags= 'ENERMY')
    turtle = canvas.create_image(550, 520, image=blue_turtle, tags= 'ENERMY') 
    turtle = canvas.create_image(1000, 315, image=blue_turtle, tags= 'ENERMY') 
    turtle = canvas.create_image(3300, 260, image=blue_turtle, tags= 'ENERMY') 
    turtle = canvas.create_image(3800, 420, image=blue_turtle, tags= 'ENERMY') 
    canvas_dino_egg = canvas.create_image(2380,110,image=dino_egg, anchor=NW, tags='EGG')
    canvas.create_image(3910, 270, image=dino_nest, tags='EGG')
    canvas.create_image(1220, 10, image=stop_menu, anchor=NW, tags='HOME')

    h = 30
    for i in range(3):
        canvas.create_image(50+h, 50, image=heart, tags='HEART'+str(i))
        h += 50
    canvas.create_text(700, 50, text='160', font=('bold', 25), tags='TIME')
    canvas.create_text(400, 50, text='Score: ', font=('bold', 20), tags='bg')
    canvas.create_text(460, 50, text='0', font=('bold', 20), tags='SCORE')

    canvas.create_image(100, 40, image=dino, tags='dino_character')
    play_again = 1
    time_game()
    move()
    gravity()


# ================================level2=========================
def level_2(event):
    canvas.delete(ALL)
    global play_again
    play_again = 2
    winsound.PlaySound("sound/click-menu-app-147357.wav", winsound.SND_ASYNC | winsound.SND_ASYNC)
    canvas.create_image(0,0,image=level2_bg,anchor=NW, tags='bg')

    canvas_water = canvas.create_image(550,570,image=water_2, anchor=NW, tags='WATER')
    canvas_water = canvas.create_image(2200,570,image=water_2, anchor=NW, tags='WATER')

    ground2_l2 = [0, 1100, 1650, 2750, 3300, 3700]
    for i in range(len(ground2_l2)):
        canvas.create_image(ground2_l2[i] ,570,image=ground2, anchor=NW, tags="PLATFORM")
 

    # ===========================ground==================
    canvas.create_image(0, 425, image=challenges_ground_l1, anchor=NW, tags='PLATFORM')

    canvas.create_image(450, 430, image=challenges_ground_l2, anchor=NW, tags='PLATFORM')
    canvas.create_image(570, 300, image=challenges_ground_l2, anchor=NW, tags='PLATFORM')
    canvas.create_image(3000, 440, image=challenges_ground_l2, anchor=NW, tags='PLATFORM')
    canvas.create_image(1000, 450, image=challenges_ground_l2, anchor=NW, tags='PLATFORM')
    canvas.create_image(2050, 370, image=challenges_ground_l2, anchor=NW, tags='PLATFORM')
    canvas.create_image(800, 350, image=challenges_ground_l2, anchor=NW, tags='PLATFORM')
    canvas.create_image(2250, 430, image=challenges_ground_l2, anchor=NW, tags='PLATFORM')
    canvas.create_image(1230, 350, image=challenges_ground_l2, anchor=NW, tags='PLATFORM')
    canvas.create_image(1650, 300, image=challenges_ground_l2, anchor=NW, tags='PLATFORM')

    canvas.create_image(1900, 430, image=challenges_ground_l3, anchor=NW, tags='PLATFORM')
    canvas.create_image(2700, 450, image=challenges_ground_l3, anchor=NW, tags='PLATFORM')
    canvas.create_image(3340, 350, image=challenges_ground_l3, anchor=NW, tags='PLATFORM')
    canvas.create_image(3740, 460, image=challenges_ground_l3, anchor=NW, tags='PLATFORM')
    canvas.create_image(3480, 300, image=challenges_ground_l3, anchor=NW, tags='PLATFORM')

    canvas.create_image(700, 480, image=challenges_ground_l4, anchor=NW, tags='PLATFORM')
    canvas.create_image(850, 480, image=challenges_ground_l4, anchor=NW, tags='PLATFORM')
    canvas.create_image(1450, 260, image=challenges_ground_l4, anchor=NW, tags='PLATFORM')
    canvas.create_image(2490, 440, image=challenges_ground_l4, anchor=NW, tags='PLATFORM')
    canvas.create_image(3220, 400, image=challenges_ground_l4, anchor=NW, tags='PLATFORM')
    canvas.create_image(350, 310, image=challenges_ground_l4, anchor=NW, tags='PLATFORM')
    canvas.create_image(3540, 200, image=challenges_ground_l4, anchor=NW, tags='PLATFORM')


    k = 10
    for i in range(3):
        canvas.create_image(380, 220 + k, image=coin, tags='MONEY')
        k += 30
    for i in range(4):
        money = canvas.create_image(370 + k, 420, image=coin, tags='MONEY')
        k += 30
    for i in range(7):
        canvas.create_image(130 + k, 545, image=coin, tags='MONEY')
        k += 30
    for i in range(4):
        money = canvas.create_image(160 + k, 290, image=coin, tags='MONEY')
        k += 30
    for i in range(4):
        canvas.create_image(280 + k, 340, image=coin, tags='MONEY')
        k += 30
    for i in range(4):
        canvas.create_image(1000 + k, 290, image=coin, tags='MONEY')
        k += 30
    for i in range(4):
        money = canvas.create_image(240 + k, 440, image=coin, tags='MONEY')
        k += 30
    for i in range(4):
        canvas.create_image(340 + k, 340, image=coin, tags='MONEY')
        k += 30
    for i in range(5):
        money = canvas.create_image(900 + k, 550, image=coin, tags='MONEY')
        k += 30
    for i in range(4):
        canvas.create_image(900 + k, 360, image=coin, tags='MONEY')
        k += 30
    for i in range(4):
        money = canvas.create_image(970 + k, 420, image=coin, tags='MONEY')
        k += 30
    for i in range(4):
        canvas.create_image(1450 + k, 550, image=coin, tags='MONEY')
        k += 30
    for i in range(3):
        canvas.create_image(1830 + k, 333, image=coin, tags='MONEY')
        k += 30
    for i in range(3):
        canvas.create_image(1900 + k, 550, image=coin, tags='MONEY')
        k += 30
    canvas.create_image(2520, 420, image=coin, tags='MONEY')
    canvas.create_image(3250, 380, image=coin, tags='MONEY')

    
    canvas_dino_nest = canvas.create_image(3750,420,image=dino_nest, anchor=NW, tags='EGG')
    canvas_dino_egg = canvas.create_image(3547,170,image=dino_egg, anchor=NW, tags='EGG')
    
    canvas_turtle_enermey = canvas.create_image(3700,560,image=turtle_enermey, tags= 'ENERMY')
    canvas_turtle_enermey = canvas.create_image(2150,560,image=turtle_enermey, tags= 'ENERMY')
    canvas_turtle_enermey_2 = canvas.create_image(3200,560,image=turtle_enermey_2, tags= 'ENERMY')

    trap_l2 = [255, 1700, 1750, 3700, 3530]
    for i in range(len(trap_l2)):
        canvas.create_image(trap_l2[i], 550, image=trap, anchor=NW, tags='ENERMY')
 
    canvas_trap = canvas.create_image(3530,288,image=trap, anchor=NW, tags='ENERMY')

    # dino
    canvas_dino_challenges2 = canvas.create_image(1310,540,image=dino_challenges2, tags= 'ENERMY')
    canvas_dino_challenges1 = canvas.create_image(3250,540,image=dino_challenges1, tags= 'ENERMY')

    # bird
    canvas_bird_1 = canvas.create_image(200, 170,image=bird_1, tags= 'ENERMY')
    canvas_bird_2 = canvas.create_image(3830,138,image=bird_2, tags= 'ENERMY')
    canvas_bird_2 = canvas.create_image(2070, 240,image=bird_2, tags= 'ENERMY')
    canvas.create_image(1220, 10, image=stop_menu, anchor=NW, tags='HOME')

    h = 30
    for i in range(3):
        canvas.create_image(50+h, 50, image=heart, tags='HEART'+str(i))
        h += 50
    canvas.create_text(700, 50, text='160', font=('bold', 25), tags='TIME')
    canvas.create_text(400, 50, text='Score: ', font=('bold', 20), tags='bg')
    canvas.create_text(460, 50, text='0', font=('bold', 20), tags='SCORE')

    canvas.create_image(100, 40, image=dino, tags='dino_character')

    time_game()
    move()
    gravity()


# ========================level3====================================
def level_3(event):

    canvas.delete(ALL)
    global play_again
    play_again = 3
    winsound.PlaySound("sound/click-menu-app-147357.wav", winsound.SND_ASYNC | winsound.SND_ASYNC)
    # home_bg-------------------------------

    canvas.create_image(0,0,image=level3_bg,anchor=NW, tags='bg')
    canvas.create_image(600,572,image=water, anchor=NW, tags='WATER')
    canvas.create_image(2550,572,image=water, anchor=NW, tags='WATER')

    first_ground = [0, 1250, 1650, 2000, 3350, 3600, 3900]
    for i in range(len(first_ground)):
        canvas.create_image(first_ground[i], 572, image=ground, anchor=NW, tags='PLATFORM')

     
    # -------------------ground_2-----------------
    ground_2_x = [40,110, 770, 950, 950, 1100]
    ground_2_y = [250, 380, 400, 230, 450, 350]
    ground_2 = 0
    for i in range(len(ground_2_x)):
        canvas.create_image(ground_2_x[i], ground_2_y[ground_2], image=challenges_ground_2, anchor=NW, tags='PLATFORM')
        ground_2 += 1

    id_4 = canvas.create_image(270, 450, image=challenges_ground, anchor=NW, tags='PLATFORM')

    ground_4_x = [500, 1300, 3300, 1850]
    ground_4_y = [270, 330, 400, 350]
    ground_4 = 0
    for i in range(len(ground_4_x)):
        canvas.create_image(ground_4_x[i], ground_4_y[ground_4], image=challenges_ground_4, anchor=NW, tags = 'PLATFORM')
        ground_4 += 1

    # -----------------------ground_4---------------------
    ground_3_x = [1650, 250, 2220, 2420, 2650, 2850, 3100, 3850, 3700, 3740]
    ground_3_y = [450, 230, 450, 370, 450, 500, 500, 200, 290, 460]
    ground_3 = 0
    for i in range(len(ground_3_x)):
        canvas.create_image(ground_3_x[i], ground_3_y[ground_3], image=challenges_ground_3, anchor=NW, tags='PLATFORM')
        ground_3 += 1

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

    money_arr_x = [820, 850, 880, 910, 940, 970, 2500, 2530, 2560, 2590, 2620, 2650, 2680]
    money_arr_y = [400, 370, 340, 370, 400, 430, 360, 330, 300, 330, 360, 390, 420]
    money_y = 0
    for i in range(len(money_arr_x)):
        canvas.create_image(money_arr_x[i], money_arr_y[money_y], image=coin, tags='MONEY')
        money_y += 1

    # ----------------------animal----------------------------


    canvas.create_image(400, 570, image=turtle_enermey, tags= 'ENERMY')
    canvas.create_image(550, 270, image=turtle_enermey, tags= 'ENERMY')
    canvas.create_image(3800, 570, image=turtle_enermey, tags= 'ENERMY')
    canvas.create_image(450, 450, image=turtle_enermey_2, tags= 'ENERMY')
    canvas.create_image(1900, 355, image=turtle_enermey_2, tags= 'ENERMY')
    canvas.create_image(3500, 400, image=turtle_enermey_2, tags= 'ENERMY')
    turtle = canvas.create_image(1500, 570, image=turtle_enermey_2, tags= 'ENERMY')

    bird_0=canvas.create_image(100, 100, image=bird_1, tags= 'ENERMY')
    canvas.create_image(3600, 180, image=bird_1, tags= 'ENERMY')
    canvas.create_image(2800, 300, image=bird_2, tags= 'ENERMY')

    trap_arr = [1350, 1400, 1800, 1850, 2550, 2600, 3600, 3650]
    for i in range(len(trap_arr)):
        canvas.create_image(trap_arr[i], 570, image=trap, tags= 'ENERMY')


    egg = canvas.create_image(990, 240, image=dino_egg, tags='EGG')
    nest = canvas.create_image(3910, 190, image=dino_nest, tags='EGG')
    h = 30
    for i in range(3):
        canvas.create_image(50+h, 50, image=heart, tags='HEART'+str(i))
        h += 50
    canvas.create_text(700, 50, text='160', font=('bold', 25), tags='TIME')
    canvas.create_text(400, 50, text='Score: ', font=('bold', 20), tags='bg')
    canvas.create_text(460, 50, text='0', font=('bold', 20), tags='SCORE')
    canvas.create_image(1220, 10, image=stop_menu, anchor=NW, tags='HOME')
    canvas.create_image(90, 500, image=dino, tags='dino_character')

    # ----------------function----------

    time_game()
    move()
    gravity()



# ====================egg_id================
def check_egg():
    coord_1 = canvas.coords('dino_character')
    platforms = canvas.find_withtag("EGG")

    overlap = canvas.find_overlapping(coord_1[0], coord_1[1], coord_1[0] + dino.width(), coord_1[1] + dino.height())

    for platform in platforms:
        if platform in overlap:
            return platform
    return 0

def check_enermy():
    coord_1 = canvas.coords('dino_character')
    platforms = canvas.find_withtag("ENERMY")

    overlap = canvas.find_overlapping(coord_1[0], coord_1[1], coord_1[0] + dino.width(), coord_1[1] + dino.height())

    for platform in platforms:
        if platform in overlap:
            return platform
    return 0

def check_water():
    coord_1 = canvas.coords('dino_character')
    platforms = canvas.find_withtag("WATER")

    overlap = canvas.find_overlapping(coord_1[0], coord_1[1], coord_1[0] + dino.width(), coord_1[1] + dino.height())

    for platform in platforms:
        if platform in overlap:
            return platform
    return 0



# ==============================defind id money==================
def check_money():
    coord_1 = canvas.coords('dino_character')
    platforms = canvas.find_withtag("MONEY")

    overlap = canvas.find_overlapping(coord_1[0], coord_1[1], coord_1[0] + dino.width(), coord_1[1] + dino.height())

    for platform in platforms:
        if platform in overlap:
            return platform
    return 0


# ================================defind_id=======================
def check_movement(dx=0, dy=0, checkGround=False):
    coord = canvas.coords('dino_character')
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
            canvas.move('dino_character', 0, -force)
            window.after(TIMED_LOOP, jump, force-1)


# ----------------start_move------------------------
def start_move(event):
    if event.keysym not in keyPressed:
        keyPressed.append(event.keysym)
        if len(keyPressed) == 1:
            move()


# =======================update_time==============
def update_time_leve():
    canvas.itemconfigure('TIME')


#---------------Move_object----------------------------------

score = 0
def move():
    global IsEgg, score, heat_life
    if not keyPressed == []:
        x = 0
        if "Left" in keyPressed:
            x -= SPEED
            canvas.itemconfig('dino_character', image=dino2)
            scroll_bg_img_1()
        if "Right" in keyPressed:
            x += SPEED
            canvas.itemconfig('dino_character', image=dino)
            
        if "space" in keyPressed and not check_movement(0, GRAVITY_FORCE, True):
            jump(JUMP_FORCE)
            winsound.PlaySound("sound/jump_c_02-102843.wav", winsound.SND_ASYNC | winsound.SND_ASYNC)
        if check_movement(x):
            canvas.move('dino_character', x, 0)
            if x != 0:
                scroll_bg_img()
        window.after(TIMED_LOOP, move)
    money = check_money()
   
    if money != 0:
        canvas.delete(money)
        score += 1
        canvas.itemconfigure('SCORE', text=score)
        winsound.PlaySound("sound/collect-ring-15982.wav", winsound.SND_ASYNC | winsound.SND_ASYNC)
    eGG = check_egg()
    if eGG != 0:
        canvas.delete(eGG)
        IsEgg += 1
    if IsEgg == 2:
        win_game()
        IsEgg = 0
    eNermy = check_enermy()
    if eNermy != 0:
        winsound.PlaySound("sound/enermy.wav", winsound.SND_ASYNC | winsound.SND_ASYNC)
        canvas.delete('HEART2')
        heat_life += 1
        if heat_life > 20:
            canvas.delete('HEART1')
    elif heat_life > 30:
        IsEgg = 0
        canvas.delete('HEART0')
        lose_game()
        heat_life = 0
    water_enermy = check_water()
    if water_enermy != 0:
        IsEgg = 0
        lose_game()
        

#--------check_player_move---------------------
def gravity():
    if check_movement(0, GRAVITY_FORCE, True):
        canvas.move('dino_character', 0, GRAVITY_FORCE)
    window.after(TIMED_LOOP, gravity)

#--------------stop_move and remove key------------------------
def stop_move(event):
    global keyPressed
    if event.keysym in keyPressed:
        keyPressed.remove(event.keysym)



canvas.tag_bind('ROUND_1', '<Button-1>', level_1)
canvas.tag_bind('ROUND_2', '<Button-1>', level_2)
canvas.tag_bind('ROUND_3', '<Button-1>', level_3)
canvas.tag_bind('Exit', '<Button-1>', Exit)
window.bind("<Key>", start_move)
window.bind("<KeyRelease>", stop_move)

window.resizable(0,0)

window.mainloop()