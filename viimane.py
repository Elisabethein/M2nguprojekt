import pygame
from sys import exit
import time
pygame.init()


# suurused
fps = 90
WIDTH, HEIGHT = 1200,600        # gamewindow suurus
c_width, c_height = 95,125      # poisi tegelaskuju suurus

# algväärtused
kõnd = 0
tegelane='tüdruk'   # character screeni jaoks
plika_gravity=0
p_gravity=0
k = 4               # tausta kiirus


screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Puuviljamäng')
clock = pygame.time.Clock()



###########################################                 ASSETID                   ###################################################


proovifont=pygame.font.Font("assets/alagard.ttf", 50)                   # font

# algusekraanil
algus=pygame.image.load('assets/final-scroll-ver2.png').convert_alpha() #scroll
button1=pygame.image.load('assets/character-nupp.png').convert_alpha()  #character nupp
button1_rect=button1.get_rect(topleft=(440, 450))
button2=pygame.image.load('assets/start-nupp.png').convert_alpha()      #stardi nupp
button2_rect=button2.get_rect(topleft=(600,450))
game_active=1                                                           #märgib seda et alguses oleks üks ekraan

# herilased
wasp = pygame.transform.scale(pygame.image.load('wasp.png'),(70,80)).convert_alpha()
wasp_rect=wasp.get_rect(midbottom=(8100,150))
wasp2,wasp3,wasp4,wasp5,wasp6 = wasp,wasp,wasp,wasp,wasp
wasp2_rect=wasp.get_rect(topleft=(2485,230))
wasp3_rect=wasp.get_rect(topleft=(4000,300))
wasp4_rect=wasp.get_rect(topleft=(5060,230))
wasp5_rect=wasp.get_rect(topleft=(6700,150))
wasp6_rect=wasp.get_rect(topleft=(7500,300))
l = [wasp_rect,wasp2_rect,wasp3_rect,wasp4_rect,wasp5_rect,wasp6_rect]

# tegelased
plika=pygame.image.load('assets/piksliplika/plika1.png').convert_alpha()
t1=pygame.image.load('assets/piksliplika/plika1.png').convert_alpha()
t2=pygame.image.load('assets/piksliplika/plika2.png').convert_alpha()
t3=pygame.image.load('assets/piksliplika/plika3.png').convert_alpha()
t4=pygame.image.load('assets/piksliplika/plika4.png').convert_alpha()
t_jump = t4
t_walk = [t1,t3,t2]
t=t_walk[kõnd]
#tWalkRight=[t1,t1,t1,t1,t1,t1,t1,t1,t3,t3,t3,t3,t3,t3,t3,t3,t2,t2,t2,t2,t2,t2,t2,t2]
tWalkRight=[t1,t2,t3,t4,t1,t2,t3,t4,t1,t2,t3,t4,t1]
plika_rect=t.get_rect(midbottom=(50, 350))

# boy asstets, .convert_alpha() lõppu
poiss=pygame.image.load('assets/p-seisab.png')
p1 = pygame.transform.scale(pygame.image.load('p-k6nnib1.png'), (c_width,c_height)).convert_alpha()
p2 = pygame.transform.scale(pygame.image.load('p-k6nnib2&hyppab.png'), (c_width,c_height)).convert_alpha()
p3= pygame.transform.scale(pygame.image.load('p-k6nnib3.png'), (c_width,c_height)).convert_alpha()
p4= pygame.transform.scale(pygame.image.load('p-k6nnib4.png'), (c_width,c_height)).convert_alpha()

p_walk = [p1,p2,p3,p4]
p_jump = p2
p=p_walk[kõnd]
walkRight = [p1,p2,p3,p4,p1,p2,p3,p4,p1,p2,p3,p4,p1]
p_rect=p.get_rect(midbottom=(50, 350))

#puude taust
taust=pygame.image.load('assets/manutaust-1.png.png').convert()
puud=pygame.image.load('puud2.png').convert_alpha()
puud2=puud
puude_positsioon=0

#puuviljad
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
apelsinide_arv=0 # võtab ainult ühe korra skoori

#pealkiri
tekst=proovifont.render('Puuviljaseiklus', False, 'Black')  # teksti vari
tekst2=proovifont.render('Puuviljaseiklus', False, 'Brown') # tekst
tekst3=proovifont.render('GAME OVER', False, 'Brown')       # game over tekst

# skoori jaoks
väikebanaan=pygame.image.load('assets/pikslipuuviljad/puuviljad-2.png.png').convert_alpha()
väikebanaan_rect=väikebanaan.get_rect(midright=(100, 60))

#lõpuekraan
# lõpp=pygame.image.load('assets/outro.png').convert_alpha()
lõpp=pygame.image.load('outro-cropped.png').convert_alpha() # võit
gameover = pygame.image.load('game-over.jpg').convert_alpha() # kaotus



###################################                ASSETID                 ###################################################




# skoor
viljacounter=0
def skoor(viljacounter):
    puuvilju=proovifont.render(str(viljacounter)+'00', False, 'Brown')
    puuvilju_rect=puuvilju.get_rect(midleft=(100, 60))
    screen.blit(pygame.transform.scale(puuvilju, (50, 30)), (58,18))

# animatsioon
def animation(kumb):
    global t, p, kõnd

    if kumb == 'tüdruk':
        print('tüdruk')
        if plika_rect.bottom < 360:
            t = t_jump 
        else:
            kõnd += 0.05
            if kõnd >= len(t_walk):
                kõnd=0
            t = t_walk[int(kõnd)]
        
    if kumb == 'poiss':
        print('poiss')
        if p_rect.bottom < 360:
            p = p_jump
        else:
            kõnd += 0.05
            if kõnd >= len(p_walk):
                kõnd=0
            p = p_walk[int(kõnd)]


# main
while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:     # mäng kinni
            pygame.quit()
            exit()
            
        if game_active:
            if event.type==pygame.KEYDOWN: # võimalik on teha üks hüpe ja double-jump aga kui tegelane on juba õhus kõrgel siis ei saa hüpata rohkem
                if event.key==pygame.K_SPACE and plika_rect.top>=0:
                    plika_gravity=-15
                if event.key==pygame.K_SPACE and p_rect.top>=0:
                    p_gravity= -15

        if event.type==pygame.MOUSEBUTTONDOWN: # chrcter select tegelasevahetus 
            if button2_rect.collidepoint(event.pos):
                game_active=2
            if button1_rect.collidepoint(event.pos):
                if tegelane=='tüdruk':
                    tegelane='poiss'
                    player = 'tüdruk'
                    continue
                elif tegelane=='poiss':
                    tegelane='tüdruk'
                    player = 'poiss'
                    continue


    if game_active==1: # alguse ekraan
        screen.blit(taust, (0,0))
        screen.blit(pygame.transform.scale(algus,(532, 600)), (330,0))
        screen.blit(pygame.transform.scale(button1, (150,64)), button1_rect)
        screen.blit(pygame.transform.scale(button2, (150,64)), button2_rect)
        if tegelane=='tüdruk':
            screen.blit(pygame.transform.scale(plika, (90, 143)), (542, 300))
        elif tegelane=='poiss':
            screen.blit(pygame.transform.scale(poiss, (90, 143)), (542, 300))


    if game_active==2: # päris mäng
        #taust
        screen.blit(taust,(0,0))
        #puude osa:
        puude_positsioon-=k
        if puude_positsioon<-1200: puude_positsioon=0
        screen.blit(pygame.transform.scale(puud, (1200,348)), (puude_positsioon,250))
        screen.blit(pygame.transform.scale(puud2, (1200,348)),(puude_positsioon+1200, 250))
        # skoor
        screen.blit(pygame.transform.scale(väikebanaan, (30,30)), väikebanaan_rect)
        screen.blit(tekst, (450, 50))   # pealkiri
        screen.blit(tekst2, (453,50))   # vari

        #puuviljad
        if banaanide_arv == 0: screen.blit(pygame.transform.scale(banaan, (80, 91)), banaan_rect)
        banaan_rect.x-=k
        if ananasside_arv == 0: screen.blit(pygame.transform.scale(ananass, (76, 100)), ananass_rect)
        ananass_rect.x-=k
        if apelsinide_arv == 0: screen.blit(pygame.transform.scale(apelsin, (80, 80)), apelsin_rect)
        apelsin_rect.x-=k
        if maasikate_arv == 0: screen.blit(pygame.transform.scale(maasikas, (80, 98)), maasikas_rect)
        maasikas_rect.x-=k
        if sidrunite_arv == 0: screen.blit(pygame.transform.scale(sidrun, (74, 86)), sidrun_rect)
        sidrun_rect.x-=k
        
        # herilased
        screen.blit(wasp, wasp_rect)
        wasp_rect.x-=k*1.5
        screen.blit(wasp2,  wasp2_rect)
        wasp2_rect.x-=k*1.5
        screen.blit(wasp3, wasp3_rect)
        wasp3_rect.x-=k*1.5
        screen.blit(wasp4, wasp4_rect)
        wasp4_rect.x-=k*1.5
        screen.blit(wasp5, wasp5_rect)
        wasp5_rect.x-=k*1.5
        screen.blit(wasp6, wasp6_rect)
        wasp6_rect.x-=k*1.5



        # COLLISION JA SKOOR

        if player == 'tüdruk':
            if plika_rect.colliderect(banaan_rect) and banaanide_arv==0:
                banaanide_arv+=1
                viljacounter+=1
            if plika_rect.colliderect(ananass_rect) and ananasside_arv==0:
                ananasside_arv+=1
                viljacounter+=1
            if plika_rect.colliderect(maasikas_rect) and maasikate_arv==0:
                maasikate_arv+=1
                viljacounter+=1
            if plika_rect.colliderect(sidrun_rect) and sidrunite_arv==0:
                sidrunite_arv+=1
                viljacounter+=1
            if plika_rect.colliderect(apelsin_rect) and apelsinide_arv==0:
                apelsinide_arv+=1
                viljacounter+=1
            skoor(viljacounter)

            for herilane in l:
                    if plika_rect.colliderect(herilane):
                        print('kokkupõrge herilasega')
                        game_active=4

            if plika_rect.x >= 6500:
                print('out of bounds')
                game_active=4

            
        elif player == 'poiss':
            if p_rect.colliderect(banaan_rect) and banaanide_arv==0:
                banaanide_arv+=1
                viljacounter+=1
            if p_rect.colliderect(ananass_rect) and ananasside_arv==0:
                ananasside_arv+=1
                viljacounter+=1
            if p_rect.colliderect(maasikas_rect) and maasikate_arv==0:
                maasikate_arv+=1
                viljacounter+=1
            if p_rect.colliderect(sidrun_rect) and sidrunite_arv==0:
                sidrunite_arv+=1
                viljacounter+=1
            if p_rect.colliderect(apelsin_rect) and apelsinide_arv==0:
                apelsinide_arv+=1
                viljacounter+=1
            skoor(viljacounter)

            for herilane in l:
                if p_rect.colliderect(herilane):
                    print('kokkupõrge herilasega')
                    game_active=4

            if p_rect.x >= 6500:
                print('out of bounds')
                game_active=4


        if viljacounter==5: # kui kõik koos, on mäng läbi
            time.sleep(0.2)
            game_active=3

        # tegelase animatsioon

        if player ==  'tüdruk':
            plika_gravity+=0.5
            plika_rect.y+=plika_gravity
            if plika_rect.bottom>=360:
                plika_rect.bottom=360
            animation('tüdruk')
            screen.blit(t, plika_rect)
        
        elif player == 'poiss':
            p_gravity+=0.5
            p_rect.y+=p_gravity
            if p_rect.bottom>=360:
                p_rect.bottom=360
            animation('poiss')
            screen.blit(p, p_rect)


    
    if game_active==3: # win screen 
        time.sleep(0.5)
        screen.blit(taust, (0,0))
        screen.blit(pygame.transform.scale(lõpp,(240*3.5,175*3.5)),(WIDTH/2-120*3.5,HEIGHT/2-88*3.5))
        pygame.display.update()
        print('Palju õnne, olete mängu võitnud!')
        time.sleep(5)
        pygame.quit()
        exit()

    if game_active== 4: # game over screen
        time.sleep(1)
        screen.blit(pygame.transform.scale(gameover,(WIDTH,HEIGHT)),(0,0))
        pygame.display.update()
        print('Seekord kaotasite, proovige uuesti!')
        time.sleep(3.5)
        pygame.quit()
        exit()

    pygame.display.update()
    clock.tick(fps) # mängukiirus


    # sizing
# x_centered = screen_width / 2 - image_width / 2
# y_centered = screen_height / 2 - image_height / 2 #similarly..