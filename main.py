import sys

velocity = 0
acceleration = 0.25
y = 0
jumpheight = 60
isjump = False
isfall = False

def fall():
    global isjump
    global y
    global velocity
    global acceleration
    global jumpheight
    velocity += acceleration
    y -= velocity
    print(y)
    if y == 0:
        sys.exit()

def main():
    global isjump
    global y
    global velocity
    global acceleration
    global jumpheight
    global isfall
    while True:
        if isjump == False:
            isjump = True
            velocity = 7.5
        
        if isjump == True:
            velocity -= acceleration
            y += velocity
            print(y)

            if velocity == 0:
                if isfall == False:
                    isfall = True
                    print("falling")
        if isfall == True:
            fall()
            #if velocity == jumpheight:
                #fall()
            #if == -6:
                #isjump = False
                #v = 5
                #m = 1
                #print(y)
                #break

if __name__ == "__main__":
    main()