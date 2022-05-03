isjump = False
velocity = 25
jumpheight = 50
y = 0

def jump():
    global isjump
    global velocity
    global y
    if not isjump:
        for i in range(jumpheight):
            y += velocity
            velocity -= 1
            print(y)

print(y)
jump()
print(y)