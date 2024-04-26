import random

def calculate_birthday_duplication_probability(trial, people):
    num_duplications = 0
    for x in range(trial):
        birthdays = []

        for i in range(people):
            days = random.randint(1, 365)
            birthdays.append(days)

        noduplication = set(birthdays)

        if len(noduplication) != len(birthdays):
            num_duplications += 1

    probability = (num_duplications / trial) * 100
    return probability

trial = int(input("Trial: "))
people = 23

probability = calculate_birthday_duplication_probability(trial, people)
print(f"Probability of at least one shared birthday among {people} people: {probability:.2f}%")