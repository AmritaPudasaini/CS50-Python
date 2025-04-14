from validators import email

def main():
    print(valid_email(input("Povide your email address: ")))


def valid_email(s):
    if email(s):
        return 'Valid'
    else:
        return 'Invalid'



if __name__ == "__main__" :
    main()
