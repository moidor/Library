import os


def create_order_bill_docx(text, order_number, customer_lastname, order_date):
    bill_name = f"C:\\Users\\Cham\\PycharmProjects\\Library\\src\\streams\\" \
                f"order_bill n°{order_number}-{customer_lastname}-{order_date[:10]}.docx"
    bill_exists = os.path.exists(bill_name)
    print(f"Was the bill already printed ? {bill_exists}")
    if bill_exists:
        bill = open(bill_name, 'w')
        bill.write(text)
        bill.close()
        print(f"The bill already exists but has been downloaded once again within the name {bill_name}.")
    #  if file doesn't exist
    else:
        bill = open(bill_name, 'w')
        bill.write(text)
        bill.close()
        print(f"The bill has been downloaded within the name {bill_name}.")


class DOCX_bill:
    pass
