import pygame
from sys import exit

pygame.init()#alustab
screen=pygame.display.set_mode((1000, 600))#window suurus,,, See tundub suht norm isegi?
pygame.display.set_caption('Puuviljamäng')#pealkiri
clock=pygame.time.Clock()

taust=pygame.image.load('Desktop/staff/pxArt.png')
proov=pygame.image.load('Desktop/staff/tegelane3.1.png')#64x90 reso vist, ja tundub parim

# proov=pygame.Surface((200,100))
# proov.fill('green')

while True:#mäng töötab kogu aeg ja lõppeb kui exit
    for event in pygame.event.get():
        if event.type==pygame.QUIT:#suudab quitida
            pygame.quit()
            exit()
    screen.blit(taust,(0,0))
    screen.blit(proov,(0,0))#paneb ruue surface kuhugi

    pygame.display.update()
    clock.tick()#mängukiirus

#panna pildid samasse faili et displayd muuta