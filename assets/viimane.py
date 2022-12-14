import pygame
from sys import exit
import time
pygame.init()


# suurused
fps = 90
WIDTH, HEIGHT = 1200,600        # gamewindow suurus
c_width, c_height = 100, 150    # poisi tegelaskuju suurus
walkCount = 0

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Puuviljamäng')
clock = pygame.time.Clock()

# assetid
proovifont=pygame.font.Font("assets/alagard.ttf", 50)

# algusekraanil
algus=pygame.image.load('assets/final-scroll-ver2.png').convert_alpha() #scroll
button1=pygame.image.load('assets/character-nupp.png').convert_alpha()  #character nupp
button1_rect=button1.get_rect(topleft=(440, 450))
button2=pygame.image.load('assets/start-nupp.png').convert_alpha()      #stardi nupp
button2_rect=button2.get_rect(topleft=(600,450))
game_active=1                                    #märgib seda et alguses oleks üks ekraan


wasp = pygame.transform.scale(pygame.image.load('wasp.png'),(80,120)).convert_alpha()
wasp_rect=wasp.get_rect(midbottom=(230,150))
wasp2,wasp3,wasp4 = wasp,wasp,wasp
wasp2_rect=wasp.get_rect(topleft=(2485,345))
wasp3_rect=wasp.get_rect(topleft=(4000,100))
wasp4_rect=wasp.get_rect(topleft=(5060,200))
taust=pygame.image.load('assets/manutaust-1.png.png').convert()
l = [wasp_rect,wasp2_rect,wasp3_rect,wasp4_rect]

tegelane='tüdruk' # character screeni jaoks
player='tüdruk'
player1=pygame.image.load('assets/piksliplika/plika1.png').convert_alpha()
player2=pygame.image.load('assets/piksliplika/plika2.png').convert_alpha()
player3=pygame.image.load('assets/piksliplika/plika3.png').convert_alpha()
player4=pygame.image.load('assets/piksliplika/plika4.png').convert_alpha()

# animatsioon 
player_kõnd=[player1, player2]
player_index=0
plika=player_kõnd[player_index] #100x141 reso vist, ja tundub parim
plika_rect=plika.get_rect(midbottom=(50, 350))
plika_gravity=0

p_gravity=0

tegelane='tüdruk'
t1=pygame.image.load('assets/piksliplika/plika1.png').convert_alpha()
t2=pygame.image.load('assets/piksliplika/plika2.png').convert_alpha()
t3=pygame.image.load('assets/piksliplika/plika3.png').convert_alpha()
t4=pygame.image.load('assets/piksliplika/plika4.png').convert_alpha()

tWalkRight=[t1,t1,t1,t3,t3,t3,t2,t2,t2]


# boy asstets, kas panen .convert_alpha() lõppu?
poiss=pygame.image.load('assets/p-seisab.png')
p1 = pygame.transform.scale(pygame.image.load('assets/p-k6nnib1.png'), (c_width,c_height))
p2 = pygame.transform.scale(pygame.image.load('assets/p-k6nnib2&hyppab.png'), (c_width,c_height))
p3= pygame.transform.scale(pygame.image.load('assets/p-k6nnib3.png'), (c_width,c_height))
p4= pygame.transform.scale(pygame.image.load('assets/p-k6nnib4.png'), (c_width,c_height))
# poisi animatsiooni list
walkRight = [p1,p2,p3,p4,p1,p2,p3,p4,p1]

p_rect=poiss.get_rect(topleft=(50, 350))

#puude taust
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
tekst=proovifont.render('Puuviljaseiklus', False, 'Black') # teksti vari
tekst2=proovifont.render('Puuviljaseiklus', False, 'Brown') # tekst

#skoor
viljacounter=0
def skoor(viljacounter):
    puuvilju=proovifont.render(str(viljacounter)+'00', False, 'Brown')
    puuvilju_rect=puuvilju.get_rect(midleft=(100, 60))
    screen.blit(pygame.transform.scale(puuvilju, (50, 30)), (58,18))

väikebanaan=pygame.image.load('assets/pikslipuuviljad/puuviljad-2.png.png').convert_alpha()
väikebanaan_rect=väikebanaan.get_rect(midright=(100, 60))

#lõpuekraan
lõpp=pygame.image.load('assets/lõpuke.png').convert_alpha() # võit
gameover = pygame.image.load('game-over.jpg').convert_alpha() # kaotus

while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:     # mäng kinni
            pygame.quit()
            exit()
            
        if game_active:
            if event.type==pygame.KEYDOWN:#võimalik on teha üks hüpe ja double-jump aga kui tegelane on juba õhus kõrgel siis ei saa hüpata rohkem
                if event.key==pygame.K_SPACE and plika_rect.top>=0:
                    plika_gravity=-20
                    p_gravity= -20
        
        walkCount += 1

        if event.type==pygame.MOUSEBUTTONDOWN: # chrcter select tegelasevahetus 
            if button2_rect.collidepoint(event.pos):
                game_active=2
            if button1_rect.collidepoint(event.pos):
                if tegelane=='tüdruk':
                    tegelane='poiss'
                    player = 'poiss'
                    continue
                elif tegelane=='poiss':
                    tegelane='tüdruk'
                    player = 'tüdruk'
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
        puude_positsioon-=2
        if puude_positsioon<-1200: puude_positsioon=0
        screen.blit(pygame.transform.scale(puud, (1200,348)), (puude_positsioon,250))
        screen.blit(pygame.transform.scale(puud2, (1200,348)),(puude_positsioon+1200, 250))
        #tekstide osa:
        screen.blit(pygame.transform.scale(väikebanaan, (30,30)), väikebanaan_rect)
        screen.blit(tekst, (450, 50))#pealkiri
        screen.blit(tekst2, (453,50))#vari
        #puuviljad
        screen.blit(pygame.transform.scale(banaan, (80, 91)), banaan_rect)
        banaan_rect.x-=2
        screen.blit(pygame.transform.scale(ananass, (76, 100)), ananass_rect)
        ananass_rect.x-=2
        screen.blit(pygame.transform.scale(apelsin, (80, 80)), apelsin_rect)
        apelsin_rect.x-=2
        screen.blit(pygame.transform.scale(maasikas, (80, 98)), maasikas_rect)
        maasikas_rect.x-=2
        screen.blit(pygame.transform.scale(sidrun, (74, 86)), sidrun_rect)
        sidrun_rect.x-=2
        
        # herilased
        screen.blit(wasp, wasp_rect)
        wasp_rect.x-=2
        screen.blit(wasp2,  wasp2_rect)
        wasp2_rect.x-=2
        screen.blit(wasp3, wasp3_rect)
        wasp3_rect.x-=2
        screen.blit(wasp4, wasp4_rect)
        wasp4_rect.x-=2



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


        if viljacounter==5:#kui kõik koos, on mäng läbi
            time.sleep(0.2)
            game_active=3

        # collision herilasega

        if walkCount +1>=12:
            walkCount = 0

        #tegelane
        # player_animation()
        if player ==  'tüdruk':
            plika_gravity+=0.5
            plika_rect.y+=plika_gravity
            if plika_rect.bottom>=300:
                plika_rect.bottom=300
            screen.blit(tWalkRight[walkCount//3], plika_rect)
        if player == 'poiss':
            p_gravity+=0.5
            p_rect.y+=p_gravity
            if p_rect.bottom>=300:
                p_rect.bottom=300
            screen.blit(walkRight[walkCount//3], p_rect)

    if game_active==3:#lõpuekraan
        time.sleep(1)
        screen.blit(taust, (0,0))
        screen.blit(pygame.transform.scale(lõpp,(532, 600)), (330,0))

    if game_active== 4: # game over screen
        time.sleep(1)
        screen.blit(pygame.transform.scale(gameover,(WIDTH,HEIGHT)),(0,0))



    pygame.display.update()
    clock.tick(fps) # mängukiirus