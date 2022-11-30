import pygame
from sys import exit
import time

pygame.init()#alustab
screen=pygame.display.set_mode((1200, 600))#window suurus,,, See tundub suht norm isegi?LAIUSxKÕRGUS
pygame.display.set_caption('Puuviljamäng')#pealkiri
clock=pygame.time.Clock()
proovifont=pygame.font.Font("Desktop/Mänguprojekt/assets/alagard.ttf", 50)

#struktuur?:
#while True loop
    #game_active on false ja seal on see algus, niikaua kui pole start vajutatud, on see screen
    #game_active on True kui vajutad start
        #kui saad puuviljad kätte, see loop lõppeb ja tuleb lõpu ekraan
        #lõpu screen, palju õnne juhuuu



algus=pygame.image.load('Desktop/Mänguprojekt/assets/final-scroll-ver2.png').convert_alpha()
button1=pygame.image.load('Desktop/Mänguprojekt/assets/character-nupp.png').convert_alpha()
button1_rect=button1.get_rect(topleft=(440, 450))
button2=pygame.image.load('Desktop/Mänguprojekt/assets/start-nupp.png').convert_alpha()
button2_rect=button2.get_rect(topleft=(600,450))
game_active=False

    
# def player_animation():
#     global plika, player_index
#     if plika_rect.bottom<300:
#         plika=player3
#     else:

taust=pygame.image.load('Desktop/Mänguprojekt/assets/manutaust-1.png.png').convert()

tegelane='tüdruk'
player1=pygame.image.load('Desktop/Mänguprojekt/assets/piksliplika/plika1.png').convert_alpha()
player2=pygame.image.load('Desktop/Mänguprojekt/assets/piksliplika/plika2.png').convert_alpha()
player_kõnd=[player1, player2]
player_index=0
player3=pygame.image.load('Desktop/Mänguprojekt/assets/piksliplika/plika3.png').convert_alpha()
player4=pygame.image.load('Desktop/Mänguprojekt/assets/piksliplika/plika4.png').convert_alpha()
plika=player_kõnd[player_index]#100x141 reso vist, ja tundub parim
plika_rect=plika.get_rect(midbottom=(50, 300))
plika_gravity=0

poiss=pygame.image.load('Desktop/Mänguprojekt/assets/p-seisab.png')

puud=pygame.image.load('Desktop/Mänguprojekt/assets/puudkindel-1.png.png').convert_alpha()
puud2=puud
puude_positsioon=0

banaan=pygame.image.load('Desktop/Mänguprojekt/assets/pikslipuuviljad/puuviljad-2.png.png').convert_alpha()
banaan_rect=banaan.get_rect(midright=(100, 60))

tekst=proovifont.render('Puuviljaseiklus', False, 'Black')
tekst2=proovifont.render('Puuviljaseiklus', False, 'Brown')

viljacounter=0
puuvilju=proovifont.render(str(viljacounter)+'00', False, 'Brown')
puuvilju_rect=puuvilju.get_rect(midleft=(100, 60))
# puuvilju1=proovifont.render('100', False, 'Brown')
# puuvilju2=proovifont.render('200', False, 'Brown')
# puuvilju3=proovifont.render('300', False, 'Brown')
# puuvilju4=proovifont.render('400', False, 'Brown')
# puuvilju5=proovifont.render('500', False, 'Brown')


alus1=pygame.image.load('Desktop/Mänguprojekt/assets/alus1.png').convert_alpha()
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

while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:#suudab quitida
            pygame.quit()
            exit()
        if game_active:
            if event.type==pygame.KEYDOWN:#võimalik on teha üks hüpe ja double-jump aga kui tegelane on juba õhus kõrgel siis ei saa hüpata rohkem
                if event.key==pygame.K_SPACE and plika_rect.top>=0:
                    plika_gravity=-15
        # if event.type==pygame.MOUSEMOTION:
        if event.type==pygame.MOUSEBUTTONDOWN:
            if button2_rect.collidepoint(event.pos):
                game_active=True
            if button1_rect.collidepoint(event.pos):
                if tegelane=='tüdruk':
                    tegelane='poiss'
                    continue
                elif tegelane=='poiss':
                    tegelane='tüdruk'
                    continue

    if game_active==False:
        screen.blit(taust, (0,0))
        screen.blit(pygame.transform.scale(algus,(532, 600)), (330,0))
        screen.blit(pygame.transform.scale(button1, (150,64)), button1_rect)
        screen.blit(pygame.transform.scale(button2, (150,64)), button2_rect)
        if tegelane=='tüdruk':
            screen.blit(pygame.transform.scale(plika, (90, 143)), (542, 300))
        elif tegelane=='poiss':
            screen.blit(pygame.transform.scale(poiss, (90, 143)), (542, 300))

    if game_active:
        #taust
        screen.blit(taust,(0,0))
        #puude osa:
        puude_positsioon-=2
        if puude_positsioon<-1200: puude_positsioon=0
        screen.blit(pygame.transform.scale(puud, (1200,348)), (puude_positsioon,250))
        screen.blit(pygame.transform.scale(puud2, (1200,348)),(puude_positsioon+1200, 250))
        #tekstide osa:
        screen.blit(pygame.transform.scale(banaan, (30,30)), banaan_rect)
        screen.blit(pygame.transform.scale(puuvilju, (50, 30)), (58,18))

        screen.blit(tekst, (450, 50))
        screen.blit(tekst2, (453,50))
        #alused
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


    pygame.display.update()
    clock.tick(90)#mängukiirus