# Check if inputs are numbers and convert them to floats
def process_input():
    global side
    try:
        for i in range(3):  # Did not use "for i in side" so as to keep track of array index
            side[i] = float(side[i])
        return True
    except ValueError:
        return False

# Enter lengths of 3 sides of triangle
side = [input("Enter side 1: "), input("Enter side 2: "), input("Enter side 3: ")]

if process_input():
    # Sort array according to magnitude of length
    side.sort()

    # Check if largest side is smaller than sum of the other 2 sides
    if side[2] < (side[0]+side[1]):
        print("Perimeter  = {0}".format(side[0]+side[1]+side[2]))
    else:
        print("Invalid triangle!")
else:
    print("Invalid input")



