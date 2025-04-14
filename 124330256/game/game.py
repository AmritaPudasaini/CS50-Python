import random

number = random.randint(1,100)
while True:
    try:
        num = int(input("Level: "))
        if num > 0:
            break
    except ValueError:
        pass

while True:
    try:
        guess = int(input("Guess: "))
        if number>guess:
            print("Too small!")
        elif number<guess:
            print("Too large!")
        else:
            print("Just right!")
            break

    except ValueError:
        pass
