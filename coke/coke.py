due = 50

while due > 0:
    print(f"Amount Due: {due}")

    coin = int(input("Insert Coin: "))

    if coin in [5, 10, 25]:
            due -= coin
    else:
            print(f"Amount Due: {due}")

if due < 0:
     print(f"Change Owed: {abs(due)}")
else:
    print("Change Owed: 0")
