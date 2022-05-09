import pygame
import sys
pygame.init()

display = pygame.display.set_mode((500, 500))

FPS = 60
running = True

speed = 5
hangtime = 20
jumpheight = 100
gravity = jumpheight / ((hangtime**2) / 2)
velocity = 0
isjump = False
isfall = False

x = 225
y = 450
pygame.draw.rect(display, (255, 0, 0), (x, y, 50, 50))

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
    if isjump == False:
        if y + velocity < 450:
            isfall = True
            y += velocity
            velocity += gravity
        else:
            y = 450
            isfall = False

def update():
    global x
    global y
    display.fill((0, 0, 0))
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
    global speed
    clock = pygame.time.Clock()
    while running:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        keys = pygame.key.get_pressed()

        if keys[pygame.K_RIGHT]:
            x += speed
        if keys[pygame.K_LEFT]:
            x -= speed

        if keys[pygame.K_UP] and isjump == False and isfall == False:
            isjump = True
            starty = y
            create_vars()
        if isjump == True:
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