from hotel import Hotel

def main():
    hotel = Hotel("Royal Stay Hotel")
    while True:
        print("1.Add Guest 2.Guests 3.Rooms 4.Book 5.In 6.Out 7.Cancel 8.Search 9.Summary 0.Exit")
        choice = input("Choice: ")
        
        if choice == "1": hotel.add_guest_from_input()
        elif choice == "2": hotel.show_guests()
        elif choice == "3": hotel.show_rooms()
        elif choice == "4": hotel.book_room_from_input()
        elif choice == "5": hotel.check_in_from_input()
        elif choice == "6": hotel.check_out_from_input()
        elif choice == "7": hotel.cancel_booking_from_input()
        elif choice == "8": hotel.search_guest_from_input()
        elif choice == "9": hotel.show_summary()
        elif choice == "0": break
        else: print("Invalid")

if __name__ == "__main__":
    main()
