from datetime import date, datetime
import inflect
import sys

def main():
        birth_date = input("Date of Birth: ")
        print(intoMinute(birth_date))


def intoMinute(birth_date):
    try:
        today = date.today()
        date_str = birth_date.split("-")
        birth = date(int(date_str[0]), int(date_str[1]), int(date_str[2]))
        days = today - birth
        day = days.days
        minute = day*24*60
        p = inflect.engine()
        result = p.number_to_words(minute).capitalize()
        result = result.replace(" and", "")
        return result+" minutes"

    except ValueError:
        sys.exit("Invalid Date")


if __name__ == "__main__":
    main()
