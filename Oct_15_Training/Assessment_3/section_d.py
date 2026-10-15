# section_d.py


# 36-38. Event Base Class
class Event:

    def __init__(self, event_id, event_name, capacity, ticket_price):
        self.event_id = event_id
        self.event_name = event_name
        self.capacity = capacity
        self.ticket_price = ticket_price

    def display_event(self):
        print(
            f"[Event] ID: {self.event_id} | Name: {self.event_name} | "
            f"Capacity: {self.capacity} | Price: ₹{self.ticket_price}"
        )

    def calculate_revenue(self, tickets_sold):
        return tickets_sold * self.ticket_price


# 39. Create two Event objects
event1 = Event("E101", "AI Summit", 500, 2500)
event2 = Event("E102", "Leadership Forum", 350, 3500)

print("--- Event Objects ---")
event1.display_event()
event2.display_event()
print(f"Revenue for 100 tickets at {event1.event_name}: ₹{event1.calculate_revenue(100)}")


# 40-42. OnlineEvent Child Class
class OnlineEvent(Event):

    def __init__(self, event_id, event_name, capacity, ticket_price, platform):
        super().__init__(event_id, event_name, capacity, ticket_price)
        self.platform = platform

    def display_event(self):
        print(
            f"[OnlineEvent] ID: {self.event_id} | Name: {self.event_name} | "
            f"Platform: {self.platform} | Price: ₹{self.ticket_price}"
        )


# 43-44. PhysicalEvent Child Class
class PhysicalEvent(Event):

    def __init__(self, event_id, event_name, capacity, ticket_price, venue):
        super().__init__(event_id, event_name, capacity, ticket_price)
        self.venue = venue

    def display_event(self):
        print(
            f"[PhysicalEvent] ID: {self.event_id} | Name: {self.event_name} | "
            f"Venue: {self.venue} | Price: ₹{self.ticket_price}"
        )


# 45-46. Polymorphism Demonstration
online = OnlineEvent("E201", "Cloud Masterclass", 1000, 1500, "Zoom")
physical = PhysicalEvent("E202", "Design Expo", 250, 2000, "HITEX Hyderabad")

events_list = [online, physical]
print("\n--- Polymorphic Event Display ---")
for ev in events_list:
    ev.display_event()