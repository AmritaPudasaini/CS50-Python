import sys

def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
        sys.exit(0)
    else:
        print("Invalid")
        sys.exit(1)


def is_valid(s):
    i = 2
    if 2 <= len(s) <= 6 and s.isalnum():
        if s.isalpha():
            return True
        for i in range (len(s)):
            if s[i].isdigit():
                break
        part1=s[:i]
        part2=s[i:]
        if part2[0]!='0' and part2[2].isdigit() and part1.isalpha():
            return True
        else:
            return False

if __name__ == "__main__":
    main()
