def main():
    time = (input("What time is it? "))
    meal = convert(time)

    if (7.00 <= meal <= 8.00):
        print ("breakfast time")
    elif (12.00 <= meal <= 13.00):
        print("lunch time")
    elif (18.00 <= meal <= 19.00):
        print("dinner time")


def convert(time):
    hours,minutes = time.split(":")
    meal = int(hours) + int(minutes) / 60
    return meal


if __name__ == "__main__":
    main()
