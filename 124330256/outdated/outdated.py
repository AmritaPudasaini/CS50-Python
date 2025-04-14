months = ["January", "February", "March", "April", "May", "June","July", "August", "September", "October", "November", "December"]

while True:
    date_input = input("Date: ").strip()

    if "/" in date_input:
        try:
            month, day, year = date_input.split("/")

            month = int(month)
            day = int(day)
            year = int(year)

            if 1 <= month <= 12 and 1 <= day <= 31:
                print(f"{year:04}-{month:02}-{day:02}")
                break
        except ValueError:
            pass

    elif "," in date_input:
        try:
            parts = date_input.split(" ")

            if len(parts) == 3:
                month_name = parts[0]
                day = parts[1].replace(",", "")
                year = parts[2]

                if month_name in months:
                    month = months.index(month_name) + 1
                    day = int(day)
                    year = int (year)

                    if 1 <= day <= 31:
                        print(f"{year:04}-{month:02}-{day:02}")
                        break
        except (ValueError, IndexError):
            pass
    else:
        pass
