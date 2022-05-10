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

def fall():
    global y
    global isjump
    global gravity
    global velocity
    global jumpheight
    global hangtime
    global isfall
    global ground
    if isjump == False:
        if y + velocity < ground:
            isfall = True
            y += velocity
            velocity += gravity
        else:
            y = ground
            isfall = False

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
    clock = pygame.time.Clock()
    while running:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        keys = pygame.key.get_pressed()

        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            x += speed
        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            x -= speed

        if  isjump == False and isfall == False and keys[pygame.K_UP] or keys[pygame.K_SPACE] and isjump == False and isfall == False:
            isjump = True
            starty = y
            create_vars()
        if isjump == True:
            if keys[pygame.K_DOWN]:
                isjump = False
            else:
                if velocity >= 0:
                    y -= velocity
                    velocity -= gravity
                else:
                    y = starty - jumpheight
                    isjump = False
                    velocity = 0
        fall()
        update()
    pygame.quit()

if __name__ == "__main__":
    main()