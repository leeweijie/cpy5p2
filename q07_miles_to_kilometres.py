# Constant to convert mile to kilometres
mile_to_kilometres = 1.609

# Print table heading
print("Miles Kilometres Kilometres Miles")

# Print the 10 rows
for i in range(1, 11):

    # Get value of kilometres for 3rd column
    kilometres = 20+(i-1)*5

    # Convert the values and print
    print("{0:<6}{1:<11.3f}{2:<11}{3:.3f}".format(i, i*mile_to_kilometres, kilometres, kilometres/mile_to_kilometres))
