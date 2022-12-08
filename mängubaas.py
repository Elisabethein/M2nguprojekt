

import pygame
import os

pygame.init()

WIDTH, HEIGHT = 1200,700
WIN = pygame.display.set_mode((WIDTH,HEIGHT))
vel = 5

pygame.display.set_caption('puuviljamäng')
white = (255,255,255)
fps = 27

# kõndimine

left = False
right = False
walkCount = 0

p1_image = pygame.image.load(os.path.join('p-k6nnib1.png'))
p2_image = pygame.image.load(os.path.join('p-k6nnib2&hyppab.png'))
bg = pygame.image.load(os.path.join('taust.jpg'))
seisab = pygame.image.load(os.path.join('p-seisab.png'))
p3 = pygame.image.load(os.path.join('p-k6nnib3.png'))
p4 = pygame.image.load(os.path.join('p-k6nnib4.png'))

#resize the image
p_width, p_height = 250, 300
p1_image= pygame.transform.scale(p1_image, (p_width,p_height))
p2_image= pygame.transform.scale(p2_image, (p_width,p_height))
bg= pygame.transform.scale(bg, (WIDTH, HEIGHT))
seisab= pygame.transform.scale(seisab, (p_width,p_height))
p3= pygame.transform.scale(p3, (p_width,p_height))
p4= pygame.transform.scale(p4, (p_width,p_height))

walkRight = [p1_image,p2_image,p3,p4]
walkLeft = [p1_image,p2_image,p3,p4]

def draw_window(poiss):
    global walkCount
    WIN.blit(bg,(0,0)) #taust
    if walkCount +1>=27:
        walkCount = 0
    if right:
        win.blit(p1_image[walkCount//3], (poiss.x,poiss.y))
        walkcount += 1
    elif left:
        win.blit(p2_image[walkCount//3], (poiss.x,poiss.y))
        walkcount += 1
    else:
        win.blit(seisab, (poiss.x,poiss.y))
    
        
        
    #WIN.blit(p1_image, (poiss.x,poiss.y)) #draw a surface onto the screen
    pygame.display.update()
    
    
def poiss_movement(keys_pressed, poiss):
    if keys_pressed[pygame.K_a] and poiss.x > vel:
        poiss.x -= vel
        left = True
        right = False
    elif keys_pressed[pygame.K_d] and poiss.x < WIDTH:
        poiss.x += vel
        left = False
        right = True
    else:
        right = False
        left = False
        walkCount = 0
        
    if keys_pressed[pygame.K_w] and poiss.y:
            poiss.y -= vel
    if keys_pressed[pygame.K_s] and poiss.y:
            poiss.y += vel

#main game loop
def main():
    #POISI ASUKOHT
    poiss = pygame.Rect(100,100, p_width, p_height)
    
    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(fps)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                
        keys_pressed = pygame.key.get_pressed()
        poiss_movement(keys_pressed,poiss)
        draw_window(poiss)
    
    pygame.quit()
    
if __name__ == "__main__":
    main()
    