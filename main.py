canjump = True
jumping = False
velocity = 25
jumpheight = 60
y = 0

def main():
    global isjump
    global velocity
    global y
    global canjump
    while True:
        if canjump:
            x = input()
            if x == "jump":
                jumping = True
                canjump = False
                velocity = 25
                i = 0
        else:
            velocity = 0
        
        if jumping:
            if i <= jumpheight:
                y += velocity
                velocity -= 1
                i += 1
            else:
                jumping = False
                canjump = True

if __name__ == "__main__":
    main()