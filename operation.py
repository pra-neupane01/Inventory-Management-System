from write import write, add_stock_invoice, sell_invoice, purchase_invoice

def show_products(data):
    print("-" * 80)
    print("| {:<20} | {:<12} | {:<10} | {:<10} | {:<12} |".format("Name", "Brand", "Quantity", "Price", "Origin"))
    print("-" * 80)
    
    for item in data:
        print("| {:<20} | {:<12} | {:<10} | {:<10} | {:<12} |".format(item[0], item[1], item[2], item[3], item[4]))
        print("-" * 80)
        
def purchase(data):
    """ 
    Facilitates the process of purchasing new product, by taking user-inputs,
    verifying them and extracting invoice data to be processed.
    Provides platform to add new items.

    Args:
        data (list): A list of the products availabe in the inventory
                      
    """
    invoice_data = []
    while True:
        ui_product_name = input("Enter the name of product: ")
        ui_product_brand = input("Enter the brand of product: ")
        
        while True:
            try:
                ui_product_quantity = int(input("Enter the quantity of product:"))
                if(ui_product_quantity<0):
                    print("Quantity can not be negative.")
                    continue
                break
            except ValueError:
                print("please enter a valid numeric data for quantity!.") 
                
        while True:
            try:
                ui_product_price = float(input("Enter the product price: "))
                if(ui_product_price<0):
                    print("Price cannot be negative.")
                    continue
                break
            except ValueError:
                print("Please enter a valid numeric data for price!.")     
                
        while True:
            ui_product_origin = input("Enter the originality of product (domestic/international): ").strip().lower()
            if ui_product_origin not in ["domestic", "international"]:
                print(" Invalid input, Re-enter valid choice.")
                continue
            break
        
        data.append([ui_product_name,ui_product_brand, ui_product_quantity, ui_product_price,ui_product_origin])
        print("Item successfully purchased!")
        invoice_data.append([ui_product_name,ui_product_brand, ui_product_quantity, ui_product_price,ui_product_origin, ui_product_quantity * ui_product_price])

        more_purchase = input("Do you want to purchase more product? (yes/no): ").lower()
        if more_purchase != "yes":
            break
    write(data)
    
    if invoice_data:
        purchase_invoice(invoice_data)
        


def add_stock(data):
    """
    Facilitates the process of adding stock of existing product, by taking user-inputs,
    verifying them and extracting invoice data to be processed.
    Increases the stock of items after successful purchase.

    Args:
        data (list): A list of products of the inventory
    """

    invoice_data = []
    while True:
        ui_product_name = input("Enter the name of product: ").strip().lower()
        found = False
        i = -1
        for i in range(len(data)):
            stored_product_name = data[i][0]
            if stored_product_name.lower() == ui_product_name:
                found = True
                break
        
        if not found:
            print("Sorry, The entered product is not available!..")
            continue
            
       
        while True:
            try:
                ui_product_quantity = int(input("Enter the quantity of product:"))
                if(ui_product_quantity<0):
                    print("Quantity can not be negative.")
                    continue
                break
            except ValueError:
                print("please enter a valid numeric data for quantity!.")
        
       
        stored_product_name = data[i][0]
        stored_product_brand = data[i][1] 
        stored_product_quantity = data[i][2]
        stored_product_price = float(data[i][3])
        stored_product_origin = data[i][4] 
        
        data[i][2] = int(stored_product_quantity) + ui_product_quantity
        new_quantity = data[i][2]
        print("--------------Updated Item--------------")
        print("Product Name:", ui_product_name, "\n New Quantity:", new_quantity)
        invoice_data.append([stored_product_name,stored_product_brand, ui_product_quantity, stored_product_price,stored_product_origin, ui_product_quantity * stored_product_price])
        
        write(data)
        
        more_purchase = input("Do you want to add more stock? (yes/no): ").lower()
        if more_purchase != "yes":
            break

    if invoice_data:
        add_stock_invoice(invoice_data)


def sell(data):
    """
    Facilitates the process of selling item in stock, by taking user-inputs,
    verifying them and extracting invoice data to be processed.
    Reduces the stock of inventory after successful sell.
    

    Args:
        data (list):  A list of products of the inventory
    """
    invoice_data = []
    while True:
        ui_product_name = input("Enter the name of product: ").strip().lower()
        
        
        found = False
        i = -1
        
        for i in range(len(data)):
            stored_product_name = data[i][0]
            if stored_product_name.lower() == ui_product_name:
                found = True
                break
        
        if not found:
            print("Sorry, The entered product is not available!..")
            continue
        
        while True:
            try:
                ui_product_quantity = int(input("Enter the quantity of product:"))
                if(ui_product_quantity<0):
                    print("Quantity can not be negative.")
                    continue
                break
            except ValueError:
                print("please enter a valid numeric data for quantity!.")
        found = False
        for i in range(len(data)):
            stored_product_name = data[i][0]
            stored_product_brand = data[i][1]
            stored_product_quantity = data[i][2]
            stored_product_price = float(data[i][3])
            stored_product_origin = data[i][4] 
            
            
            if stored_product_name.strip().lower() == ui_product_name: # redundant!.
                if int(stored_product_quantity) >= ui_product_quantity:
                   
                    data[i][2] = int(stored_product_quantity) - ui_product_quantity
                    remaining_stock = data[i][2]
                    invoice_data.append([stored_product_name, stored_product_brand, ui_product_quantity, stored_product_price, stored_product_origin])
                    print(f"Sold {ui_product_quantity} of {stored_product_name}. Remaining stock: {remaining_stock}")
                    found = True
                    write(data)
                else:
                    print("Not enough stock!")
                break

        if not found:
            print("Invalid product name!")

        more_sell = input("Do you want to sell more products? (yes/no): ").lower()
        if more_sell != "yes":
            break

    if invoice_data:
        sell_invoice(invoice_data)
