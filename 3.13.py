# Question 1

# def find_min_coins(amount):
#     coins = [200, 100, 50, 20, 10, 5, 2, 1]
#     approved_coins = []
#     for coin in coins:
#         while amount >= coin:
#             approved_coins.append(coin)
#             amount -= coin
#     return approved_coins
#
# def pound_to_pence(amount):
#     return (amount * 100)
#
#
# amount_in_pounds = 1.28
# amount_in_pence = pound_to_pence(amount_in_pounds)
# coins = find_min_coins(amount_in_pence)
#
# print(f"Smallest number of coins needed to make up {amount_in_pence}")
# for coin in coins:
#     print(f"£{coin/100:.2f}")

# Question 2
def get_first_element(item):
    return item[0]

items = [
    [10, 400],
    [25, 2000],
    [17, 1200]
]

sorted_items = sorted(items, key=get_first_element)

# Get the sum of the first values
sum_of_two_values = sum(item[0] + item[1] for item in sorted_items)
