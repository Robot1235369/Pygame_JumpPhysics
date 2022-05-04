velocity = [10, 10, 8, 7, 5, 5, 4, 3, 2, 1, 1, 0, 0, 0, 0, -1, -1, -2, -3, -4, -5, -5, -7, -8, -10, -10]
y = 0
isjump = False

def main():
    global isjump
    global y
    while True:
        if isjump == False:
            isjump = True

        if isjump == True:
            F = (1 / 2) * m * (v**2)
            print(y)
            y += F
            v -= 1
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