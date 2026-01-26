import datetime

def date_file():
    """
    Creates a String of the current date and time in the format of the 
    local system date and time. 
    The time stamp includes year, month, day, hour, minute, second, and 
    microsecond which are separed by underscore. This is done to create
    unique file names for invoice.

    Returns:
        str: A timestamp of string in the format of 
             'YYYY_MM_DD_HH_MM_SS_MS'.
    """
    current_time = datetime.datetime.now()
    year = current_time.year
    month = current_time.month
    day = current_time.day
    hour = current_time.hour
    minute = current_time.minute
    second = current_time.second
    milli_sec = current_time.microsecond
    
    timestamp = "{}_{}_{}_{}_{}_{}_{}".format(year, month, day, hour, minute, second, milli_sec)
    return timestamp
    
    

def write(data): 
    """
    Write updated data of inventory to inventory.txt file.
    
    Args:
        data (list): A list having data [product_name, brand, quantity, price, origin].
    """
    with open("inventory.txt", "w") as file:
        for i in data:
            if len(i) == 5:
                file.write(f"{i[0]},{i[1]},{i[2]},{i[3]},{i[4]}\n")


def add_stock_invoice(data):
    """
    Generates the invoice containing all the purchase details in tabular form.
    
    Args:
        data (list): A list having data [product_name, brand, quantity, unit_price, origin, total_price].
    """
    
    while True:
        try:
            ui_bill_no = int(input("Enter the bill number: "))
            if(ui_bill_no < 0):
                print("Please enter a valid positive number for bill number")
                continue
            break
        except ValueError:
            print("please enter a valid numeric data for bill number!.") 
    
    
    while True:
        ui_vendor_name = input("Enter the name of vendor: ").strip()
        name_check = ui_vendor_name.replace(" ", "")  # remove spaces
        valid = True

        for character in name_check:
            if character not in "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ":
                valid = False
                print("Please re-enter a valid name (alphabets only).")
                break

        if valid and ui_vendor_name != "":
            break

            
    
    ui_contact_num = input("Enter the contact number: ")
    ui_address = input("Enter the address: ")

    invoice_file_name = "add_stock_" + date_file() + ".txt"
    
    with open(invoice_file_name, 'w') as file:
        file.write("{:<20} {}\n".format("Bill No.:", ui_bill_no))
        file.write("{:<20} {}\n".format("Vendor Name:", ui_vendor_name))
        file.write("{:<20} {}\n".format("Contact Number:", ui_contact_num))
        file.write("{:<20} {}\n".format("Address:", ui_address))
        file.write("{:<20} {}-{}-{}\n".format("Date:", datetime.datetime.now().year, datetime.datetime.now().month, datetime.datetime.now().day))
        file.write("=" * 90 + "\n")
        
        
        file.write("{:<20}{:<15}{:<10}{:<12}{:<15}{:<15}\n".format(
            "Product Name", "Brand", "Quantity", "Unit Price", "Origin", "Total Amount"
        ))
        file.write("-" * 90 + "\n")

        item_total = 0
        for items in data:
            product_name, product_brand, product_quantity, product_price, product_origin, total_price = items
            item_total += total_price
            file.write("{:<20}{:<15}{:<10}{:<12.2f}{:<15}{:<15.2f}\n".format(
                product_name, product_brand, product_quantity, product_price, product_origin, total_price))

        vat_amount = item_total * 0.13
        overall_total = item_total + vat_amount

        file.write("-" * 90 + "\n")
        file.write("{:<72}{:<15.2f}\n".format("Item total", item_total))
        file.write("{:<72}{:<15.2f}\n".format("VAT (13%)", vat_amount))
        file.write("{:<72}{:<15.2f}\n".format("Overall Total", overall_total))
        file.write("=" * 90 + "\n")

    print("Invoice saved as {}".format(invoice_file_name))


def sell_invoice(data):
    """
    Generates the invoice containing all the purchase details along with
    disocunt and VAT in tabular form.

    Args:
        data (list): A list having data [product_name, brand, quantity, unit_price, origin].
    """

    while True:
        try:
            ui_bill_no = int(input("Enter the bill number: "))
            if(ui_bill_no < 0):
                print("Please enter a valid positive number for bill number")
                continue
            break
        except ValueError:
            print("please enter a valid numeric data for bill number!.") 
    
    
    while True:
        ui_customer_name = input("Enter the name of vendor: ").strip()
        name_check = ui_customer_name.replace(" ", "")  # remove spaces
        valid = True

        for character in name_check:
            if character not in "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ":
                valid = False
                print("Please re-enter a valid name (alphabets only).")
                break

        if valid and ui_customer_name != "":
            break
        
    ui_contact_num = input("Enter the contact number: ")
    ui_address = input("Enter the address: ")
    
    invoice_file_name = "sell_invoice_" + date_file() + ".txt"

    with open(invoice_file_name, 'w') as file:
        file.write("{:<20} {}\n".format("Bill No.:", ui_bill_no))
        file.write("{:<20} {}\n".format("Customer Name:", ui_customer_name))
        file.write("{:<20} {}\n".format("Contact Number:", ui_contact_num))
        file.write("{:<20} {}\n".format("Address:", ui_address))
        file.write("{:<20} {}-{}-{}\n".format("Date:", datetime.datetime.now().year, datetime.datetime.now().month, datetime.datetime.now().day))
        file.write("=" * 90 + "\n")
        
        file.write("{:<20}{:<15}{:<10}{:<12}{:<15}{:<15}{:<15}\n".format(
            "Product Name", "Brand", "Quantity", "Unit Price", "Origin", "Discount", "Final Amount"
        ))
        file.write("-" * 90 + "\n")

        item_total = 0
        total_discount = 0

        for items in data:
            product_name, product_brand, product_quantity, product_price, product_origin = items

            total_price = product_quantity * product_price
            discount_rate = 0
            if product_quantity > 10:
                discount_rate += 0.05
                if product_origin.lower() == "domestic":
                    discount_rate += 0.07

            discount_amount = total_price * discount_rate
            final_price = total_price - discount_amount

            item_total += final_price
            total_discount += discount_amount

            file.write("{:<20}{:<15}{:<10}{:<12.2f}{:<15}{:<15.2f}{:<15.2f}\n".format(
                product_name, product_brand, product_quantity, product_price, product_origin, discount_amount, final_price
            ))

        vat_amount = item_total * 0.13
        overall_total = item_total + vat_amount

        file.write("-" * 90 + "\n")
        file.write("{:<72}{:<15.2f}\n".format("Total Discount", total_discount))
        file.write("{:<72}{:<15.2f}\n".format("Item Total (After Discount)", item_total))
        file.write("{:<72}{:<15.2f}\n".format("VAT (13%)", vat_amount))
        file.write("{:<72}{:<15.2f}\n".format("Overall Total", overall_total))
        file.write("=" * 90 + "\n")

    print("Invoice saved as {}".format(invoice_file_name))


def purchase_invoice(data):
    """
    Generates the invoice containing all the purchase details along with
    VAT in tabular form.


    Args:
        data (list): A list having data [product_name, brand, quantity, unit_price, origin, total_price].
    """


    while True:
        try:
            ui_bill_no = int(input("Enter the bill number: "))
            if(ui_bill_no < 0):
                print("Please enter a valid positive number for bill number")
                continue
            break
        except ValueError:
            print("please enter a valid numeric data for bill number!.") 
    
    
    while True:
        ui_supplier_name = input("Enter the name of vendor: ").strip()
        name_check = ui_supplier_name.replace(" ", "")  # remove spaces
        valid = True

        for character in name_check:
            if character not in "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ":
                valid = False
                print("Please re-enter a valid name (alphabets only).")
                break

        if valid and ui_supplier_name != "":
            break
        
    ui_contact_num = input("Enter the contact number: ")
    ui_address = input("Enter the address: ")
    
    invoice_file_name = "purchase_invoice_" + date_file() + ".txt"
    


    with open(invoice_file_name, 'w') as file:
        file.write("{:<20} {}\n".format("Bill No.:", ui_bill_no))
        file.write("{:<20} {}\n".format("Supplier Name:", ui_supplier_name))
        file.write("{:<20} {}\n".format("Contact Number:", ui_contact_num))
        file.write("{:<20} {}\n".format("Address:", ui_address))
        file.write("{:<20} {}-{}-{}\n".format("Date:", datetime.datetime.now().year, datetime.datetime.now().month, datetime.datetime.now().day))
        file.write("=" * 90 + "\n")
        
        file.write("{:<20}{:<15}{:<10}{:<12}{:<15}{:<15}\n".format(
            "Product Name", "Brand", "Quantity", "Unit Price", "Origin", "Total Amount"
        ))
        file.write("-" * 90 + "\n")

        item_total = 0
        for items in data:
            product_name, product_brand, product_quantity, product_price, product_origin, total_price = items
            item_total += total_price
            file.write("{:<20}{:<15}{:<10}{:<12.2f}{:<15}{:<15.2f}\n".format(
                product_name, product_brand, product_quantity, product_price, product_origin, total_price
            ))

        vat_amount = item_total * 0.13
        overall_total = item_total + vat_amount

        file.write("-" * 90 + "\n")
        file.write("{:<72}{:<15.2f}\n".format("Item total", item_total))
        file.write("{:<72}{:<15.2f}\n".format("VAT (13%)", vat_amount))
        file.write("{:<72}{:<15.2f}\n".format("Overall Total", overall_total))
        file.write("=" * 90 + "\n")

    print("Invoice saved as {}".format(invoice_file_name))
