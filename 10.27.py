# importing random library in order to generate random integers
import random

num_duplications = 0
for day in range(10000):
    birthdays = []

    i = 1
    while i <= 23:
        days = random.randint(1, 365)
        i += 1
        birthdays.append(days)

    noduplication = set(birthdays)

    if len(noduplication) != len(birthdays):
        num_duplications += 1

probability = (num_duplications / 10000) * 100

print(f"{probability:.2f}%")
