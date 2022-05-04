velocity = 0
acceleration = 0.25
y = 0
isjump = False

def main():
    global isjump
    global y
    while True:
        if isjump == False:
            isjump = True
            velocity = 

        if isjump == True:
            velocity += acceleration
            if v < 0:
                m = -1
            if v == -6:
                isjump = False
                v = 5
                m = 1
                print(y)
                break

if __name__ == "__main__":
    main()