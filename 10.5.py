input_list = []

while True:
    item = float(input("Enter a number: "))
    input_list.append(item)
    if input("Do you want to finish? (yes/no): ").lower() == "yes":
        break

result = sum(input_list)
print("Sum of the list values:", result)
