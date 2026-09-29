from hotel import Hotel

def run_tests():
    hotel = Hotel("Test Hotel")

    hotel.guests.append(__import__("guest").Guest(1, "Test User", "9999999999"))
    assert hotel.find_guest(1).name == "Test User"

    room = hotel.find_room(101)
    assert room.is_available is True

    from booking import Booking
    booking = Booking(1, hotel.find_guest(1), room, 2)
    hotel.bookings.append(booking)
    room.is_available = False

    assert booking.total_amount == 3000
    assert room.is_available is False

    booking.check_out()
    assert room.is_available is True
    assert booking.status == "Checked Out"

    print("All validation tests passed.")

if __name__ == "__main__":
    run_tests()
