# retail_utils.py


# 56. Functions for total, discount, and stock check
def calculate_order_total(price, quantity):
    return price * quantity


def calculate_discount(amount):
    if amount >= 50000:
        return amount * 0.10
    return amount * 0.05


def check_stock(stock):
    if stock > 20:
        return "High Stock"
    elif stock > 0:
        return "Low Stock"
    return "Out of Stock"