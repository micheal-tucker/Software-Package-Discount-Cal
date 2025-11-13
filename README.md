# 📦 Software Package Discount Calculator  
A simple Python program that calculates quantity-based discounts for software package purchases. This project demonstrates the use of conditional logic (`if`, `elif`, `else`), arithmetic operations, user input handling, and clean structured program design.

---

## 📘 Project Description  
A software company sells a package that retails for **Le 100**.  
Customers receive discounts based on the number of packages purchased:

| Quantity Range | Discount |
|----------------|----------|
| 0–9            | 0%       |
| 10–19          | 20%      |
| 20–49          | 30%      |
| 50–99          | 40%      |
| 100+           | 50%      |

This program asks the user to enter the number of packages purchased, calculates the appropriate discount, and displays:

- The **discount rate**
- The **discount amount**
- The **total price after discount**

---

## 🧠 Features
- Accepts user input for quantity  
- Applies correct discount using conditional logic  
- Calculates and displays:  
  - Discount percentage  
  - Discount amount  
  - Final price after discount  
- Easy to run and modify  
- Beginner–friendly, good for learning Python basics  

---

## 🧮 How It Works (Logic Breakdown)

1. User enters number of packages  
2. Program checks which discount bracket the number falls into  
3. Discount rate is applied  
4. Program calculates:  
   - `totalBefore = quantity * price_per_package`  
   - `discountAmount = totalBefore * discountRate`  
   - `totalAfter = totalBefore - discountAmount`
5. Outputs results clearly  

---

## 🧾 Code (discount.py)

```python
def main():
    quantity = int(input("Enter the number of packages purchased: "))
    
    price_per_package = 100
    
    if quantity < 10:
        discount_rate = 0
    elif 10 <= quantity <= 19:
        discount_rate = 0.2
    elif 20 <= quantity <= 49:
        discount_rate = 0.3
    elif 50 <= quantity <= 99:
        discount_rate = 0.4
    else:
        discount_rate = 0.5
    
    total_before = quantity * price_per_package
    discount_amount = total_before * discount_rate
    total_after = total_before - discount_amount
    
    print(f"Discount rate: {discount_rate * 100}%")
    print(f"Discount amount: Le {discount_amount}")
    print(f"Total after discount: Le {total_after}")

main()
