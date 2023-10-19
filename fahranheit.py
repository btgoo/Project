# First, the user will be prompted to choose whether they want to convert c to f or f to c.
choice = input("Enter 'C' to convert from Celsius to Fahrenheit or 'F' to convert from Fahrenheit to Celsius: ").upper()

# If the user entered C, the program will convert celsius to fahranheit and print it.
if choice == "C":
    celsius = float(input('Enter temperature in celsius: '))
    fahranheit = celsius * 1.8 + 32
    print("Fahranheit: ", fahranheit)
# If the user entered F, the program will convert fahranheit to celsius and print it.
elif choice == "F":
    fahranheit = float(input('Enter temperature in fahranheit: '))
    celsius = (fahranheit - 32) * 5/9
    print("Celsius: ", celsius)
# If the user doesn't enter neither c nor f, the program will print this.
else:
    print('Enter either C or F')