numbers = []

while True:
    number = int(input("Enter your number, 'done' if you are done: "))
    if number // 2:
        numbers.append(number)
    elif number.toString() == 'done':
        continue
    else:
        continue

print(sum(numbers))
