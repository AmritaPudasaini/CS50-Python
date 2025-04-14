from PIL import Image, ImageOps
import sys

if len(sys.argv) < 3:
    sys.exit("Too few command-line arguments")
elif len(sys.argv) > 3:
    sys.exit("Too many command-line arguments")

input_file = sys.argv[1]
output_file = sys.argv[2]

valid_extensions = [".jpg", ".jpeg", ".png"]
input_ext = input_file.lower().rsplit('.', 1)[-1]
output_ext = output_file.lower().rsplit('.', 1)[-1]

if f".{input_ext}" not in valid_extensions or f".{output_ext}" not in valid_extensions:
    sys.exit("Invalid file format. Supported formats: .jpg, .jpeg, .png")
if input_ext != output_ext:
    sys.exit("Input and output file extensions do not match")

try:
    input_image = Image.open(input_file)
except FileNotFoundError:
    sys.exit("Input file does not exist")
except Exception as e:
    sys.exit(f"Error opening input file: {e}")

try:
    shirt_image = Image.open("shirt.png")
    input_image = ImageOps.fit(input_image, shirt_image.size)
    input_image.paste(shirt_image, (0, 0), shirt_image)
    input_image.save(output_file)
    print(f"Output saved as {output_file}")
except Exception as e:
    sys.exit(f"An error occurred: {e}")
