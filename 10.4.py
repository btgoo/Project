while True:
    item = str(input("Enter your word (or stop): "))
    if item.lower() == 'stop':
        break
    else:
        length = len(item)
        print("The length of the word:", length, "character")