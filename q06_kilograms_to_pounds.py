# Constant to convert kilograms to pounds
kilograms_to_pounds = 2.2

# Print table heading
print("Kilograms Pounds")
# Iterate through the rows and print it
print("{0:<10}{1:.1f}".format(i, i * kilograms_to_pounds) for i in range(1, 11))
