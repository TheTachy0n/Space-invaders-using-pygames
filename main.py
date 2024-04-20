import pygame
import math
import random

# initializing pygame
pygame.init()

# create a screen
screen = pygame.display.set_mode((800, 600))

# title and icon
pygame.display.set_caption("space invaders")
icon = pygame.image.load('001-spaceship.png')
pygame.display.set_icon(icon)

# player
playerimg = pygame.image.load('spaceshipmain.png')
playerx = 370
playery = 480
playerx_change = 0

# enemy
#multiple enemies
enemyimg = []
enemyx = []
enemyy = []
enemyx_change = []
enemyy_change = []
num_of_enemies = 6
for i in range(num_of_enemies):
    enemyimg.append(pygame.image.load('alien enemy.png'))
    enemyx.append(random.randint(0, 735))
    enemyy.append(random.randint(50, 150))
    enemyx_change.append(0.3)
    enemyy_change.append(40)


# bullet
bulletimg = pygame.image.load('bullet.png')
bulletx = 0
bullety = 480
bulletx_change = 0
bullety_change = 10
bullet_state = 0  # ready=can't see the bullet on screen#fire- bullet becomes visible

#score
score_value = 0
font = pygame.font.Font('freesansbold.ttf',32)
testx=10
testy=10
def show_score(x,y):
    score = font.render("score:" + str(score_value),True,(255,255,255))
    screen.blit(score, (x,y))

def player(x, y):
    screen.blit(playerimg, (x, y))


def enemy(x, y, i):
    screen.blit(enemyimg[i], (x, y))


def fire_bullet(x, y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bulletimg, (x + 16, y + 10))

def iscollision(enemyx,enemyy,bulletx,bullety):
    distance= math.sqrt((math.pow(enemyx-bulletx,2)) + (math.pow(enemyy-bullety,2)))
    if distance<27:
        return True
    else:
        return False

# game loop
running = True
while running:
    screen.fill((0, 0, 50))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # if keystroke is pressed check whether its left or right
        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_LEFT:

                playerx_change = -0.5
            if event.key == pygame.K_RIGHT:

                playerx_change = 0.5
            if event.key == pygame.K_SPACE:
                bulletx = playerx
                fire_bullet(bulletx, bullety)

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:

                playerx_change = 0

    # for the boundary of the player
    playerx += playerx_change

    if playerx <= 0:
        playerx = 0
    elif playerx >= 736:
        playerx = 736
    # for the boundary of the enemy
    for i in range(num_of_enemies):
        enemyx[i] += enemyx_change[i]
        if enemyx[i] <= 0:
            enemyx_change[i] = 0.5
            enemyy[i] += enemyy_change[i]
        elif enemyx[i] >= 736:
            enemyx_change[i] = -0.5
            enemyy[i] += enemyy_change[i]
         # collision
        collision = iscollision(enemyx[i], enemyy[i], bulletx, bullety)
        if collision:
            bullety = 480
            bullet_state = "ready"
            score_value += 1
            enemyx[i] = random.randint(0, 735)
            enemyy[i] = random.randint(50, 150)
        enemy(enemyx[i], enemyy[i], i)

    #bullet movement
    if bullety <=0:
        bullety=480
        bullet_state="ready"

    if bullet_state is "fire":
        fire_bullet(bulletx,bullety)
        bullety -= bullety_change


    player(playerx, playery)
    show_score(testx,testy)
    pygame.display.update()
