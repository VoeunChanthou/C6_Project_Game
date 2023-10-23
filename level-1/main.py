from tkinter import*

window = Tk()
window.title ('SUPER DINO')
WIDTH = 1350
HEIGHT = 670
window.geometry(f"{WIDTH}x{HEIGHT}+{0}+{0}")
frame = Frame(window)
frame.pack()
canvas=Canvas(frame, width=1350, height=670, scrollregion= (0,0,4000,5000))
canvas.pack()


# group-image
ground = PhotoImage(file='image/bg-lv1.png')
whater = PhotoImage(file='image/whater-lv1.png')
lead1 = PhotoImage(file='image/lend-lv1.png')
lead2 = PhotoImage(file='image/lead2-lv1.png')
lead3 = PhotoImage(file='image/lead3-lv1.png')
lead4 = PhotoImage(file='image/lead4-lv1.png')
dino = PhotoImage(file='image/photo_2023-10-20_10-09-36-removebg-preview 1.png')
dino_egg = PhotoImage(file='image/dino_egg-removebg-preview 1.png')
dino_nest = PhotoImage(file='image/nest.png')
coin = PhotoImage(file='image/coin.png')

# background
canvas.create_image(0, 0, image=ground, anchor=NW, tags="PLATFORM")
canvas.create_image(1797, 0, image=ground, anchor=NW, tags="PLATFORM")
canvas.create_image(3594, 0, image=ground, anchor=NW, tags="PLATFORM")

# Whater
canvas.create_image(0, 572, image=whater, anchor=NW)
canvas.create_image(1144, 572, image=whater, anchor=NW)
canvas.create_image(2288, 572, image=whater, anchor=NW)
# Dino
canvas.create_image(0, 473, image=dino, anchor=NW)
canvas.create_image(2400, 100, image=dino_egg, anchor=NW)
canvas.create_image(3890,250, image=dino_nest, anchor=NW)

# 
canvas.create_image(0,525, image=lead1, anchor=NW)
canvas.create_image(500,525, image=lead1, anchor=NW)
canvas.create_image(1000,525, image=lead1, anchor=NW)
canvas.create_image(1600,525, image=lead1, anchor=NW)
canvas.create_image(2010,525, image=lead1, anchor=NW)
canvas.create_image(2505, 525, image=lead1, anchor=NW)
canvas.create_image(3150,525, image=lead1, anchor=NW)
canvas.create_image(950,325, image=lead1, anchor=NW)
canvas.create_image(2090,390, image=lead1, anchor=NW)
canvas.create_image(3090,270, image=lead1, anchor=NW)
canvas.create_image(1590,290, image=lead1, anchor=NW)
# 
canvas.create_image(0,355, image=lead2, anchor=NW)
canvas.create_image(0,190, image=lead2, anchor=NW)
canvas.create_image(230,405, image=lead2, anchor=NW)
canvas.create_image(250,260, image=lead2, anchor=NW)
canvas.create_image(470,390, image=lead2, anchor=NW)
canvas.create_image(470,170, image=lead2, anchor=NW)
canvas.create_image(670,260, image=lead2, anchor=NW)
canvas.create_image(740,400, image=lead2, anchor=NW)
canvas.create_image(1140,200, image=lead2, anchor=NW)
canvas.create_image(2340,140, image=lead2, anchor=NW)
canvas.create_image(3860,290, image=lead2, anchor=NW)
canvas.create_image(2860,290, image=lead2, anchor=NW)
canvas.create_image(1860,290, image=lead2, anchor=NW)
canvas.create_image(2560,290, image=lead2, anchor=NW)
canvas.create_image(3370,400, image=lead2, anchor=NW)
canvas.create_image(1340,379, image=lead2, anchor=NW)



# 
canvas.create_image(1400,525, image=lead3, anchor=NW)
canvas.create_image(2950,525, image=lead3, anchor=NW)
canvas.create_image(2700,200, image=lead3, anchor=NW)
canvas.create_image(2050,200, image=lead3, anchor=NW)
canvas.create_image(2190,170, image=lead3, anchor=NW)

# 

canvas.create_image(3660,425, image=lead4, anchor=NW)
# coin////////////////////
k = 10
for i in range(3):
    money = canvas.create_image(200+k,525, image=coin)
    k += 30
for i in range(10):
    money = canvas.create_image(410 + k, 525, image=coin)
    k += 30
# for i in range(5):
#     money = canvas.create_image(200 + k, 270, image=coin)
#     k += 30
# for i in range(6):
#     money = canvas.create_image(850 + k, 330, image=coin)
#     k += 30
# for i in range(6):
#     money = canvas.create_image(860 + k, 570, image=coin)
#     k += 30
# for i in range(6):
#     money = canvas.create_image(1050 + k, 350, image=coin)
#     k += 30
# for i in range(6):
#     money = canvas.create_image(2300 + k, 400, image=coin)
#     k += 30




# Auto-scrolling--------------------
scrollbar_bottom = Scrollbar(window, orient='horizontal', command=canvas.xview)
canvas.configure(xscrollcommand=scrollbar_bottom.set)
scrollbar_bottom.place(relx=0, rely=1, relwidth=1, anchor='sw')








window.mainloop()

