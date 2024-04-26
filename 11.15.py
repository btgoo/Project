try:
    user_input = input("Enter a number: ")
    mylist = user_input.split()
    numeric_list = [int(num) for num in mylist]
    print("List of numbers: ", numeric_list)
    try:
        user_index = int(input("Enter index number: "))
        number_on_index = numeric_list[user_index]
        print("Your number on your desired index is:", number_on_index)
    except IndexError:
        print("Error: Please enter a valid index number.")


except ValueError:
    print("Error: Please enter valid numeric values.")