list = []

while True:
    item = input("Enter a word (or 'done' to finish): ")
    list.append(item)
    if item.lower() == "done":
            break

new_list = [item for item in list if len(item) > 5]  

for word in new_list:
    if word[0] == word[len(word) - 1]:
        print(len(new_list))