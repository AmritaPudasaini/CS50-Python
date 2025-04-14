def main():
    x = int(get_input())

    if x<=1:
        print("E")
    elif x>=99:
        print("F")
    else:
        print(f"{x}%")


def get_input():
    while True:
        try:
            z =  input("Fraction: ")
            x,y = z.split("/")
            if int(x)>int(y):
                continue
            else:
                return float((int(x) * 100 / int(y)))
        except (ValueError, ZeroDivisionError):
            pass

main()
