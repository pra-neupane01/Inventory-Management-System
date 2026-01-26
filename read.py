def read_data(file_path, is_found=False):
    """
    Reads the data from inventorty.txt
    Each line of the data file is stripped and splitted when it faces 
    commas, and the data is stored as a list inside the main list named
    'sales'.

    Args:
        file_path (str): The path of the file containing the inventory data

    Returns:
        list[list[str]]: A list of data where each data is enclosed as a list
                         of string values
    """
    sales=[]
    try:
        with open(file_path,"r") as file:
            is_found = True 
            data = file.readlines()

        for line in data:
            new_data = line.strip().split(",")
            sales.append(new_data) #appends each list of string to another list
    except FileNotFoundError:
        print("Error!",file_path, " not found.")        
    return sales, is_found
    
result = read_data("inventory.txt") #calling read_data function

    


    