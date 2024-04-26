def factorial():
    n = int(input("Enter the integer: "))
    # define the result as 1
    result = 1
    # x for the while loop
    x = 1
    while x <= n:
        result = result * x
        x += 1
    return result

print(factorial())


