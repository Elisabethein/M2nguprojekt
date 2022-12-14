# veel üks proov

import pygame
import os
from sys import exit
pygame.init()


WIDTH,HEIGHT = 1000, 600
fps = 60

# creating a display
screen = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption('Puuviljamäng')
clock = pygame.time.Clock()

# assets
bg= pygame.transform.scale(pygame.image.load(os.path.join('taust.jpg')), (WIDTH, HEIGHT))
ground=pygame.transform.scale(pygame.image.load('puud.png'),(WIDTH, 200))
platform = pygame.image.load('assets/alus1.png').convert_alpha()

while True:
    for event in pygame.event.get(): # exit game
        if event.type == pygame.QUIT:
            pygame.quit()
            exit() # exit the loop
    
    screen.blit(bg,(0,0)) # background
    screen.blit(ground,(0,400))

    pygame.display.update()
    clock.tick(fps)

