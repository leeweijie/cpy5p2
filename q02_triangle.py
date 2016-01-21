from verify_input import verify

# Enter lengths of 3 sides of triangle
side = [input("Enter side {0}: ".format(i)) for i in range(3)]

if verify(side, "float"):
    # Convert strings in list to arrays
    side = [float(i) for i in side]
    # Sort array according to magnitude of length
    side.sort()
    # Check if largest side is smaller than sum of the other 2 sides
    if side[2] < (side[0] + side[1]):
        # Calculate perimeter and print it
        print("Perimeter  = {0}".format(sum(side)))
    else:
        print("Invalid triangle!")
else:
    print("Invalid input")
