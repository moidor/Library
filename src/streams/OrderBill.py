import os


def create_order_bill(text, order_number, customer_lastname, order_date):
    bill_name = f"C:\\Users\\Cham\\PycharmProjects\\Library\\src\\streams\\" \
                f"order_bill n°{order_number}-{customer_lastname}-{order_date}.docx"
    bill_exists = os.path.exists(bill_name)
    print(bill_exists)
    if bill_exists:
        bill = open(f"{bill_name}", "w")
        bill.write(text)
        bill.close()
        print(f"The bill already exists but has been downloaded once again within the name {bill_name}.")
    #  if file doesn't exist
    else:
        bill = open(f"{bill_name}", "w")
        bill.write(text)
        bill.close()
        print(f"The bill has been downloaded within the name {bill_name}.")


class OrderBill:
    pass
