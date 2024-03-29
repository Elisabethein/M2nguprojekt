import pygame
from sys import exit
import time
pygame.init()

# teha : pikenda mängu natuke peale viimase puuvilja kogumist, siis end screen 
#        pane hüppama plankude peal ja game over screen

# muutsin puude tausta nime

# suurused
fps = 90
WIDTH, HEIGHT = 1200,600        # gamewindow suurus
c_width, c_height = 250, 300    # poisi tegelaskuju suurus

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Puuviljamäng')
clock = pygame.time.Clock()

wasp = pygame.image.load('assets/character-nupp.png').convert_alpha()

# assetid
proovifont=pygame.font.Font("assets/alagard.ttf", 50)

# algusekraanil
algus=pygame.image.load('assets/final-scroll-ver2.png').convert_alpha() #scroll
button1=pygame.image.load('assets/character-nupp.png').convert_alpha()  #character nupp
button1_rect=button1.get_rect(topleft=(440, 450))
button2=pygame.image.load('assets/start-nupp.png').convert_alpha()      #stardi nupp
button2_rect=button2.get_rect(topleft=(600,450))
game_active=1                                    #märgib seda et alguses oleks üks ekraan


taust=pygame.image.load('assets/manutaust-1.png.png').convert()

tegelane='tüdruk' # character screeni jaoks
player1=pygame.image.load('assets/piksliplika/plika1.png').convert_alpha()
player2=pygame.image.load('assets/piksliplika/plika2.png').convert_alpha()
player3=pygame.image.load('assets/piksliplika/plika3.png').convert_alpha()
player4=pygame.image.load('assets/piksliplika/plika4.png').convert_alpha()

# animatsioon 
player_kõnd=[player1, player2]
player_index=0
plika=player_kõnd[player_index] #100x141 reso vist, ja tundub parim
plika_rect=plika.get_rect(midbottom=(50, 300))
plika_gravity=0

tWalkLeft = []
tWalkRight = []

# boy asstets, kas panen .convert_alpha() lõppu?
poiss=pygame.image.load('assets/p-seisab.png')
p1 = pygame.transform.scale(pygame.image.load('assets/p-k6nnib1.png'), (c_width,c_height))
p2 = pygame.transform.scale(pygame.image.load('assets/p-k6nnib2&hyppab.png'), (c_width,c_height))
p3= pygame.transform.scale(pygame.image.load('assets/p-k6nnib3.png'), (c_width,c_height))
p4= pygame.transform.scale(pygame.image.load('assets/p-k6nnib4.png'), (c_width,c_height))
# poisi animatsiooni list
walkRight = [p1,p2,p3,p4,p1,p2,p3,p4,p1]
walkLeft = [p1,p2,p3,p4,p1,p2,p3,p4,p1] # walkleft vajab flippimist!

#puude taust
puud=pygame.image.load('puud.png').convert_alpha()
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

#alused, saab ilma kordamata ka v?
alus1=pygame.image.load('assets/alus1.png').convert_alpha()
alus1_pos=35
alus2=alus1
alus2_pos=220
alus3=alus1
alus3_pos=440
alus4=alus1
alus4_pos=775
alus5=alus1
alus5_pos=1030

alus11=alus1
alus11_pos=1235
alus22=alus1
alus22_pos=1420
alus33=alus1
alus33_pos=1640
alus44=alus1
alus44_pos=1975
alus55=alus1
alus55_pos=2230

#lõpuekraan
lõpp=pygame.image.load('outro.png').convert_alpha()
gameover = pygame.image.load('game-over.jpg').convert_alpha()

while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:     # mäng kinni
            pygame.quit()
            exit()
            
        if game_active:
            if event.type==pygame.KEYDOWN:#võimalik on teha üks hüpe ja double-jump aga kui tegelane on juba õhus kõrgel siis ei saa hüpata rohkem
                if event.key==pygame.K_SPACE and plika_rect.top>=0:
                    plika_gravity=-12

        if event.type==pygame.MOUSEBUTTONDOWN:
            if button2_rect.collidepoint(event.pos):
                game_active=2
            if button1_rect.collidepoint(event.pos):
                if tegelane=='tüdruk':
                    tegelane='poiss'
                    continue
                elif tegelane=='poiss':
                    tegelane='tüdruk'
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

        #SKOOR
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

        if viljacounter==5:#kui kõik koos, on mäng läbi
            time.sleep(0.2)
            game_active=3

        #alused, KAS SEE PeAB NII PIKK OLEMA?
        screen.blit(pygame.transform.scale(alus1, (100, 25)), (alus1_pos, 350))
        screen.blit(pygame.transform.scale(alus2, (100, 25)), (alus2_pos, 350))
        screen.blit(pygame.transform.scale(alus3, (100, 25)), (alus3_pos, 325))
        screen.blit(pygame.transform.scale(alus4, (100, 25)), (alus4_pos, 300))
        screen.blit(pygame.transform.scale(alus5, (100, 25)), (alus5_pos, 300))
        screen.blit(pygame.transform.scale(alus11, (100, 25)), (alus11_pos, 350))
        screen.blit(pygame.transform.scale(alus22, (100, 25)), (alus22_pos, 350))
        screen.blit(pygame.transform.scale(alus33, (100, 25)), (alus33_pos, 325))
        screen.blit(pygame.transform.scale(alus44, (100, 25)), (alus44_pos, 300))
        screen.blit(pygame.transform.scale(alus55, (100, 25)), (alus55_pos, 300))
        alus1_pos-=2
        if alus1_pos<-1165: alus1_pos=1235
        alus2_pos-=2
        if alus2_pos<-980: alus2_pos=1420
        alus3_pos-=2
        if alus3_pos<-760: alus3_pos=1640
        alus4_pos-=2
        if alus4_pos<-425: alus4_pos=1975
        alus5_pos-=2
        if alus5_pos<-170: alus5_pos=2230
        alus11_pos-=2
        if alus11_pos<-1165: alus11_pos=1235
        alus22_pos-=2
        if alus22_pos<-980: alus22_pos=1420
        alus33_pos-=2
        if alus33_pos<-760: alus33_pos=1640
        alus44_pos-=2
        if alus44_pos<-425: alus44_pos=1975
        alus55_pos-=2
        if alus55_pos<-170: alus55_pos=2230
        
        #tegelane
        # player_animation()

        plika_gravity+=0.5
        plika_rect.y+=plika_gravity
        if plika_rect.bottom>=300:
            plika_rect.bottom=300
        screen.blit(plika, plika_rect)

    if game_active==3:#lõpuekraan
        screen.blit(taust, (0,0))
        screen.blit(pygame.transform.scale(lõpp,(532, 600)), (330,0))

    if game_active== 4: # game over screen
        screen.blit(pygame.transform.scale(gameover,(WIDTH,HEIGHT)))



    pygame.display.update()
    clock.tick(fps)#mängukiirus