def addnumber():
    total = 0
    for i in range(5):
        num = int(input(f"Enter single digit number {i+1}: "))
        if 0 < num < 10:
            total += num
        else:
            print("Please enter a valid number")

    print(f"The total is {total}")
    return total

print(addnumber)
