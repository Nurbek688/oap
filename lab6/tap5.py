def subtotal(price, quantity):
    return price*quantity
def discount_amount(amount, rate):
    return amount*rate
def final_price(price, quantity, rate=0):
    amount=subtotal(price, quantity)
    return amount-discount_amount(amount, rate)
print(final_price(2500, 3, 0.10))