def main():
    s = input("Input: ")
    s = shorten(s)
    print(s)

def shorten(word):
    word = word.replace("a","").replace("e","").replace("i","").replace("o","").replace("u","").replace("A","").replace("E","").replace("I","").replace("O","").replace("U","").strip()
    return word

if __name__ == "__main__":
    main()
