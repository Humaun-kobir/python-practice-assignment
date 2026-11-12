# Customer Name: Rahim
# Product 1: Keyboard
# Price: 1500
# Product 2: Mouse
# Price: 800
# Product 3: Headphone
# Price: 2000


name = input("Enter customer name: ")

p1_name = input("Product 1 name: ")
p1_price = float(input("Product 1 price: "))

p2_name = input("Product 2 name: ")
p2_price = float(input("Product 2 price: "))

p3_name = input("Product 3 name: ")
p3_price = float(input("Product 3 price: "))


subtotal = p1_price + p2_price + p3_price

if subtotal >= 5000:
  rate = 0.20
elif subtotal >= 3000:
  rate = 0.10
elif subtotal >= 1000:
  rate = 0.05
else:
  rate = 0.0

discount = subtotal * rate
final_total = subtotal - discount


print("\nCustomer Name:", name)
print("Product 1:", p1_name, "-", p1_price)
print("Product 2:", p2_name, "-", p2_price)
print("Product 3:", p3_name, "-", p3_price)
print("Subtotal:", subtotal)
print("Discount:", discount)
print("Final Total:", final_total)
