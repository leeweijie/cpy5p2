# Constant to convert kilograms to pounds
kilograms_to_pounds = 2.2

# Print table heading
print("Kilograms Pounds")

# Print the 10 rows
for i in range(1, 11):
    # Print pounds to 1 d.p. and reserve white spaces after printing kilograms
    print("{0:<10}{1:.1f}".format(i, i*kilograms_to_pounds))
