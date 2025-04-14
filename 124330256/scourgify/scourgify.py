import sys
import csv

try:
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")

    with open(sys.argv[1], "r") as before_file:
        with open(sys.argv[2], "w", newline="") as after_file:
            reader = csv.DictReader(before_file)
            writer = csv.DictWriter(after_file, fieldnames=["first","last","house"])
            writer.writeheader()

            for row in reader:
                if "name" in row and "house" in row:
                    if ", " in row["name"]:
                        last, first = row["name"].split(", ")
                        writer.writerow({"first": first.strip(), "last": last.strip(), "house": row["house"].strip()})
                    else:
                        sys.exit("Invalid name format in input file")
                else:
                    sys.exit("INvalid input file format")


except FileNotFoundError:
    print("Could not read invalid_file.csv")
    sys.exit(1)
