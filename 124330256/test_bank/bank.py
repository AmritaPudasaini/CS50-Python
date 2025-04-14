def main():
    a = input("Greeting:")
    print(f"${value(a)}")

def value(greeting):
    greeting=greeting.lower().strip().replace(",", " ")
    total_word = greeting.split()
    word_greet = total_word[0]

    if word_greet == "hello":
        return 0

    elif word_greet.startswith("h"):
        return 20

    else:
        return 100

if __name__ =="__main__":
    main()
