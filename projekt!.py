import pygame
from sys import exit

pygame.init()#alustab
screen=pygame.display.set_mode((1200, 600))#window suurus,,, See tundub suht norm isegi?LAIUSxKÕRGUS
pygame.display.set_caption('Puuviljamäng')#pealkiri
clock=pygame.time.Clock()
proovifont=pygame.font.Font("Desktop/Mänguprojekt/alagard.ttf", 50)

taust=pygame.image.load('Desktop/Mänguprojekt/manutaust-1.png.png').convert()
plika=pygame.image.load('Desktop/Mänguprojekt/piksliplika/tegelane1-1.png.png').convert_alpha()#100x141 reso vist, ja tundub parim
puud=pygame.image.load('Desktop/Mänguprojekt/puudkindel-1.png.png').convert_alpha()
puud2=puud
banaan=pygame.image.load('Desktop/Mänguprojekt/pikslipuuviljad/puuviljad-2.png.png').convert_alpha()
tekst=proovifont.render('Puuviljaseiklus', False, 'Black')
tekst2=proovifont.render('Puuviljaseiklus', False, 'Brown')
puude_positsioon=0


while True:#mäng töötab kogu aeg ja lõppeb kui exit
    for event in pygame.event.get():
        if event.type==pygame.QUIT:#suudab quitida
            pygame.quit()
            exit()
    screen.blit(taust,(0,0))
    screen.blit(plika,(150,200))#paneb ruue surface kuhugi
    puude_positsioon-=1
    if puude_positsioon<-1200: puude_positsioon=0
    screen.blit(puud, (puude_positsioon,250))
    screen.blit(banaan, (300,50))
    screen.blit(tekst, (450, 50))#Mängu nimi nt üles äärde?
    screen.blit(tekst2, (453,50))
    screen.blit(puud2,(puude_positsioon+1200, 250))
    pygame.display.update()
    clock.tick(60)#mängukiirus

#panna pildid samasse faili et displayd muuta