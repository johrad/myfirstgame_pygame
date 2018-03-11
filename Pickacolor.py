def Get_Color():
    print("Give me a value between 0 and 255 for the color RED")
    while True:
        red = input(">")
        if int(red) in range(0, 256):
            break
        else:
            print("What the fuck? that's not a correct value, try again\nGive me a new value!")
            continue
        return red

    print("Give me a value between 0 and 255 for the color GREEN")
    while True:
        green = input(">")
        if int(green) in range(0, 256):
            break
        else:
            print("What the fuck? that's not a correct value, try again\nGive me a new value!")
            continue
        return green

    print("Give me a value between 0 and 255 for the color BLUE")
    while True:
        blue = input(">")
        if int(blue) in range(0, 256):
            break
        else:
            print("What the fuck? that's not a correct value, try again\nGive me a new value!")
            continue
    return blue

# NEEDS TO BE CLASS IN ORDER TO RETURN RESULT


print(str(blue))