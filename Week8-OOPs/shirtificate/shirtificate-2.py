from fpdf import FPDF

def name():
    return input("Name: ")

nam = name()
pdf = FPDF('P', 'mm', 'A4')
ph, pw = pdf.h, pdf.w
pdf.add_page()
pdf.set_auto_page_break(False)

#pdf.set_line_width(5)
#pdf.set_fill_color(173, 216, 230)
#pdf.rect(x = 0.00, y = 0.00, h = 297.0, w = 210.00, style = "DF")

# Add image
pdf.image("shirtificate.png", x = (pw - 190)/2, y = (ph - 160)/2, h = 190, w = 190)

# Add text at the same coordinates
pdf.set_font("helvetica", size = 50)
pdf.set_y(30)
pdf.cell(200, 20, text = "CS50 Shirtificate", align = 'C')

pdf.set_font("helvetica", size = 20)
pdf.set_y(130)
pdf.set_text_color(255, 255, 255)
pdf.cell(200, 10, text = nam + " took CS50", align = 'C')


pdf.output("shirtificate.pdf")
