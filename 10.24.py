print("Hello...")

stop_words = {"a", "an", "the", "in", "on", "at", "to", "of"}
common_endings = {"s", "es", "ed", "ing"}
index = {}
line_number = 0

print("Enter text line by line. Type a '.' when finished: ")

while True:
    line = input()
    line_number += 1

    if line == ".":
        break

words = line.lower().split()
words = [word.strip(".,!?()[]") for word in words]

for word in words:
    if word not in stop_words:
