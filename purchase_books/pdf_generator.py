from fpdf import FPDF


def generate_receipt(customer_name, book_name, price, book_id):
    pdf = FPDF(orientation="P", format="A4", unit="mm")
    pdf.add_page()

    pdf.set_font(family="Helvetica", style="B", size=12)
    pdf.cell(w=0, h=12, align='l', txt=f"id.{book_id}", ln=1)

    pdf.set_font(family="Helvetica", style="I", size=10)
    pdf.cell(w=0, h=8, align='l', txt=f"Purchaser : {customer_name}", ln=1)

    pdf.set_font(family="Helvetica", style="I", size=10)
    pdf.cell(w=0, h=8, align='l', txt=f"Name of book: {book_name}", ln=1)

    pdf.set_font(family="Helvetica", style="B", size=12)
    pdf.cell(w=0, h=12, align='l', txt=f"Price: {price}", ln=1)

    pdf.output("receipt.pdf")

