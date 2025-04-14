import pyfiglet
import random
import sys

def main():
    font_list = pyfiglet.Figlet().getFonts()


    if len(sys.argv) == 3:

        if sys.argv[1] == '-f' or sys.argv[1] == '--font':

            if sys.argv[2] in font_list:
                word = input("Input: ")
                output = pyfiglet.figlet_format(word, sys.argv[2])
                print(output)

            else:
                sys.exit("Invalid font name")

        else:
            sys.exit("Invalid Usage")

    elif len(sys.argv) == 1:
        word = input("Input: ")
        output = pyfiglet.figlet_format(word, random.choice(font_list))
        print(output)

    else:
        sys.exit("Invalid Usage")

if __name__ == "__main__":
    main()
