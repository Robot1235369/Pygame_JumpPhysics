m = 1
v = 5
y = 0
isjump = False

def main():
    global isjump
    global v
    global m
    global y
    while True:
        if isjump == False:
            isjump = True

        if isjump == True:
            F = (1 / 2) * m * (v**2)
            y += F
            print(y)
            v -= 1
            if v < 0:
                m = -1
            if v == -6:
                isjump = False
                v = 5
                m = 1

if __name__ == "__main__":
    main()