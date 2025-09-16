
order_amount = int(input("Enter the order amount: "))

# delivery_fee = 0

# if order_amount > 300:
#     delivery_fee = 0
# else:
#     delivery_fee = 50

delivery_fee = 0 if order_amount > 300 else 50

print(f"Delivery fee: ${delivery_fee}")
