def divisible(min, max):
    for number in range(min, max):
        if number % 21 == 0:
            print(number)

divisible(0, 1001)