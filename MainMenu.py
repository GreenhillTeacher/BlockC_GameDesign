#MAria Suarez
#MAke the Main Menu 
#width  the text, mouse position



import pygame, time,os
os.system('cls')
pygame.init()
#variables, constants, and objects
WIDTH=700
HEIGHT=700
xs=20
ys=120
wb=40
hb=40
yT=10
xT=0

square=pygame.Rect(xs,ys,wb,hb )
# bg=pygame.image.load('bgSmaller.jpg')

#Messages
message=''
MainMenu=['Instructions', 'Settings','Level I','Level II','Level III','Sce','Exit']
#define colors Dictionary dictio={key: values}
colors={'red':[255,0,0],'white':[255,255,255],'mag':[255,0,255],
'aqua':[51,153,255],'m':[47,192,229],'navy':[5,31,64],'pink':[200,3,75]}
background= colors.get('white')
sq_c= colors.get('pink')
Title_color=colors.get('navy')

#create different FNTS
TITLE_FNT=pygame.font.SysFont('comicsans', 80)
MENU_FNT=pygame.font.SysFont('comicsans', 40)
INST_FNT=pygame.font.SysFont('comicsans', 15)

#create screen
window=pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption('Circle Eats Square')

#CREATE TITLES
title=TITLE_FNT.render('MENU', 1, Title_color)
xT=WIDTH/2-title.get_width()/2
window.fill(background)
window.blit(title,(xT,yT))

#create Square
for message in MainMenu:

    pygame.draw.rect(window,sq_c, square)
    
    text=MENU_FNT.render(message,1,Title_color)
    window.blit(text,(square.x+wb+10,square.y-5))
    square.y +=75


pygame.display.update()
xm=0
ym=0
check=True
while check:
    # window.blit(bg,(0,0))
    # window.fill(background)
    move=10
    for case in pygame.event.get():
        if case.type == pygame.QUIT:
            check=False
    if case.type==pygame.MOUSEBUTTONDOWN:
        mouse_pos=pygame.mouse.get_pos()
        print(type(mouse_pos ))
        xm=mouse_pos[0]
        ym=mouse_pos[1]
    if xm>=20 and xm<60 and ym>=120 and ym<160 :
        window.fill(background)
        #add instruct title




    pygame.display.update()