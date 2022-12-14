import pygame
pygame.init()

win = pygame.display.set_mode((1200, 600))

clock = pygame.time.Clock()

class Player(object):
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.vel = 5
        self.left = False
        self.right = False
        self.walk_count = 0
        self.is_jumping = False
        self.jump_count = 10
        self.standing = False
        self.idle = True
        self.hitbox = (self.x + 10, self.y + 15, 50, 47)

    def draw(self, win):
        self.hitbox = (self.x + 10, self.y + 15, 50, 47)
        pygame.draw.rect(win, (255,0,0), self.hitbox, 2)

    def land(self):
        self.y = stick.hitbox[0] - self.hitbox[0]
        self.is_jumping = False
        self.jump_count = 10
        self.x = 800
        self.y = 410 - self.height + 4

class Platform(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.hitbox = (self.x, self.y, 104, 5, 2)

    def draw(self, win):
        pygame.draw.rect(win, (255, 255, 255), (self.x, self.y, 104, 5))
        self.hitbox = (self.x, self.y, 104, 2)


# DRAW FUNCTION
def redraw_game_window():
    win.fill((0, 0, 0))
    stick.draw(win)
    george.draw(win)
    pygame.display.update()


# MAIN LOOP
font = pygame.font.SysFont('arial', 32, True)
stick = Platform(800, 410)
george = Player(50, 525, 64, 64)
running = True

while running:
    clock.tick(27)

    if george.is_jumping:
        if george.hitbox[0] + george.hitbox[2] < stick.hitbox[0] + stick.hitbox[2] and george.hitbox[0] + george.hitbox[2] > stick.hitbox[0]:
            if george.hitbox[1] + george.hitbox[3] < stick.hitbox[1] and george.hitbox[1] + george.hitbox[3] > 390:
                george.land()
                print('land')
    if george.jump_count == 10 and george.y == 410 - george.height + 4:
        if george.hitbox[0] + george.hitbox[2] < stick.hitbox[0] or george.hitbox[0] > stick.hitbox[0] + stick.hitbox[2]:
            george.is_jumping = True
            george.jump_count = -10

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT] and george.x > george.vel:
        george.x -= george.vel
        george.left = True
        george.right = False
        george.standing = False
        george.idle = False
    elif keys[pygame.K_RIGHT] and george.x < 1200 - (george.width + george.vel):
        george.x += george.vel
        george.left = False
        george.right = True
        george.standing = False
        george.idle = False
    else:
        george.walk_count = 0
        george.standing = True

    if not(george.is_jumping):
        if keys[pygame.K_UP]:
            george.is_jumping = True
            george.walk_count = 0
            george.idle = False
    else:
        if george.jump_count >= -10:
            george.y -= (george.jump_count * abs(george.jump_count)) * 0.5
            george.jump_count -= 1
            george.standing = False
        else:
            george.is_jumping = False
            george.jump_count = 10

    redraw_game_window()

pygame.quit()