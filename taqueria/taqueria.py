item = {
    "Baja Taco": 4.25,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}

i = 0

while True:
    try:
        a = input("Item: ").title().strip()
        i = i+item[a]
        print(f"Total: ${i:.2f}")
    except EOFError:
        print()
        break
    except KeyError:
        pass
