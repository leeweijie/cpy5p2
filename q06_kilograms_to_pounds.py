kilograms_to_pounds = 2.2

print("Kilograms Pounds")
for i in range(1,11):
    pounds = i*kilograms_to_pounds
    print("{0:<10}{1:.1f}".format(i, pounds))
