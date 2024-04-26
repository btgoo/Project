# # Using the Force formula F=ma
# # Refactor by creating a function that tests whether an inputted
# # value is positive or not. Use this to record the inputted
# # mass, acceleration and to print the force
#
# while True:
#     mass = int(input("Enter the mass value: "))
#     if mass > 0:
#         break
# while True:
#     acceleration = int(input("Enter the acceleration:"))
#     if acceleration > 0:
#         break
# print("The Force is", mass * acceleration)
#
# # Refactor by using a list comprehension instead of
# # for loop
#
# numbers = [1, 2, 3, 4, 5, 6, 7, 8]
# odd_numbers = []
# for item in numbers:
#     if item % 2 == 1:  # % gives remainder from division
#         odd_numbers.append(item)
# print(odd_numbers)
#
# # Use a ternary operator (evaluates if condition is True ot False
# # instead of if-else statements
#
# to_check = int(input("Enter a whole number :"))
# msg = ""
# if (to_check % 2 == 0):
#     msg = "even"
# else:
#     msg = "odd"
# print("The number you entered is an", msg, "number")
#
# # Use enumerate function instead of range
# # enumerate adds a counter as a key for each object
# colors = ["white", "black", "brown"]
# for i in range(len(colors)):
#     print(i + 1, colors[i])

"Rock-Paper-Scissors Refactoring"
while True:  # allows loop to repeat continuously
    player1 = ""
    while player1 not in ["rock", "paper", "scissors"]:
        player1 = input("player1 make your move (rock, paper, scissors): ")
    player2 = ""
    while player2 not in ["rock", "paper", "scissors"]:
        player2 = input("player2 make your move (rock, paper, scissors): ")
    winner_message = ""
    if player1 == player2:
        winner_message = "The outcome is a tie"
    elif player1 == "rock" and player2 == "scissors":
        winner_message = "player1 is the winner"
    elif player1 == "paper" and player2 == "rock":
        winner_message = "player1 is the winner"
    elif player1 == "scissors" and player2 == "paper":
        winner_message = "player1 is the winner"
    elif player2 == "rock" and player1 == "scissors":
        winner_message = "player2 is the winner"
    elif player2 == "paper" and player1 == "rock":
        winner_message = "player2 is the winner"
    elif player2 == "scissors" and player1 == "paper":
        winner_message = "player2 is the winner"
    print(winner_message)
    again = ""
    while again not in ["y", "n"]:
        again = input("Do you want to play again? (y/n): ")
    if again == "n":
        break

# look for repeated blocks, create functions for these
# are there repeated check within the if/else statements?