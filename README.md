# 📦 Inventory Management System (Python)
### File-Based Console Application  
**Author: Pralad Neupane**

---

## 🚀 Project Overview

The Inventory Management System is a console-based Python application designed to manage product inventory, handle sales and purchases, and generate invoice files automatically.

The system operates using file handling techniques and demonstrates:

- Inventory tracking
- Purchase operations
- Sales operations
- Automatic invoice generation
- File read/write operations
- Modular programming structure

This project showcases strong understanding of Python fundamentals and file-based data management.

---

## 🛠 Technologies Used

- Python 3
- File Handling (Text Files)
- Modular Programming
- Console-Based User Interface

---

## 📁 Project Structure

```
inventory.txt
main.py
operation.py
read.py
write.py
purchase_invoice_*.txt
sell_invoice_*.txt
```

---

## 📌 File Descriptions

### 🔹 main.py
Entry point of the program.  
Handles user interaction and menu options.

---

### 🔹 operation.py
Contains core logic for:
- Buying products
- Selling products
- Updating inventory
- Generating invoices

---

### 🔹 read.py
Handles reading inventory data from `inventory.txt`.

---

### 🔹 write.py
Handles writing updated inventory data back to file.

---

### 🔹 inventory.txt
Stores all product details including:
- Product Name
- Brand
- Quantity
- Cost Price
- Selling Price

---

### 🔹 Invoice Files
Automatically generated during transactions:
- `purchase_invoice_*.txt`
- `sell_invoice_*.txt`

Each invoice includes:
- Customer/Supplier Name
- Date and Time
- Purchased/Sold Items
- Total Amount

---

## ⚙️ How To Run The Project

1️⃣ Make sure Python is installed:

```bash
python --version
```

2️⃣ Navigate to project directory:

```bash
cd your_project_folder
```

3️⃣ Run the program:

```bash
python main.py
```

---

## 🧩 Features

- View Available Inventory
- Purchase Items (Increase Stock)
- Sell Items (Decrease Stock)
- Automatic Stock Update
- Invoice Generation
- File-Based Data Persistence
- Error Handling for Invalid Inputs

---

## 🧾 Sample Inventory Format

```
Product1,BrandA,50,200,250
Product2,BrandB,30,150,200
```

---

## 🧾 Sample Invoice Output

```
-----------------------------------
        SALES INVOICE
-----------------------------------
Customer Name: John Doe
Date: 2025-08-29

Product: Product1
Quantity: 2
Price: 250
Total: 500

Grand Total: 500
-----------------------------------
```

---

## 🏗 System Workflow

1. Program starts from `main.py`
2. User selects operation
3. Data is read from `inventory.txt`
4. Operation is performed
5. Updated data is written back
6. Invoice file is generated

---

## 🎯 Learning Outcomes

- Python file handling
- Modular programming
- Data persistence
- Console-based application design
- Invoice generation logic
- Structured code organization

---

## 🧠 Key Concepts Demonstrated

- Functions
- Lists & Dictionaries
- File I/O
- Exception Handling
- Date & Time Handling
- Dynamic File Naming

---

## 🏆 Project Highlights

- Clean modular design
- Automatic invoice generation
- Structured inventory management
- Beginner-to-Intermediate Python project
- Academic + Portfolio Ready

---

## 👨‍💻 Author

**Pralad Neupane**  
Python Developer  
Inventory Management System Project
