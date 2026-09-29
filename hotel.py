from guest import Guest
from room import Room
from booking import Booking
from validation import get_non_empty, get_positive_int

class Hotel:
    def __init__(self, name):
        self.name = name
        self.guests = []
        self.rooms = []
        self.bookings = []
        self._create_rooms()

    def _create_rooms(self):
        room_data = [(101, "Single", 1500), (102, "Single", 1500), (201, "Double", 2500), (202, "Double", 2500), (301, "Deluxe", 4000), (302, "Deluxe", 4000)]
        for r in room_data:
            self.rooms.append(Room(r[0], r[1], r[2]))

    def find_guest(self, guest_id):
        for g in self.guests:
            if g.guest_id == guest_id: return g
        return None

    def find_room(self, room_number):
        for r in self.rooms:
            if r.number == room_number: return r
        return None

    def find_booking(self, booking_id):
        for b in self.bookings:
            if b.booking_id == booking_id: return b
        return None

    def add_guest_from_input(self):
        guest_id = get_positive_int("Guest ID: ")
        if self.find_guest(guest_id):
            print("Exists")
            return
        self.guests.append(Guest(guest_id, get_non_empty("Name: "), get_non_empty("Phone: ")))
        print("Done")

    def show_guests(self):
        for g in self.guests: print(g)

    def show_rooms(self):
        for r in self.rooms: print(r)

    def book_room_from_input(self):
        guest = self.find_guest(get_positive_int("Guest ID: "))
        room = self.find_room(get_positive_int("Room number: "))
        days = get_positive_int("Days: ")
        
        if not guest or not room or not room.is_available:
            print("Error")
            return

        b = Booking(len(self.bookings) + 1, guest, room, days)
        self.bookings.append(b)
        room.is_available = False
        print("Booked")

    def check_in_from_input(self):
        b = self.find_booking(get_positive_int("Booking ID: "))
        if b: b.check_in()

    def check_out_from_input(self):
        b = self.find_booking(get_positive_int("Booking ID: "))
        if b: b.check_out()

    def cancel_booking_from_input(self):
        b = self.find_booking(get_positive_int("Booking ID: "))
        if b: b.cancel()

    def search_guest_from_input(self):
        keyword = get_non_empty("Search: ").lower()
        for g in self.guests:
            if keyword in g.name.lower() or keyword == str(g.guest_id):
                print(g)

    def show_summary(self):
        print("Rooms:", len(self.rooms))
        print("Guests:", len(self.guests))
        print("Bookings:", len(self.bookings))
