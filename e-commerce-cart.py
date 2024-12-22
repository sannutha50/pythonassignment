def cal_total(cart):
    total = sum(cart.values())
    if len(cart) > 5:
        total = total - 42500
    return total
cart = {
    'laptop': 50000,
    'headphone': 2000,
    'Mouse': 35000,
    'Keyboard': 1500,
    'monitor': 8000,
    'usb driver': 1000
}
print(f"Total Price: {cal_total(cart)}")

