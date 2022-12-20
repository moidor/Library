from fpdf import FPDF
import os


def create_order_bill_pdf(order_number, order_date, customer_firstname, customer_lastname, seller, book):
    bill_name = f"C:\\Users\\Cham\\PycharmProjects\\Library\\src\\streams\\" \
                f"order_bill n°{order_number}-{customer_lastname}-{order_date[:10]}.pdf"
    bill_exists = os.path.exists(bill_name)
    print(f"Was the bill already printed ? {bill_exists}")

    pdf = FPDF()
    pdf.add_page()
    # Set style and size of font
    pdf.set_font("Arial", size=15)
    # pdf.text("dffff", 1)
    # Creating each cell to integrate one or multiple variables
    pdf.cell(200, 10, txt=f"Summary of the bill n°{order_number}", ln=1, align="C")
    pdf.cell(200, 20, txt=f"Customer: {customer_firstname} {customer_lastname.upper()}", ln=1, align="L")
    pdf.cell(200, 10, txt=f"Seller: {seller} - Date: {order_date}", ln=1, align="L")
    pdf.cell(200, 10, txt=f"Book: {book}", ln=1, align="L")

    if bill_exists:
        # Saving the PDF file formatted as in the variable above
        pdf.output(bill_name)
        print(f"The bill already exists but has been downloaded once again within the name {bill_name}.")
    #  if file doesn't exist
    else:
        # Saving the PDF file formatted as in the variable above
        pdf.output(bill_name)
        print(f"The bill has been downloaded within the name {bill_name}.")



