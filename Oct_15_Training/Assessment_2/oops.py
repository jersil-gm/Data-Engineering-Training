# section_oop.py


# 18-20. Shipment base class
class Shipment:

    def __init__(self, shipment_id, destination, weight, cost):
        self.shipment_id = shipment_id
        self.destination = destination
        self.weight = weight
        self.cost = cost

    def display(self):
        print(
            f"[Standard] ID: {self.shipment_id} | Dest: {self.destination} | Weight: {self.weight}kg | Cost: Rs. {self.cost}"
        )


# 21-22. ExpressShipment child class with surcharge override
class ExpressShipment(Shipment):

    def __init__(
        self, shipment_id, destination, weight, cost, surcharge=250.0
    ):
        super().__init__(shipment_id, destination, weight, cost)
        self.surcharge = surcharge

    def display(self):
        total_cost = self.cost + self.surcharge
        print(
            f"[Express]  ID: {self.shipment_id} | Dest: {self.destination} | Weight: {self.weight}kg | Total Cost: Rs. {total_cost} (Incl. Surcharge: Rs. {self.surcharge})"
        )


# 23. Demonstrate polymorphism using normal and express shipment objects
print("--- Polymorphism Demonstration ---")
s1 = Shipment("S1001", "Hyderabad", 12.5, 850)
s2 = ExpressShipment("S1002", "Mumbai", 8.0, 620, surcharge=200)

shipment_list = [s1, s2]
for item in shipment_list:
    item.display()