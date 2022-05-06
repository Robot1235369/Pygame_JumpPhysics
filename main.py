import pygame
import sys
pygame.init()

display = pygame.display.set_mode((500, 500))

FPS = 60
running = True

hangtime = 60
jumpheight = 60
gravity = jumpheight / ((hangtime**2) / 2)
velocity = gravity * (hangtime / 2)
isjump = False
isfall = False

x = 225
y = 450
pygame.draw.rect(display, (255, 0, 0), (x, y, 50, 50))

def create_vars():
    global hangtime
    global jumpheight
    global gravity
    global velocity
    hangtime = 60
    jumpheight = 60
    gravity = jumpheight / ((hangtime**2) / 2)
    velocity = gravity * (hangtime / 2)

def fall():
    global y
    global isjump
    global gravity
    global velocity
    global jumpheight
    global hangtime
    global isfall
    if isjump == False:
        if y + velocity < 450:
            isfall = True
            y += velocity
            velocity += gravity
        else:
            y = 450
            isfall = False
            create_vars()


def update():
    global x
    global y
    display.fill(0, 0, 0)
    pygame.draw.rect(display, (255, 0, 0), (x, y, 50, 50))
    pygame.display.update()

def main():
    global x
    global y
    global isjump
    global gravity
    global velocity
    global jumpheight
    global hangtime
    global running
    global FPS
    global isfall
    clock = pygame.Clock()
    while running:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        keys = pygame.key.get_pressed()

        if keys[pygame.K_SPACE] and isjump == False and isfall == False:
            isjump = True
            starty = y
        if isjump == True:
            if y - velocity > starty - 60:
                y -= velocity
                velocity += gravity
            else:
                y = starty - 60
                isjump = False
                create_vars()
        fall()
        update()
    pygame.quit()