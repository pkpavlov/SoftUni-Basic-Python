square_m = float(input())
total = (square_m * 7.61)
discount = (square_m * 7.61) * 0.18
total_with_discount = total - discount

print(f"The final price is: {total_with_discount} lv.")
print(f"The discount is: {discount} lv.")