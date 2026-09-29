class Booking:
    def __init__(self, booking_id, guest, room, days):
        self.booking_id = booking_id
        self.guest = guest
        self.room = room
        self.days = days
        self.total_amount = room.price * days
        self.status = "Booked"

    def check_in(self):
        if self.status == "Booked":
            self.status = "Checked In"
            print("Checked in")
        elif self.status == "Checked In":
            print("Already checked in")
        else:
            print("Error")

    def check_out(self):
        if self.status == "Checked In" or self.status == "Booked":
            self.status = "Checked Out"
            self.room.is_available = True
            print("Checked out. Bill:", self.total_amount)
        else:
            print("Already closed")

    def cancel(self):
        if self.status in ["Booked", "Checked In"]:
            self.status = "Cancelled"
            self.room.is_available = True
            print("Cancelled")
        else:
            print("Error")

    def __str__(self):
        return f"{self.booking_id} {self.guest.name} {self.room.number} {self.status}"
