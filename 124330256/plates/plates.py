def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    i = 2
    if 2 <= len(s) <= 6 and s.isalnum():
        if s[:2].isalpha():
            if check_rule(s):
                return True
    return False


def check_rule(s):
    i = 0
    while i < len(s):
        if s[i].isdigit():
            if not s[i:].isdigit():
                return False
            if s[i] == '0':
                return False
            break
        i += 1
    return True

main()
