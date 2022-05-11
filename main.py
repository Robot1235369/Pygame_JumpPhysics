import pygame
import sys
pygame.init()

display = pygame.display.set_mode((500, 500))

FPS = 60
running = True

speed = 5
hangtime = 35
jumpheight = 100
hangtime /= 2
gravity = jumpheight / ((hangtime**2) / 2)
velocity = 0
isjump = False
isfall = False
ground = 500 - 50
fastfall = False
walljump = True

x = 225
y = ground
X = x - 500
pygame.draw.rect(display, (255, 0, 0), (x, y, 50, 50))
pygame.draw.rect(display, (255, 0, 0), (X, y, 50, 50))

def create_vars():
    global hangtime
    global gravity
    global velocity
    velocity = gravity * hangtime

def fall(keys, fastfall):
    global y
    global isjump
    global gravity
    global velocity
    global jumpheight
    global hangtime
    global isfall
    global ground
    global walljump
    if isjump == False:
        if y + velocity < ground:
            if keys[pygame.K_DOWN] or fastfall == True:
                gravity *= 1.5
                fastfall = True
            isfall = True
            y += velocity
            velocity += gravity
        else:
            y = ground
            isfall = False
            gravity = jumpheight / ((hangtime**2) / 2)
            fastfall = False

def jump(keys):
    global isjump
    global y
    global gravity
    global velocity
    global fastfall
    global starty
    global speed
    global walljump
    global x
    if keys[pygame.K_UP] or keys[pygame.K_SPACE]:
        if isjump == False and isfall == False or x + speed >= 450 and walljump == True or x - speed <= 0 and walljump == True:
            isjump = True
            walljump = False
            starty = y
            create_vars()
    if isjump == True:
        if keys[pygame.K_DOWN]:
            isjump = False
            fastfall == True
        else:
            fastfall == False
            if velocity >= 0:
                y -= velocity
                velocity -= gravity
            else:
                y = starty - jumpheight
                isjump = False
                velocity = 0

def update():
    global x
    global y
    global X
    display.fill((0, 0, 0))
    pygame.draw.rect(display, (255, 0, 0), (x, y, 50, 50))
    pygame.draw.rect(display, (255, 0, 0), (X, y, 50, 50))
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
    global speed
    global X
    global keys
    global walljump
    clock = pygame.time.Clock()
    while running:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        keys = pygame.key.get_pressed()

        if keys[pygame.K_RIGHT]:
            if x + speed >= 450:
                x = 450
            else:
                x += speed
        if keys[pygame.K_LEFT]:
            if x - speed <= 0:
                x = 0
            else:
                x -= speed
        
        if x + speed < 450 and x - speed > 0:
            walljump = True
        
        jump(keys)
        fall(keys, fastfall)
        update()
    pygame.quit()

if __name__ == "__main__":
    main()
