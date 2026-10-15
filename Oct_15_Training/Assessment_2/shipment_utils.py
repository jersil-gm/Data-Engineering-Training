# shipment_utils.py


# 33. Reusable shipment functions
def calculate_shipping_cost(weight, rate=75):
    return weight * rate


def classify_shipment_weight(weight):
    if weight > 20:
        return "Heavy"
    elif weight >= 10:
        return "Medium"
    return "Light"