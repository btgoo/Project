import random

num_duplications = 0
bdays = []

for x in range(23):
    bday = random.randint(1, 365)
    bdays.append(bday)

noduplication = set(bdays)

if len(bdays) != len(bdays):
    num_duplications += 1

probability = (num_duplications / 23) * 100

print(f"{probability:.2f}%")
