total = 0

for i in range(1):
    while True:
        user_input = input(f"Enter number between 0 and 9: ")
        if user_input.isdigit() and 0 <= int(user_input) <= 9:
            total += int(user_input)
            break
        print("Invalid input. Please enter a number between 0 and 9.")

print(f"Total: {total}")