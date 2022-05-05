velocity = 0
acceleration = 0.25
y = 0
jumpheight = 60
isjump = False

def fall():
    global isjump
    global y
    global velocity
    global acceleration
    global jumpheight
    velocity += acceleration
    y -= velocity
    print(y)

def main():
    global isjump
    global y
    global velocity
    global acceleration
    global jumpheight
    i = 0
    while True:
        if i == 30:
            break
        if isjump == False:
            isjump = True
            velocity = 0

        if isjump == True:
            fall()
            #if velocity == jumpheight:
                #fall()
            #if == -6:
                #isjump = False
                #v = 5
                #m = 1
                #print(y)
                #break
        i += 1

if __name__ == "__main__":
    main()