import pygame
from sys import exit

pygame.init()#alustab
screen=pygame.display.set_mode((1200, 600))#window suurus,,, See tundub suht norm isegi?LAIUSxKÕRGUS
pygame.display.set_caption('Puuviljamäng')#pealkiri
clock=pygame.time.Clock()
proovifont=pygame.font.Font("Desktop/Mänguprojekt/alagard.ttf", 50)

taust=pygame.image.load('Desktop/Mänguprojekt/manutaust-1.png.png').convert()

plika=pygame.image.load('Desktop/Mänguprojekt/piksliplika/tegelane1-1.png.png').convert_alpha()#100x141 reso vist, ja tundub parim
plika_rect=plika.get_rect(midbottom=(50, 300))

puud=pygame.image.load('Desktop/Mänguprojekt/puudkindel-1.png.png').convert_alpha()
puud2=puud
puude_positsioon=0

banaan=pygame.image.load('Desktop/Mänguprojekt/pikslipuuviljad/puuviljad-2.png.png').convert_alpha()


tekst=proovifont.render('Puuviljaseiklus', False, 'Black')
tekst2=proovifont.render('Puuviljaseiklus', False, 'Brown')


alus1=pygame.image.load('Desktop/Mänguprojekt/alus1.png').convert_alpha()
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


while True:#mäng töötab kogu aeg ja lõppeb kui exit
    for event in pygame.event.get():
        if event.type==pygame.QUIT:#suudab quitida
            pygame.quit()
            exit()
    screen.blit(taust,(0,0))
    #screen.blit(plika, plika_rect)#paneb ruue surface kuhugi
    puude_positsioon-=1
    if puude_positsioon<-1200: puude_positsioon=0
    screen.blit(pygame.transform.scale(puud, (1200,348)), (puude_positsioon,250))
    #screen.blit(banaan, (300,50))
    screen.blit(tekst, (450, 50))#Mängu nimi nt üles äärde?
    screen.blit(tekst2, (453,50))
    screen.blit(pygame.transform.scale(puud2, (1200,348)),(puude_positsioon+1200, 250))

    #vääääääga palju kordusi
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
    alus1_pos-=1
    if alus1_pos<-1165: alus1_pos=1235
    alus2_pos-=1
    if alus2_pos<-980: alus2_pos=1420
    alus3_pos-=1
    if alus3_pos<-760: alus3_pos=1640
    alus4_pos-=1
    if alus4_pos<-425: alus4_pos=1975
    alus5_pos-=1
    if alus5_pos<-170: alus5_pos=2230
    alus11_pos-=1
    if alus11_pos<-1165: alus11_pos=1235
    alus22_pos-=1
    if alus22_pos<-980: alus22_pos=1420
    alus33_pos-=1
    if alus33_pos<-760: alus33_pos=1640
    alus44_pos-=1
    if alus44_pos<-425: alus44_pos=1975
    alus55_pos-=1
    if alus55_pos<-170: alus55_pos=2230


    pygame.display.update()
    clock.tick(90)#mängukiirus

#panna pildid samasse faili et displayd muuta