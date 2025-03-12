from fpdf import FPDF

name = input("Name: ")

pdf = FPDF()
ph, pw = pdf.h, pdf.w
pdf.add_page()
pdf.set_auto_page_break(0)

pdf.set_line_width(5)
pdf.set_fill_color(173, 216, 230)
pdf.rect(x = 0.00, y = 0.00, h = 297.0, w = 210.00, style = "DF")

# Add image
pdf.image("shirtificate.png", x = (pw - 190)/2, y = (ph - 200)/2, w = 190, h = 200)

# Add text at the same coordinates
pdf.set_font("helvetica", size = 50)
pdf.set_y(30)
pdf.cell(200, 20, text = "CS50 Shirtificate", align = 'C')

pdf.set_font("helvetica", size = 50/2)
pdf.set_y(120)
pdf.set_text_color(255, 255, 255)
pdf.cell(200, 20, text = name + " took CS50", align = 'C')

imh, imw = 50, 50
pdf.image("dd.png", x = (pw - imw)/2, y = 150, w = 50, h = 50)

pdf.output("my_pdf.pdf")