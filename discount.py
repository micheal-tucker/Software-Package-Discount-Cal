def main():
    quantity = int(input("Enter the number of packages purchased: "))
    
    price_per_package = 100
    
    # Determine discount rate
    if quantity < 10:
        discount_rate = 0
    elif 10 <= quantity <= 19:
        discount_rate = 0.2
    elif 20 <= quantity <= 49:
        discount_rate = 0.3
    elif 50 <= quantity <= 99:
        discount_rate = 0.4
    else:
        discount_rate = 0.5   # 100 and above
    
    # Calculations
    total_before = quantity * price_per_package
    discount_amount = total_before * discount_rate
    total_after = total_before - discount_amount
    
    # Output
    print(f"Discount rate: {discount_rate * 100}%")
    print(f"Discount amount: Le {discount_amount}")
    print(f"Total after discount: Le {total_after}")

main()
