from tabulate import tabulate
import sys
import csv

if len(sys.argv) < 2:
    sys.exit("Too few command-line arguments")
elif len(sys.argv) > 2:
    sys.exit("Too many command-line arguments")

file_name = sys.argv[1]

if not file_name.endswith(".csv"):
        sys.exit("Not a csv file")

try:
    with open(sys.argv[1],"r") as file:
        reader = csv.reader(file)
        header = next(reader)
        data = [row for row in reader]
        print(tabulate(data, header, tablefmt="grid"))


except (FileNotFoundError):
    sys.exit("File does not exist")
