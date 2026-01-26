
from read import read_data
from operation import show_products,add_stock, purchase, sell

def main():
    """
    This is the main module to launch Speedzwear Wholesale system. 
    This function generates a menu having choices like display,
    purchase, add stock, sell or exit for managing wholesale system.
    """
    while True:
        print("\n.....SpeedzWear Wholesale System.....")
        print("1. Press (1) to Display Items")
        print("2. Press (2) to Purchase Item")
        print("3. Press (3) to Add Item's Stock")
        print("4. Press (4) to Sell Item")
        print("5. Press (5) to Exit")
        
        try:
            choice = int(input("Enter a choice: (1-5): "))
        except ValueError:
            print("Invalid Selection! Re-enter the valid choice between 1 and 5.")
            continue
        data, is_found = read_data("inventory.txt")
        if(not is_found):
            continue
        if choice == 1:
            print("\nCurrent Inventory:")
            show_products(data)
        elif choice == 2:
            purchase(data)
        elif choice == 3:
            add_stock(data)
        elif choice == 4:
            sell(data)
        elif choice == 5:
            print("Exiting......Exited!")
            break
        else:
            print("Invalid Selection \n")
                
                
            

if __name__ == '__main__':
    main()
