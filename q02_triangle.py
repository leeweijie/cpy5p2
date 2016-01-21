from verify_input import verify

# Enter lengths of 3 sides of triangle
side = [input("Enter side 1: "), input("Enter side 2: "), input("Enter side 3: ")]

if verify(side, "float"):
    side[0], side[1], side[2] = float(side[0]), float(side[1]), float(side[2])
    # Sort array according to magnitude of length
    side.sort()

    # Check if largest side is smaller than sum of the other 2 sides
    if side[2] < (side[0] + side[1]):
        print("Perimeter  = {0}".format(side[0] + side[1] + side[2]))
    else:
        print("Invalid triangle!")
else:
    print("Invalid input")
