def calculate_price():
    price = 100
    tax = price * 0.1
    print(f"Total: {price + tax}")


calculate_price()  # Total: 110

# This fails - price doesn't exist outside the function
# print(price)  # NameError: name 'price' is not defined


discount_rate = 0.15  # Global variable


def apply_discount(price):
    discount = price * discount_rate  # Can read global variable
    return price - discount


result = apply_discount(100)
print(result)  # 85.0


counter = 0  # Global variable


def increment():
    # global counter  # Declare we want to modify the global variable
    counter += 1


increment()
increment()
print(counter)  # 2
