import re
import sys


def main():
    try:
        print(convert(input("Hours: ")))
    except ValueError:
        sys.exit("ValueError")


def convert(s):
    time_result = re.search(r"(\d+)(?::(\d+))? (AM|PM) to (\d+)(?::(\d+))? (AM|PM)", s)

    if time_result:
        groups = list(time_result.groups())

        for i in range(len(groups)):
            if groups[i] is None:
                groups[i] = '00'

        start_hour, start_minute = int(groups[0]), int(groups[1])
        start_period = groups[2]
        end_hour, end_minute = int(groups[3]), int(groups[4])
        end_period = groups[5]

        if not (1 <= start_hour <= 12) or not (1 <= end_hour <= 12):
            raise ValueError("Invalid hour value")
        if not (0 <= start_minute < 60) or not (0 <= end_minute < 60):
            raise ValueError("Invalid minute value")

        start_hour_24 = convert_to_24_hour(start_hour, start_period)
        end_hour_24 = convert_to_24_hour(end_hour, end_period)

        return f"{start_hour_24:02}:{start_minute:02} to {end_hour_24:02}:{end_minute:02}"

    else:
        raise ValueError("Invalid input format")


def convert_to_24_hour(hour, period):
    if period == "AM" and hour == 12:
        return 0
    elif period == "PM" and hour != 12:
        return hour + 12
    return hour


if __name__ == "__main__":
    main()
