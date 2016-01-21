# Constant to convert kilograms to pounds
kilograms_to_pounds = 2.2

print("Kilograms Pounds")
for i in range(1, 11):
    pounds = i * kilograms_to_pounds

    # Print pounds to 1 d.p. and reserve white spaces after printing kilograms
    print("{0:<10}{1:.1f}".format(i, pounds))
