price = int(input("Price: "))

if price < 0:
    print("Wrong amount")
elif price < 49:
    print(price)
elif 50 < price < 100:
    print(price - price*0.05)
elif 101 < price < 200:
    print(price - price*0.1)
elif price > 200:
    print(price - price*0.15)
