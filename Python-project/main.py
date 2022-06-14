


Number = int(input("Please enter any number: "))

if Number < 0:
    print("Error: Number must be positive.")
else:
    sum = 0
    i = Number
    while i > 0:
        sum += i
        i -= 1
    print("Sum of all Positive numbers till", Number, "is", sum )