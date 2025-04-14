import sys

if len(sys.argv) < 2:
    sys.exit("Too few command-line arguments")
elif len(sys.argv) > 2:
    sys.exit("Too many command-line arguments")

file_name = sys.argv[1]

if not file_name.endswith(".py"):
    sys.exit("Not a Python file")

try:
    count = 0
    with open(file_name, "r") as file:
        for line in file:
            stripped_line = line.strip()
            if stripped_line.startswith("#") or len(stripped_line) == 0:
                continue
            count += 1
    print(count)

except FileNotFoundError:
    sys.exit("File does not exist")
