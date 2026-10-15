# event_utils.py


def calculate_booking_amount(ticket_price, tickets):
    return ticket_price * tickets


def calculate_discount(amount):
    if amount >= 10000:
        return amount * 0.10
    return amount * 0.05


def check_event_capacity(registered, capacity):
    if registered > capacity:
        return "Invalid Data"
    elif registered == capacity:
        return "Full"
    return "Seats Available"