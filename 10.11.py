def check_passphrase():
    correct_passphrase = "i love chocolate"

    while True:
        user_passphrase = input("Enter the passphrase: ")

        if user_passphrase == correct_passphrase:
            return "Passphrase is correct. Access granted!"

        print("Incorrect passphrase. Please try again.")

result = check_passphrase()
print(result)