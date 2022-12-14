from fpdf import FPDF
import os


def create_order_bill_pdf(text, order_number, customer_lastname, order_date):
    bill_name = f"C:\\Users\\Cham\\PycharmProjects\\Library\\src\\streams\\" \
                f"order_bill n°{order_number}-{customer_lastname}-{order_date}.pdf"
    bill_exists = os.path.exists(bill_name)
    print(bill_exists)

    pdf = FPDF()
    pdf.add_page()
    # set style and size of font
    # that you want in the pdf
    pdf.set_font("Arial", size=15)
    # create a cell
    pdf.cell(200, 10, txt=f"{text}",
             ln=1, align='B')
    # add another cell
    # pdf.cell(200, 10, txt="A Computer Science portal for geeks.",
    #          ln=2, align='C')
    # save the pdf with name .pdf
    pdf.output(bill_name)
