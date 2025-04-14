k = input("Item: ").title()

d = {"Apple":"130",
    "Avocado":"50",
    "Sweet Cherries":"100",
    "Kiwifruit":"90",
    "Pear":"100"
    }
if k in d:
    print("Calories:", d[k])
