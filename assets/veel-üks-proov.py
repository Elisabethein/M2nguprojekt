import pygame
import os
pygame.init()

# suurused

fps = 27
c_width, c_height = 250, 300
WIDTH, HEIGHT = 1000,700
x = 200
y = 100
vel = 10
tausta_kiirus = 4

isJump = False
jumpCount = 10
left = False
right = False
walkCount = 0

win = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption('Puuviljamäng')
clock = pygame.time.Clock()


# assetid
# kõigile võib .convert_alpha() taha panna

tegelane='poiss'
t1=pygame.transform.scale(pygame.image.load('assets/piksliplika/plika1.png'), (c_width,c_height))
t2=pygame.transform.scale(pygame.image.load('assets/piksliplika/plika2.png'), (c_width,c_height))
t3=pygame.transform.scale(pygame.image.load('assets/piksliplika/plika3.png'), (c_width,c_height))
t4=pygame.transform.scale(pygame.image.load('assets/piksliplika/plika4.png'), (c_width,c_height))
tseisab=pygame.transform.scale(pygame.image.load('assets/piksliplika/plika1.png'), (c_width,c_height))
tWalkRight=[t1,t1,t2,t2,t3,t3,t4,t4,t1]
tWalkLeft=[t1,t2,t3,t4,t1,t2,t3,t4,t1]
t_rect=t1.get_rect()

poiss=pygame.image.load('assets/p-seisab.png')
p1 = pygame.transform.scale(pygame.image.load('assets/p-k6nnib1.png'), (c_width,c_height))
p2 = pygame.transform.scale(pygame.image.load('assets/p-k6nnib2&hyppab.png'), (c_width,c_height))
p3= pygame.transform.scale(pygame.image.load('assets/p-k6nnib3.png'), (c_width,c_height))
p4= pygame.transform.scale(pygame.image.load('assets/p-k6nnib4.png'), (c_width,c_height))
# poisi animatsiooni list
walkRight = [p1,p2,p3,p4,p1,p2,p3,p4,p1]
walkLeft = [p1,p2,p3,p4,p1,p2,p3,p4,p1]
p_rect=tseisab.get_rect(topleft=(x,y))

# taustal
bg= pygame.transform.scale(pygame.image.load(os.path.join('taust.jpg')), (WIDTH, HEIGHT))
seisab= pygame.transform.scale(pygame.image.load(os.path.join('p-seisab.png')), (c_width,c_height))
puud=pygame.image.load('puud.png').convert_alpha()
platvorm = pygame.image.load('assets/alus1.png').convert_alpha()
platvorm_x = 200

# viljad 
banaan=pygame.image.load('assets/pikslipuuviljad/puuviljad-2.png.png').convert_alpha()
banaan_rect=banaan.get_rect(midbottom=(1285, 345))
banaanide_arv=0
ananass=pygame.image.load('assets/pikslipuuviljad/puuviljad-6.png.png').convert_alpha()
ananass_rect=ananass.get_rect(midbottom=(2485,345))
ananasside_arv=0
maasikas=pygame.image.load('assets/pikslipuuviljad/puuviljad-5.png.png').convert_alpha()
maasikas_rect=maasikas.get_rect(midbottom=(6085, 345))#3685
maasikate_arv=0
sidrun=pygame.image.load('assets/pikslipuuviljad/puuviljad-4.png.png').convert_alpha()
sidrun_rect=sidrun.get_rect(midbottom=(4885, 345))
sidrunite_arv=0
apelsin=pygame.image.load('assets/pikslipuuviljad/puuviljad-3.png.png').convert_alpha()
apelsin_rect=apelsin.get_rect(midbottom=(3685, 345))#6085
apelsinide_arv=0
viljad=[banaan,ananass,maasikas,sidrun,apelsin]

# stardiekraan

# algusekraan
algus=pygame.image.load('assets/final-scroll-ver2.png').convert_alpha()#scroll
button1=pygame.image.load('assets/character-nupp.png').convert_alpha()#character nupp
button1_rect=button1.get_rect(topleft=(440, 450))
button2=pygame.image.load('assets/start-nupp.png').convert_alpha()#stardi nupp
button2_rect=button2.get_rect(topleft=(600,450))
game_active=1 # märgib seda et alguses oleks üks ekraan


# lõpuekraan
lõpp=pygame.image.load('assets/lõpuke.png').convert_alpha() # võit
 # game over
gameover = pygame.image.load('game-over.jpg').convert_alpha() # kaotus


# kas on platvormil?

def on_platform():
    print('platvormi loop')

# mängu kood
def redrawGameWindow():
    global walkCount
    win.blit(bg,(0,0)) #taust
    win.blit(platvorm,(platvorm_x,300))
    
    if walkCount +1>=12:
        walkCount = 0

    if tegelane =='poiss':
        if right:
            win.blit(walkRight[walkCount//3], (x,y))
            walkCount += 1
        elif left:
            win.blit(walkLeft[walkCount//3], (x,y))
            walkCount += 1
        else:
            win.blit(seisab, (x,y))

    elif tegelane =='tüdruk':
        if right:
            win.blit(tWalkRight[walkCount//3], (x,y))
            walkCount += 1
        elif left:
            win.blit(tWalkLeft[walkCount//3], (x,y))
            walkCount += 1
        else:
            win.blit(tseisab, (x,y))

    pygame.display.update()


# main loop
run = True
while run:
    clock.tick(fps)
    platvorm_x=platvorm_x-tausta_kiirus # platvorm liigub

    if platvorm_x < -100: platvorm_x = WIDTH # pane asjad ekraanil loopima

    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            
    keys = pygame.key.get_pressed()
    if keys[pygame.K_a] and x > vel:
        x -= vel
        left = True
        right = False
    elif keys[pygame.K_d] and x < WIDTH-c_width-vel:
        x += vel
        left = False
        right = True
    else:                   # meek seisab
        right = False
        left = False
        walkCount = 0
        
    if not(isJump):
        if keys[pygame.K_SPACE]:
            isJump = True
            right = False
            left = False
            walkCount =0           
    else:
        if jumpCount >= -10:
            neg = 1
            if jumpCount < 0:
                neg = -1
            y -= (jumpCount **2)* 0.5 * neg
            jumpCount -=1 
        else:
            isJump = False
            jumpCount = 10
    
    redrawGameWindow()

pygame.quit()
    

