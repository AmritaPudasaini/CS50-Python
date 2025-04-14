from fpdf import FPDF

class ShirtificateGenerator:
    def __init__(self, image_path):
        self.pdf = FPDF(orientation="portrait", format="A4")
        self.pdf.set_font("helvetica", 'B', 40)
        self.image_path = image_path
        self.pdf.add_page()

    def add_title(self):
        self.pdf.set_xy(0, 20)
        self.pdf.cell(0, 20, "CS50 Shirtificate", align="C")
        self.pdf.ln(20)

    def add_shirt_image(self):
        image_width = 150
        image_height = 150
        x = (210 - image_width)/2
        y = 80
        self.pdf.image(self.image_path, x=x, y=y, w=image_width, h=image_height)

    def add_name(self, name):
        self.pdf.set_text_color(255,255,255)
        self.pdf.set_font("helvetica", 'B', 25)

        self.pdf.set_xy(0, 130)
        self.pdf.cell(0, 10, f"{name} took CS50", align="C")
        self.pdf.ln(20)

    def save_pdf(self, output_path="shirtificate.pdf"):
        self.pdf.output(output_path)

def main():
    name = input("Name: ").strip()
    shirt = ShirtificateGenerator(image_path = "shirtificate.png")
    shirt.add_title()
    shirt.add_shirt_image()
    shirt.add_name(name)
    shirt.save_pdf()


if __name__ == "__main__":
    main()
