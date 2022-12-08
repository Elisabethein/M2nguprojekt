import pygame
import os
pygame.init()

# suurused

fps = 36
c_width, c_height = 250, 300
WIDTH, HEIGHT = 1000,700
x = 50
y = 400
vel = 10

isJump = False
jumpCount = 10
left = False
right = False
walkCount = 0

win = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption('Puuviljamäng')
clock = pygame.time.Clock()


# assetid

p1 = pygame.transform.scale(pygame.image.load(os.path.join('p-k6nnib1.png')), (c_width,c_height))
p2 = pygame.transform.scale(pygame.image.load(os.path.join('p-k6nnib2&hyppab.png')), (c_width,c_height))
p3= pygame.transform.scale(pygame.image.load(os.path.join('p-k6nnib3.png')), (c_width,c_height))
p4= pygame.transform.scale(pygame.image.load(os.path.join('p-k6nnib4.png')), (c_width,c_height))

bg= pygame.transform.scale(pygame.image.load(os.path.join('taust.jpg')), (WIDTH, HEIGHT))
seisab= pygame.transform.scale(pygame.image.load(os.path.join('p-seisab.png')), (c_width,c_height))

walkRight = [p1,p2,p3,p4,p1,p2,p3,p4,p1]
walkLeft = [p1,p2,p3,p4,p1,p2,p3,p4,p1]

# mängu kood
def redrawGameWindow():
    global walkCount
    win.blit(bg,(0,0)) #taust
    
    if walkCount +1>=12:
        walkCount = 0
        
    if right:
        win.blit(walkRight[walkCount//3], (x,y))
        walkCount += 1
    elif left:
        win.blit(walkLeft[walkCount//3], (x,y))
        walkCount += 1
    else:
        win.blit(seisab, (x,y))
    pygame.display.update()

# main loop
run = True
while run:
    clock.tick(fps)
    
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
    else:
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
    
