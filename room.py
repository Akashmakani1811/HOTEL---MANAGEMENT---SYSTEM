class Room:
    def __init__(self, number, room_type, price):
        self.number = number
        self.room_type = room_type
        self.price = price
        self.is_available = True

    def __str__(self):
        return f"{self.number} {self.room_type} {self.price} {self.is_available}"
